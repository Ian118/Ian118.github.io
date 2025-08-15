from numpy.random import normal, uniform
from numpy import clip, maximum

w = 1920
h = 1080

n = 500
size = maximum(normal(1.5, 0.1, n), 0)
x = uniform(0, w, n)
y = uniform(0, h, n)
value = clip(normal(255, 5, n), 0, 255).astype(int)
stars = zip(x, y, size, value)

stars_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  {"\n".join([f'<circle r="{size}" cx="{x}" cy="{y}" fill="#{v:02x}{v:02x}{v:02x}"/>' for x, y, size, v in stars])}
</svg>
"""

with open("stars.svg", "w") as file:
  file.write(stars_svg)

n = 20
blur = 15
size = maximum(normal(40, 10, n), 0)
x = uniform(0, w, n)
y = uniform(0, h, n)
twinkle = zip(x, y, size)

twinkle_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="{blur}" />
  </filter>
  <g fill="#00000" filter="url(#blur)">
    {"\n".join([f'<circle r="{r}" cx="{x}" cy="{y}"/>' for x, y, r in twinkle if 0 < x-r-blur and x+r+blur < w and 0 < y-r-blur and y+r+blur < h])}
  </g>
</svg>
"""

with open("twinkling.svg", "w") as file:
  file.write(twinkle_svg)
