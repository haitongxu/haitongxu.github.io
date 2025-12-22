#!/usr/bin/env python3
import json
import os
import random
import re
import sys
from datetime import datetime, timezone

import requests

OUT = "_data/metrics.json"
USER_ID = os.getenv("GSCHOLAR_USER", "").strip()
HL = os.getenv("GSCHOLAR_HL", "en").strip()

# 友好一些：别像机器人
UA_LIST = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17 Safari/605.1.15",
]

def load_existing():
    if os.path.exists(OUT):
        try:
            with open(OUT, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save(payload):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def parse_metrics(html: str):
    """
    Scholar profile 页面里有一个 metrics 表（Citations / h-index / i10-index）
    我们只取 “All” 那一列（总计），不取 “Since YYYY”。
    """
    # 粗暴但够用：先把表格中 All 列的三行数字抓出来
    # 常见顺序：Citations, h-index, i10-index
    nums = re.findall(r'class="gsc_rsb_std">(\d+)<', html)
    if len(nums) < 3:
        return None

    # 有的页面会有 6 个数字（All + Since），我们取前三个当 All
    citations = int(nums[0])
    hindex = int(nums[1])
    i10 = int(nums[2])
    return citations, hindex, i10

def main():
    if not USER_ID:
        print("Missing env GSCHOLAR_USER (your Scholar user id).")
        sys.exit(1)

    url = f"https://scholar.google.com/citations?user={USER_ID}&hl={HL}"
    headers = {"User-Agent": random.choice(UA_LIST)}
    existing = load_existing()

    try:
        r = requests.get(url, headers=headers, timeout=30)
        # 429 / 503 都可能出现
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")

        parsed = parse_metrics(r.text)
        if not parsed:
            raise RuntimeError("Parse failed")

        citations, hindex, i10 = parsed
        payload = {
            "source": "google_scholar",
            "user": USER_ID,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "total_citations": citations,
            "h_index": hindex,
            "i10_index": i10,
            "status": "ok",
        }
        save(payload)
        print("Updated metrics from Google Scholar.")
        return

    except Exception as e:
        # 失败兜底：保留旧值，并记录失败原因
        payload = existing or {}
        payload.update({
            "source": "google_scholar",
            "user": USER_ID,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "status": "error",
            "error": str(e),
        })
        save(payload)
        print(f"Failed to update, kept existing values. Reason: {e}")

if __name__ == "__main__":
    main()
