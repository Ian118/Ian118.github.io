const content = document.querySelectorAll("body > :not(#lightspeed)");
for (const e of content) e.hidden = true;
document.body.style.margin = 0;
document.body.style.padding = 0;
document.body.style.overflow = 'hidden';
const ls = document.createElement('canvas');
ls.style.position = 'absolute';
document.body.appendChild(ls);

const sleep = ms => new Promise(r => setTimeout(r, ms));
const ctx = ls.getContext('2d');
const n = 3000;
const starRatio = 500;
const speed = 5;

const [w, h] = [window.innerWidth, window.innerHeight];
const [x, y, z] = [w / 2, h / 2, (w + h) / 8];
const starColorRatio = 1 / z;

const stars = Array.from({ length: n }, () => {
  const actx = Math.random() * w - x;
  const acty = Math.random() * h - y;
  const z0 = Math.random() * z + 200;
  return {
    x: actx * z0 / starRatio,
    y: acty * z0 / starRatio,
    z0,
    z1: z0 - 1,
    get lineWidth() { return (1 - starColorRatio * this.z0) * 2; },
    get x0() { return this.x / this.z0 * starRatio; },
    get y0() { return this.y / this.z0 * starRatio; },
    get x1() { return this.x / this.z1 * starRatio; },
    get y1() { return this.y / this.z1 * starRatio; },
  };
});

ls.width = w;
ls.height = h;

ctx.fillStyle = "black";
ctx.strokeStyle = 'white';

function draw() {
  ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  for (const star of stars) {
    ctx.lineWidth = star.lw;
    ctx.beginPath();
    ctx.moveTo(x + star.x0, y + star.y0);
    ctx.lineTo(x + star.x1, y + star.y1);
    ctx.stroke();
    ctx.closePath();
  }
}

draw();
await sleep(200);

for (let i = 0; i < 52; i++) {
  for (const star of stars) star.z1 -= 2.5;
  draw();
  await sleep(1);
}
await sleep(500);
for (let i = 0; i < 13; i++) {
  for (const star of stars) star.z1 += 10;
  draw();
  await sleep(1);
}
ls.remove();
for (const e of content) e.hidden = false;