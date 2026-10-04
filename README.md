# Farbenlehre

A dark theme for [Omarchy](https://omarchy.org), inspired by Goethe's *Theory of Colours* (1810). Blue-black surfaces, warm text and a yellow accent, paired with four painterly wallpapers exploring light, darkness and color.

![Farbenlehre: Bash, Neovim, btop and the Omarchy menu](preview.png?v=20260917-regenerated)

*A real Omarchy desktop: Bash, Neovim, btop and the Omarchy menu over Farbenkreis. The screenshot is 4K; the original wallpaper is 1672 × 941.*

## Install

From the Omarchy menu: press **Super + Space**, then **Install → Style → Theme**, and paste the repository URL when it asks:

```
https://github.com/thepixelgardener-create/omarchy-farbenlehre-theme
```

Or straight from a terminal:

```sh
omarchy theme install https://github.com/thepixelgardener-create/omarchy-farbenlehre-theme
```

Omarchy installs and activates the theme, generating application colors from `colors.toml`. Choose a wallpaper with **Super + Ctrl + Space**.

## What makes it different

**Readable signal colors.** All twelve standard and bright terminal signal colors reach at least 5:1 contrast against the theme background.

**Red and green differ in brightness as well as hue.** Green is deliberately brighter than red. The palette was checked with simulations of protanopia and deuteranopia to assess their separation.

**A palette with a shared idea.** Goethe's observations of light and darkness through haze inspire the warm text and cool ground. Yellow marks focus, violet marks selection, and the active window border moves from yellow to red. [Read the design notes](DESIGN.md) for the reasoning behind each choice.

**Native Omarchy integration.** The theme supplies its palette, icon theme and artwork. Omarchy's templates generate the terminal, editor and shell configuration.

## Wallpapers

Click a preview to open the original image.

| Farbenkreis | Trübe |
| --- | --- |
| [![Farbenkreis: a circle of colored pigment over moonlit water](backgrounds/01-farbenkreis.png)](backgrounds/01-farbenkreis.png) | [![Trübe: warm and cool light across a misty landscape](backgrounds/02-truebe.png)](backgrounds/02-truebe.png) |
| Six pigment veils circling over moonlit water, watched from the ruins. | Warm light and cool darkness emerging through atmospheric haze. |

| Kanten | Dämmerung |
| --- | --- |
| [![Kanten: colored fringes along a luminous opening in dark stone](backgrounds/03-kanten.png)](backgrounds/03-kanten.png) | [![Dämmerung: warm candlelight and blue twilight in Goethe's study](backgrounds/04-daemmerung.png)](backgrounds/04-daemmerung.png) |
| Warm and cool fringes where light meets dark stone. | Goethe’s study at dusk, where warm candlelight meets the last blue twilight. |

### Resolution and displays

This edition preserves all four wallpapers at their original **1672 × 941** resolution, approximately 16:9. Omarchy scales them to fill the display; on a 3840 × 2160 screen, that means enlarging them about 2.3×. Ultrawide, 16:10 and portrait screens crop the composition differently.

A **4K variant is planned as a separate edition**. The wallpapers included here remain the original versions. [ASSETS.md](ASSETS.md) records their dimensions and provenance.

## Palette checks

The design notes record 38 checks covering palette contrast, simulated red–green separation, and wallpaper overlay contrast at modeled lock-screen and launcher opacity values.

| Measurement | Recorded result |
| --- | --- |
| Main text on the background | 14.8:1 |
| Weakest terminal signal color | 5.03:1 |
| Selected text | 12.6:1 |
| Muted text on the background | 4.04:1 |

[DESIGN.md](DESIGN.md) documents the targets, assumptions and known trade-offs. The overlay measurements use conservative black and white bounds; they do not assess wallpaper composition or cropping.

## Credits and license

The ideas come from Goethe's *Zur Farbenlehre* (1810), a public-domain work. The four wallpapers are AI-generated. [ASSETS.md](ASSETS.md) records their provenance, and [GENERATION.md](GENERATION.md) preserves their prompts. The palette and written notes are original work.

Released under the [MIT license](LICENSE).
