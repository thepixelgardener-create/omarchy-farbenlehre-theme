#!/usr/bin/env python3
"""Draw the Farbenlehre wallpapers.

    python3 tools/wallpapers.py backgrounds/

Needs Pillow. Every image is drawn from code in this file. The ideas come
from Goethe's Theory of Colours (1810): his six-part color circle, colors
seen through a turbid medium, and the colored edges a prism shows where
light meets darkness. The compositions themselves are original.
"""
import math, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

W, H = 3840, 2160
SS = 2
GROUND = "#0f141c"
LIGHT = "#fefcf7"

# Goethe's six colors, clockwise from the summit.
CIRCLE = [
    ("purpur", "#c2305c"), ("gelbrot", "#e0622b"), ("gelb", "#f0c23a"),
    ("gruen", "#3a9a5c"), ("blau", "#2f5aa8"), ("blaurot", "#6e3d97"),
]
C = dict(CIRCLE)

def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

def lerp(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(rgb(a) if isinstance(a, str) else a, rgb(b) if isinstance(b, str) else b))

def s(*v):
    return [round(x * SS) for x in v]

def canvas():
    img = Image.new("RGB", (W * SS, H * SS), GROUND)
    return img, ImageDraw.Draw(img)

def finish(img, path):
    img.resize((W, H), Image.LANCZOS).save(path, optimize=True)
    return path

def farbenkreis():
    """The six-part circle, with thin lines joining each color to the one the eye demands."""
    img, d = canvas()
    cx, cy, R, width = 2340, 1080, 600, 150
    for i, (_, color) in enumerate(CIRCLE):
        start = -90 - 30 + i * 60 + 1.5
        d.arc(s(cx - R, cy - R, cx + R, cy + R), start, start + 57, fill=color, width=width * SS)
    inner = R - width - 40
    for i in range(3):
        a = math.radians(-90 + i * 60)
        x, y = inner * math.cos(a), inner * math.sin(a)
        d.line(s(cx + x, cy + y, cx - x, cy - y), fill=lerp(GROUND, LIGHT, 0.35), width=4 * SS)
    d.ellipse(s(cx - 26, cy - 26, cx + 26, cy + 26), fill=LIGHT)
    d.rectangle(s(620, cy - 5, 1480, cy + 5), fill=lerp(GROUND, LIGHT, 0.35))
    return img

def truebe():
    """Turbid medium: light seen through haze turns yellow, then red;
    darkness seen through lit haze turns blue."""
    img = Image.new("RGB", (W * SS, H * SS), GROUND)
    glow = Image.new("RGB", img.size, (0, 0, 0))
    g = ImageDraw.Draw(glow)
    # light behind haze
    cx, cy = 2560, 1080
    stops = [(0.0, LIGHT), (0.12, "#fff1b8"), (0.3, C["gelb"]), (0.55, C["gelbrot"]), (0.8, C["purpur"]), (1.0, GROUND)]
    Rmax = 700
    for r in range(Rmax, 0, -3):
        t = r / Rmax
        for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
            if t0 <= t <= t1:
                col = lerp(c0, c1, (t - t0) / (t1 - t0)); break
        g.ellipse(s(cx - r, cy - r, cx + r, cy + r), fill=col)
    img = Image.composite(glow, img, glow.convert("L").point(lambda v: 255 if v > 0 else 0))
    # darkness behind lit haze
    haze = Image.new("L", img.size, 0)
    h = ImageDraw.Draw(haze)
    h.ellipse(s(560, 660, 1600, 1500), fill=150)
    haze = haze.filter(ImageFilter.GaussianBlur(120 * SS))
    blue = Image.new("RGB", img.size, "#4a78c4")
    img = Image.composite(blue, img, haze)
    return img

def kanten():
    """Edge spectra: a bright band on darkness, fringed blue and violet on one
    edge and yellow and red on the other, as Goethe saw through the prism."""
    img, d = canvas()
    x0, x1, y0, y1 = 760, 3080, 1000, 1160
    d.rectangle(s(x0, y0, x1, y1), fill=LIGHT)
    fringe = Image.new("RGB", img.size, GROUND)
    mask = Image.new("L", img.size, 0)
    f, m = ImageDraw.Draw(fringe), ImageDraw.Draw(mask)
    for band, color, top, bottom in [
        ("blau", C["blau"], y0 - 110, y0 + 60), ("blaurot", C["blaurot"], y0 - 230, y0 - 110),
        ("gelb", C["gelb"], y1 - 60, y1 + 110), ("gelbrot", C["gelbrot"], y1 + 110, y1 + 230),
    ]:
        f.rectangle(s(x0, top, x1, bottom), fill=color)
        m.rectangle(s(x0, top, x1, bottom), fill=255)
    fringe = fringe.filter(ImageFilter.GaussianBlur(26 * SS))
    mask = mask.filter(ImageFilter.GaussianBlur(26 * SS))
    img = Image.composite(fringe, img, mask)
    ImageDraw.Draw(img).rectangle(s(x0, y0, x1, y1), fill=LIGHT)
    return img

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for i, (name, fn) in enumerate([("farbenkreis", farbenkreis), ("truebe", truebe), ("kanten", kanten)], 1):
        print(finish(fn(), out / f"{i:02d}-{name}.png"))

if __name__ == "__main__":
    main()
