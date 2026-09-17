# Farbenlehre

A dark theme for [Omarchy](https://omarchy.org), built on Goethe's *Theory of Colours* (1810).

![Farbenlehre: Bash, palette editor, btop and Omarchy menu](preview.png?v=20260917-desktop-apps)

Real Omarchy desktop capture with Bash, a palette editor, btop and the Omarchy menu. The Farbenkreis wallpaper remains visible behind the applications.

```sh
omarchy theme install https://github.com/thepixelgardener-create/omarchy-farbenlehre-theme
```

## What makes it different

**Every terminal color is readable.** All twelve signal colors reach at least 5:1 against the background.

**Red and green stay apart for colorblind users.** Green is much brighter than red, so the two never rely on hue alone, and the result is checked with a simulation of red-green color blindness.

**Every color follows Goethe.** Darkness seen through haze turns blue, so the ground is a blue-black. Light seen through haze turns yellow, so the text is warm. Yellow sits on Goethe's plus side, so it is the accent; the eye demands violet after yellow, so the selection is violet. The active window border rises from yellow to red, the intensification Goethe placed at the top of his color circle. [DESIGN.md](DESIGN.md) lists every rule and every measured value.

## Wallpapers

Four wallpapers interpreting Goethe’s ideas:

1. **Farbenkreis:** Six pigment veils forming a luminous circle above dark water.
2. **Trübe:** warm and cold light emerging through a misty landscape.
3. **Kanten:** warm and cold fringes at a luminous opening between dark stone planes.
4. **Grenze:** the existing composition, preserved unchanged.

## Check it yourself

```sh
python3 tools/check.py colors.toml
```

Requires Python 3.11 or newer, with no additional packages. Checks palette contrast, red–green separation, and text contrast over wallpaper overlays using black and white as conservative bounds. The overlay checks cover any wallpaper under the checker’s assumed 80% lock-screen and 95% launcher background opacity.

## Credits and license

The ideas are Goethe's, from *Zur Farbenlehre* (1810), which is in the public domain. Everything in this repository, wallpapers included, is original work under the MIT license.
