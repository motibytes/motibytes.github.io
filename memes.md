---
layout: lightboxlayout
title: memes
---
<!--
<ul class="something">
{% for image in page.images %}
  <li class="something">
    <a rel="something" class="something" href="/path/to/images/dir/{{ image }}" />
  </li>
{% endfor %}
</ul> -->
<!-- looks like this requires 'lightbox' -->
{% for file in site.memes %}
  {% assign pageurl = page.url | replace: 'index.html', '' %}
  {% if file.path contains pageurl %}
    {% if file.extname == '.jpg' or file.extname == '.jpeg' or file.extname == '.JPG' or file.extname == '.JPEG' %}
    <img src="{{ file.path }}" />
    {% endif %}
  {% endif %}
{% endfor %}
