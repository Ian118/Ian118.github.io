from numpy.random import normal, uniform
from numpy import clip, maximum

n = 500
size = maximum(normal(1.5, 0.1, n), 0)
x = uniform(0, 1920, n)
y = uniform(0, 1080, n)
value = clip(normal(255, 5, n), 0, 255).astype(int)
stars = zip(x, y, size, value)

n = 32
size = maximum(normal(40, 10, n), 0)
x = uniform(-1920, 1920, n)
y = uniform(0, 1080, n)
twinkle = zip(x, y, size)


svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="15" />
  </filter>
  {"\n".join([f'<circle r="{size}" cx="{x}" cy="{y}" fill="#{v:02x}{v:02x}{v:02x}"/>' for x, y, size, v in stars])}
  <g id="twinkle" fill="#00000" filter="url(#blur)">
    <animateMotion dur="120s" repeatCount="indefinite" path="M0,0 L1920,0 z" />
    {"\n".join([f'<circle r="{size}" cx="{x}" cy="{y}"/>' for x, y, size in twinkle])}
  </g>
</svg>
"""
with open("stars.svg", "w") as file:
    file.write(svg)
