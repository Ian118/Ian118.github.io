---
title: "Portfolio"
author_profile: true
permalink: /portfolio/
---

<style> .portfolio-image{ max-width:250px; max-height:250px; } </style>

{% assign grouped_members = site.portfolio | sort: "year" | reverse | group_by: "year" %}

{% for group in grouped_members %}
<h2>{{ group.name }}</h2>
{% for item in group.items %}
![](/images/{{ item.image }}){: .portfolio-image}  
[{{ item.title }}]({{ item.url }})  
{{ item.excerpt }}
{% endfor %}
{% endfor %}