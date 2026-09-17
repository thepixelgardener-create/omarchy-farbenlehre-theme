#!/usr/bin/env python3
"""Farbenlehre palette checker.

Checks a colors.toml against the color pairs Omarchy actually draws
(terminal, editor, shell surfaces, btop) and against the rules the theme
takes from Goethe's Theory of Colours. Standard library only.

    python3 tools/check.py colors.toml [--wallpapers backgrounds/palette.json]

Contrast uses the WCAG 2 formula. Colorblind views use the Machado 2009
matrices at full severity. Color distance is Euclidean distance in OKLab.
Mixing follows Omarchy's template helper: a straight blend in sRGB.
"""
import itertools, json, math, sys, tomllib

# ---------------------------------------------------------------- color math
def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lin(h):
    return [to_lin(c) for c in hex_rgb(h)]

def luminance(h):
    r, g, b = lin(h)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    x, y = sorted((luminance(a), luminance(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)

def mix(a, b, t):
    """Omarchy's {{ mix a b t }}: straight sRGB blend, t = share of b."""
    A, B = hex_rgb(a), hex_rgb(b)
    return "#" + "".join(f"{round((x * (1 - t) + y * t) * 255):02x}" for x, y in zip(A, B))

def oklab_from_lin(v):
    r, g, b = (max(0.0, min(1.0, x)) for x in v)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (x ** (1 / 3) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)

SIM = {
    "deuteranopia": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "protanopia": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
}

def simulate(v, kind):
    if kind is None:
        return v
    M = SIM[kind]
    return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]

def distance(a, b, kind=None):
    A = oklab_from_lin(simulate(lin(a), kind))
    B = oklab_from_lin(simulate(lin(b), kind))
    return math.dist(A, B)

def oklch_hue(h):
    L, a, b = oklab_from_lin(lin(h))
    return math.degrees(math.atan2(b, a)) % 360, math.hypot(a, b)

def hue_gap(a, b):
    d = abs(oklch_hue(a)[0] - oklch_hue(b)[0]) % 360
    return min(d, 360 - d)

# ---------------------------------------------------------------- checks
SIX = ["red", "green", "yellow", "blue", "magenta", "cyan"]

def run(p, wallpaper_colors=()):
    bg, fg = p["background"], p["foreground"]
    rows = []

    def ratio(group, label, a, b, target):
        rows.append((group, label, contrast(a, b), target, "ratio"))

    def dist(group, label, value, target):
        rows.append((group, label, value, target, "dist"))

    # text
    ratio("Text", "foreground on background", fg, bg, 7)
    ratio("Text", "light_foreground on background (btop graph text)", p["light_foreground"], bg, 7)
    ratio("Text", "dark_foreground on background (line numbers)", p["dark_foreground"], bg, 4.5)
    ratio("Text", "muted on background (comments, dividers)", p["muted"], bg, 3)
    ratio("Text", "bright_foreground on selection (selected text)", p["bright_foreground"], p["selection"], 4.5)

    # terminal
    for c in SIX + ["bright_" + c for c in SIX]:
        ratio("Terminal", f"{c} on background", p[c], bg, 4.5)
    ratio("Terminal", "background on yellow (search match)", bg, p["yellow"], 4.5)
    ratio("Terminal", "background on red (focused match)", bg, p["red"], 4.5)

    # accent as text and border
    ratio("Accent", "accent on background (btop highlights)", p["accent"], bg, 4.5)
    ratio("Accent", "accent on selection (btop selected row)", p["accent"], p["selection"], 4.5)
    ratio("Accent", "accent on menu/launcher selected row (8% foreground)", p["accent"], mix(bg, fg, 0.08), 4.5)

    # shell controls (fills are foreground over background)
    ratio("Shell", "foreground on selected control (18% fill)", fg, mix(bg, fg, 0.18), 4.5)
    ratio("Shell", "foreground on pressed control (22% fill)", fg, mix(bg, fg, 0.22), 4.5)
    ratio("Shell", "red on background (polkit and lock errors)", p["red"], bg, 4.5)
    for name, w in wallpaper_colors:
        ratio("Shell", f"lock text on 80% background over wallpaper {name}", fg, mix(w, bg, 0.80), 4.5)
        ratio("Shell", f"launcher text on 95% background over wallpaper {name}", fg, mix(w, bg, 0.95), 4.5)

    # colorblind
    for kind in ("deuteranopia", "protanopia"):
        dist("Colorblind", f"red vs green, {kind}", distance(p["red"], p["green"], kind), 0.10)
    d, pair = min((distance(p[a], p[b]), f"{a}/{b}") for a, b in itertools.combinations(SIX, 2))
    dist("Colorblind", f"closest signal pair, normal vision ({pair})", d, 0.07)

    # Goethe's rules (hue relations, measured in OKLCH)
    rules = []
    g_hue, g_chroma = oklch_hue(p["background"])
    t_hue, _ = oklch_hue(p["foreground"])
    rules.append(("Minus side: the ground leans blue, darkness seen through haze", g_hue, 225, 285))
    rules.append(("Plus side: the text leans yellow, light seen through haze", t_hue, 50, 115))
    rules.append(("Demanded color: accent vs selection hue gap", hue_gap(p["accent"], p["selection"]), 140, 220))
    sat = max(oklch_hue(p[k])[1] for k in ("background", "dark_background", "darker_background", "lighter_background", "muted", "foreground"))
    low = min(oklch_hue(p[k])[1] for k in SIX + ["accent"])
    rules.append(("Neutral ground: most saturated neutral vs least saturated signal (chroma)", sat, None, low))
    return rows, rules

def fmt(v, kind):
    return f"{v:5.2f}:1" if kind == "ratio" else f"{v:6.3f} "

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    path = args[0]
    with open(path, "rb") as f:
        p = {k: v for k, v in tomllib.load(f).items() if not (isinstance(v, str) and " " in v)}
    walls = ()
    if "--wallpapers" in args:
        with open(args[args.index("--wallpapers") + 1]) as f:
            walls = tuple(json.load(f).items())
    rows, rules = run(p, walls)
    failed = 0
    group = None
    print(f"{path}  (mode = {p.get('mode', '?')})")
    for g, label, value, target, kind in rows:
        if g != group:
            print(f"\n{g}"); group = g
        ok = value >= target
        failed += not ok
        print(f"  {'pass' if ok else 'FAIL'}  {fmt(value, kind)}  min {target:<5}  {label}")
    print("\nGoethe's rules")
    for label, value, lo, hi in rules:
        if lo is None:
            ok = value < hi
            print(f"  {'pass' if ok else 'FAIL'}  {value:6.3f}   below {hi:.3f}  {label}")
        else:
            ok = lo <= value <= hi
            print(f"  {'pass' if ok else 'FAIL'}  {value:6.1f}°  {lo}-{hi}°  {label}")
        failed += not ok
    total = len(rows) + len(rules)
    print(f"\n{total - failed}/{total} checks pass")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
