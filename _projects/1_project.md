---
layout: page
title: AutoOcean
description: Distributed Intelligent decision-making system of Multi Autonomous surface vehicles for sustainable ocean monitoring
img: assets/img/autoocean/mit-portuggal.png
importance: 1
category: work
related_publications: true
---

## Abstract: 
The ocean plays a pivotal role in the blue economy. However, the increasing intensity of economic activities exerts significant pressure on the marine environment, thereby threatening ocean health. Sustaining ocean health requires advanced observation systems capable of delivering persistent, wide-area monitoring. Autonomous surface vehicles (ASVs) provide a promising solution; however, single ASVs face limitations in endurance, communication, and data storage. Multi-ASV systems can overcome these barriers, but coordinating their operations poses significant challenges due to underactuated dynamics, poor manoeuvrability, and the risk of collision in confined or dynamic ocean environments.

This project proposes the development of a distributed intelligent ocean monitoring system using multi-ASVs, with the long-term goal of enabling efficient and adaptive ocean observation. In collaboration with Dr. Michael Benjamin at MIT, the study focuses on creating an onboard distributed decision-making framework for optimal path planning. The system will employ multi-objective optimisation methods to ensure complete coverage of designated areas while avoiding collisions and accounting for the kinematic constraints of ASVs. Three custom-built ASVs at CENTEC and eight Heron ASVs at MIT will be deployed to conduct preliminary experimental tests, validating the proposed approach through evaluation of coverage efficiency and real-time navigation performance.

The project outcomes are expected to provide a cost-effective, scalable, and intelligent solution for sustainable ocean observation, with broader benefits for periodic monitoring and offshore inspection. By advancing distributed autonomy in multi-ASV systems, the project directly contributes to the development of measurement technologies aligned with Earth systems research priorities, particularly in ocean monitoring.

## PT PIs:
Haitong Xu, Centre for Marine Technology and Ocean Engineering (CENTEC), Instituto Superior Técnico

## MIT PIs:
Michael Benjamin, Center for Ocean Engineering, Department of Mechanical Engineering, MIT


To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
