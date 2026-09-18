# Farbenlehre design notes

Farbenlehre is a dark Omarchy theme built on Johann Wolfgang von Goethe's *Zur Farbenlehre* (Theory of Colours), published in 1810. Goethe died in 1832; the book, his color circle and his experiments have long been in the public domain. The theme takes his ideas, not any particular edition, translation or image.

This file is the contract for the palette. If a value changes, the rule it follows should still hold, and the values below should be measured again.

## Goals

1. Every terminal color is readable as text: at least 4.5:1 against the background.
2. Red and green stay distinguishable for people with red-green color blindness.
3. Every color has a reason that can be traced back to Goethe.
4. Ship only what Omarchy can't generate well itself, so new Omarchy versions keep working.

## The rules

**Light and darkness.** For Goethe, colors are not pieces of white light but what happens where light meets darkness. The theme starts from those two poles: a dark ground and light text, with every color placed between them.

**The turbid medium.** Light seen through a haze turns yellow, and then orange and red as the haze thickens, like the setting sun. Darkness seen through a lit haze turns blue, like the sky. So the ground is a blue-black, darkness seen through haze, and the text is a warm off-white, light seen through haze.

**Plus and minus.** Goethe sorted the colors into two sides. Yellow belongs to the plus side with light, warmth, nearness and action; blue belongs to the minus side with shadow, cold, distance and rest. The accent is yellow, because focus should come forward. Surfaces, muted text and inactive borders lean blue, because they should recede.

**Demanded colors.** Goethe noticed that after staring at a color the eye produces its opposite on his circle: yellow demands violet, orange demands blue, purple demands green. The selection is violet, the color the yellow accent demands.

**Steigerung.** Yellow and blue each intensify toward red, and meet in purple at the summit of Goethe's circle. The active window border runs from the yellow accent to the red, so the one moving element in the desktop shows that intensification.

**The six colors.** The signal colors are Goethe's six: purple-red (terminal red), yellow-red (orange), yellow, green, blue and blue-red (magenta). Cyan is the blue-green where Goethe's green, the mixture of yellow and blue, turns toward blue. Brown is a darkened yellow-red.

**Opposites need a second difference.** Purple-red and green face each other on Goethe's circle, and red-green colorblind eyes see little of that hue difference. The theme adds a brightness difference on purpose: green is much brighter than red.

**Neutral ground.** Surfaces and text stay nearly grey (OKLCH chroma of 0.022 or less). Color is kept for the accent and the signals, where it means something.

## Goethe's symbolic words

On his 1809 color circle Goethe wrote a quality beside each color. They don't drive any value in the palette, but they fit the roles surprisingly well, so they are listed here for fun:

| Color | Goethe's word | Meaning | Role in the theme |
|---|---|---|---|
| Red | schön | beautiful | Errors, the one color you can't ignore |
| Orange | edel | noble | Numbers and constants |
| Yellow | gut | good | The accent and warnings |
| Green | nützlich | useful | Success and additions |
| Blue | gemein | common, in the old sense of ordinary | Information and links |
| Violet | unnötig | unnecessary | Selection, used only when you ask for it |

## Palette

| Key | Role | Value |
|---|---|---|
| `background` | Main surface, darkness seen through haze | `#0f141c` |
| `dark_background` | Side panels, status lines | `#0a0e15` |
| `darker_background` | Deepest surface | `#05080d` |
| `lighter_background` | Cursor line, cards | `#191e28` |
| `foreground` | Text, light seen through haze | `#eae6dd` |
| `light_foreground` | Secondary text | `#f3f0e9` |
| `dark_foreground` | Dim text, line numbers | `#b0aca3` |
| `bright_foreground` | Cursor, selected text | `#fefcf7` |
| `muted` | Comments, dividers, inactive borders | `#6f7683` |
| `accent` | Yellow: focus, highlights | `#e4c124` |
| `selection` | Violet: the color yellow demands | `#3b2a4d` |
| `red` | Purple-red: errors | `#df576c` |
| `orange` | Yellow-red: numbers | `#e3793d` |
| `yellow` | Yellow: warnings | `#d8b82c` |
| `green` | Green: success | `#6ecb7e` |
| `cyan` | Blue-green | `#3badb2` |
| `blue` | Blue: information | `#578cd9` |
| `magenta` | Blue-red | `#ad76c6` |
| `brown` | Darkened yellow-red | `#a27e62` |

The bright variants keep the same hues and add brightness. `hyprland_active_border` is a gradient from the accent to the red at 45°; `hyprland_inactive_border` is the muted grey.

## Measured results

The palette is held to 38 checks: palette contrast, red–green separation, and wallpaper overlay contrast at the modeled 80% lock-screen and 95% launcher background opacity, with conservative overlay bounds. Black and white bound every sRGB wallpaper pixel, and foreground luminance exceeds the brightest possible overlay. Under the modeled 80% and 95% background opacity, white therefore gives the lowest text contrast. These checks do not inspect composition or cropping.

| Check | Result | Target |
|---|---|---|
| Text on background | 14.8:1 | 7:1 |
| Weakest terminal color | 5.03:1 (red) | 4.5:1 |
| Muted on background | 4.04:1 | 3:1 |
| Accent in menu and launcher selection | 8.76:1 | 4.5:1 |
| Selected text | 12.6:1 | 4.5:1 |
| Lock screen text, white wallpaper bound | 7.99:1 | 4.5:1 |
| Red vs green, deuteranopia | 0.117 | 0.10 |
| Red vs green, protanopia | 0.250 | 0.10 |
| Closest signal pair (blue/magenta) | 0.124 | 0.07 |

The checks follow the colors Omarchy's own templates draw: terminal ANSI colors and search highlights, the editor cursor line and selection, btop highlights and the selected process row, shell controls, menu and launcher selection, polkit and lock errors, and lock and launcher text over the wallpapers. Contrast uses WCAG 2; colorblind views use the Machado 2009 simulation at full severity; distances are measured in OKLab. The two distance thresholds are working choices from comparing about 80 existing Omarchy themes, not a standard.

## Known trade-offs

- The accent and the warning yellow are nearly the same color. Yellow is the plus side and the loudest color on a dark ground, so it leads.
- The active-border gradient also reaches the shell's popups, notifications, menus and lock screen, because Omarchy uses the Hyprland border for them. That is intended, but it makes red appear in borders that are not errors.
- Goethe described colors on a painter's and observer's terms, not in any color space. The hues here are a translation into OKLCH.

## What the theme ships, and what it leaves to Omarchy

Shipped: `colors.toml`, `icons.theme`, three wallpapers, `preview.png` and these notes.

Left to Omarchy's templates on purpose: the terminal configs, Neovim, VS Code, btop, Chromium, the shell and Hyprland. Omarchy generates them from `colors.toml`, and the checks above cover the colors those templates use. Omarchy also drops `.lua` files, terminal configs and `vscode.json` from themes installed through git, so shipping them would not work anyway.

## Release checklist

1. Measure the palette again: contrast, red–green separation and the wallpaper overlay bounds still meet the targets above.
2. Inspect the wallpaper PNGs and their provenance in ASSETS.md.
3. Push, then install from the clean URL: `omarchy theme install <repo-url>`.
4. Run `omarchy dev theme-preview farbenlehre` and look at the ramp and the selected-text sample.
5. Look at a terminal with `git diff`, Neovim, btop, the Omarchy menu, a notification and the lock screen.
6. Keep `preview.png` current with a real desktop screenshot. The current capture shows Bash, a palette editor, btop, the Omarchy menu and bar, with the replacement Farbenkreis wallpaper behind them.
7. Check each wallpaper on the widest and the tallest screen you have.
