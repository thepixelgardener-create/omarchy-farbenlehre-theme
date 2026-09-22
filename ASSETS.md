# Assets

## Wallpapers

The four wallpapers are AI-generated painterly interpretations of Goethe’s ideas, guided by DESIGN.md. The first three were made with the built-in OpenAI image generation tool; `04-daemmerung.png` was made later in ChatGPT from a much shorter prompt. All four prompts are recorded in GENERATION.md.

| File | Idea |
|---|---|
| `01-farbenkreis.png` | Six pigment veils circling a dark center over moonlit water, watched from the ruins by a seated figure |
| `02-truebe.png` | Warm light and cool darkness seen through atmospheric haze |
| `03-kanten.png` | Cool and warm fringes at the boundary between light and dark stone |
| `04-daemmerung.png` | Goethe’s study at dusk: warm candlelight on the desk against the last blue twilight in the window, watched by his bust |

All four PNGs are 1672×941, the native resolution returned by the generator. They are not native 4K images, and a 4K screen upscales them about 2.3×. Inspect cropping on the intended display.

`04-daemmerung.png` keeps its middle a dark wall and curtain, so the lock screen and launcher text never land on the candle or the window. A 21:9 crop trims the top of the window and the rug. A 16:10 crop cuts through the bust of Goethe at the right edge, and a 3:2 crop loses it entirely; the candle, desk and window survive every crop.

The overlay contrast checks use black and white bounds instead of samples from the old artwork, so they apply to all four wallpapers at the modeled opacity values.

## Preview

`preview.png` is a real 3840×2160 Omarchy desktop screenshot showing Bash, Neovim on `colors.toml`, btop, the open Omarchy menu, the live bar and an exposed area of the current Farbenkreis wallpaper. Neovim is an ordinary Omarchy LazyVim setup rendering the theme's generated colors, not a mock. btop runs with its process list switched off, so the capture does not publish a list of what was running. Its CPU graphs show load generated during the capture, so the panels are not flat. Captured on 2026-09-17. The wallpaper is scaled up by the desktop from its native 1672×941 image; the screenshot does not make the source artwork native 4K.

## License

The repository’s MIT license remains in place. The four wallpapers are AI-generated; the earlier claim that every wallpaper was drawn with Pillow no longer applies to any of them. The palette and the written notes are original work.
