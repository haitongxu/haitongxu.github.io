---
layout: page
title: DEWATRA
description: focuses on addressing the challenge of global warming and its connection to rising Earth temperatures.
img: assets/img/DEWATRA/dewatra_logo.jpeg
importance: 2
category: PI
giscus_comments: true
---

## Description
The proposed project, focuses on addressing the challenge of global warming and its connection to rising Earth temperatures, with a particular emphasis on the role of the shipping industry in international trade. It introduces the concept of “green shipping” as a comprehensive approach to enhance environmental conditions within the shipping sector.

The project outlines various technological and operational strategies, including optimizing ship hull design, implementing energy-saving devices, exploring alternative fuels, utilizing wind energy, and employing artificial neural networks (ANN) for predicting fuel consumption and emissions. Additionally, it highlights the use of Automatic Identification System (AIS) data for studying ship emissions’ impact on air quality.

The primary objective of the proposed project is to achieve a higher level of sustainability in shipping by reducing CO2 emissions, enhancing energy efficiency, and ensuring compliance with international regulations. This initiative sets clear and ambitious goals, such as developing numerical models, assessing the performance of technology combinations, fostering capacity-building, and influencing transport policy measures to promote sustainable maritime practices.

---

### Working Groups

| Number | Title                                                                 | Leader             | Vice-Leader       |
|:-----:|-----------------------------------------------------------------------|---------------------------|-----------------|
| 1     | WG1. Assessment of atmospheric emissions from shipping                | Prof Jin Wang     |  Prof Selma Ergin      |
| 2     | WG2. Hydrodynamic hull design for energy-efficient performance         | Prof Kostas Belibassakis | Mr Ivan Sulovsky |
| 3     | WG3. Operation of ship propulsion systems with alternative fuels       | Prof Peilin Zhou    | Dr Elias Yfantis     |
| 4     | WG4. Renewable energy contributions to ship energy efficiency          | Prof Jonas Ringsberg | Dr Caglar Karatug    |
| 5     | WG5. Onboard decision support systems for energy-efficient ship operation | Prof Nikola Vladimir | Prf. Haitong Xu   |



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

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
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
