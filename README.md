# Farbenlehre

A dark theme for [Omarchy](https://omarchy.org), built on Goethe's *Theory of Colours* (1810).

![Farbenlehre: Bash, Neovim, btop and the Omarchy menu](preview.png?v=20260917-regenerated)

Real Omarchy desktop capture with Bash, Neovim on `colors.toml`, btop and the Omarchy menu, over the Farbenkreis wallpaper.

```sh
omarchy theme install https://github.com/thepixelgardener-create/omarchy-farbenlehre-theme
```

## What makes it different

**Every terminal color is readable.** All twelve signal colors reach at least 5:1 against the background.

**Red and green stay apart for colorblind users.** Green is much brighter than red, so the two never rely on hue alone, and the result is checked with a simulation of red-green color blindness.

**Every color follows Goethe.** Darkness seen through haze turns blue, so the ground is a blue-black. Light seen through haze turns yellow, so the text is warm. Yellow sits on Goethe's plus side, so it is the accent; the eye demands violet after yellow, so the selection is violet. The active window border rises from yellow to red, the intensification Goethe placed at the top of his color circle. [DESIGN.md](DESIGN.md) lists every rule and every measured value.

## Wallpapers

Three wallpapers interpreting Goethe’s ideas:

1. **Farbenkreis:** Six pigment veils circling over moonlit water, watched from the ruins.
2. **Trübe:** warm and cold light emerging through a misty landscape.
3. **Kanten:** warm and cold fringes at a luminous opening between dark stone planes.

A fourth image, [Grenze](docs/grenze.png), sets Newton’s prism against Goethe’s world of perceived color. It carries lettering at its edges and loses some of it on a wide or tall crop, so it lives in `docs/` as an illustration instead of shipping as a wallpaper.

## Measured, not eyeballed

Every color pair Omarchy actually draws was measured: terminal and editor contrast, red–green separation under a simulation of red-green color blindness, and lock screen and launcher text against the brightest and darkest wallpaper pixel a screen can show. That is 38 checks in all. [DESIGN.md](DESIGN.md) explains every one and lists the measured values.

## Credits and license

The ideas are Goethe's, from *Zur Farbenlehre* (1810), which is in the public domain. The four wallpapers are AI-generated; [ASSETS.md](ASSETS.md) records how each one was made, and [GENERATION.md](GENERATION.md) holds the prompts for the three that have them. The palette and the written notes are original work. Everything in this repository is released under the MIT license.
