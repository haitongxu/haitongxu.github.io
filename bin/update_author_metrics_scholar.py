#!/usr/bin/env python3
import os, re, sys, random
from datetime import datetime, timezone

import requests

OUT = "_data/metrics.yml"
USER_ID = os.getenv("GSCHOLAR_USER", "").strip()
HL = os.getenv("GSCHOLAR_HL", "en").strip()

UA_LIST = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17 Safari/605.1.15",
]

def read_existing():
    if not os.path.exists(OUT):
        return None
    with open(OUT, "r", encoding="utf-8") as f:
        return f.read()

def write_yaml(text: str):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

def parse_metrics(html: str):
    # 抓 profile 指标表里的数字（All 列），通常会出现 >=3 个数字
    nums = re.findall(r'class="gsc_rsb_std">(\d+)<', html)
    if len(nums) < 3:
        return None
    return int(nums[0]), int(nums[1]), int(nums[2])

def main():
    if not USER_ID:
        print("Missing env GSCHOLAR_USER (your Scholar user id).")
        sys.exit(1)

    url = f"https://scholar.google.com/citations?user={USER_ID}&hl={HL}"
    headers = {"User-Agent": random.choice(UA_LIST)}

    existing = read_existing()

    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")

        parsed = parse_metrics(r.text)
        if not parsed:
            # 把返回页前几行打出来，方便你在 Actions 日志里判断是不是验证码/同意页
            snippet = r.text[:400].replace("\n", " ")
            raise RuntimeError(f"Parse failed. HTML head: {snippet}")

        citations, hindex, i10 = parsed
        now = datetime.now(timezone.utc).isoformat()

        yml = (
            f"source: google_scholar\n"
            f"user: {USER_ID}\n"
            f"updated_at: \"{now}\"\n"
            f"status: ok\n"
            f"total_citations: {citations}\n"
            f"h_index: {hindex}\n"
            f"i10_index: {i10}\n"
        )
        write_yaml(yml)
        print("Updated _data/metrics.yml from Google Scholar.")
        return

    except Exception as e:
        now = datetime.now(timezone.utc).isoformat()
        # 失败就保留旧文件内容；如果旧文件不存在，就写一个 error 版
        if existing and existing.strip():
            # 在旧内容后面追加一行错误（不破坏旧值）
            yml = existing.rstrip() + "\n" + f"last_error: \"{str(e).replace('\"','\\\"')}\"\n" + f"updated_at: \"{now}\"\n" + "status: error\n"
            write_yaml(yml)
        else:
            yml = (
                f"source: google_scholar\n"
                f"user: {USER_ID}\n"
                f"updated_at: \"{now}\"\n"
                f"status: error\n"
                f"last_error: \"{str(e).replace('\"','\\\"')}\"\n"
                f"total_citations: 0\n"
                f"h_index: 0\n"
                f"i10_index: 0\n"
            )
            write_yaml(yml)

        print(f"Failed to update; kept existing if present. Reason: {e}")

if __name__ == "__main__":
    main()
