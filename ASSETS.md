# Assets

## Wallpapers

The three wallpapers are AI-generated painterly interpretations of Goethe’s ideas, made with the built-in OpenAI image generation tool and guided by DESIGN.md. Their exact prompts are recorded in GENERATION.md.

| File | Idea |
|---|---|
| `01-farbenkreis.png` | Six pigment veils around a dark center, reflected in water |
| `02-truebe.png` | Warm light and cool darkness seen through atmospheric haze |
| `03-kanten.png` | Cool and warm fringes at the boundary between light and dark stone |

All three PNGs are 1672×941, the native resolution returned by the generator. They are not native 4K images, and a 4K screen upscales them about 2.3×. Inspect cropping on the intended display.

The checker uses black and white bounds instead of samples from the old artwork, so its overlay contrast checks apply to all three wallpapers at the modeled opacity values.

## Illustration

`docs/grenze.png` sets Newton’s prism against Goethe’s world of perceived color in a painterly landscape. It was generated in ChatGPT before the wallpapers and its prompt was not kept. It shipped in `backgrounds/` until it was moved here: unlike the wallpapers it carries lettering near all four edges, which a 21:9 crop cuts by 12% top and bottom and a 16:10 crop by 5% per side, and which competes with the lock screen and launcher text drawn over a wallpaper.

## Preview

`preview.png` is a real 3840×2160 Omarchy desktop screenshot showing Bash, Neovim displaying colors.toml, btop CPU/memory graphs, the open Omarchy menu, the live bar and a smaller exposed area of the replacement Farbenkreis wallpaper. The demonstration editor uses an isolated configuration with colors from the theme; it does not represent the default Neovim setup. It was captured on 2026-09-17. The wallpaper is scaled by the desktop from its native 1672×941 image; the screenshot does not make the source artwork native 4K.

## License

The repository’s MIT license remains in place. The three wallpapers and the Grenze illustration are AI-generated; the earlier claim that every wallpaper was drawn with Pillow no longer applies to any of them. The palette, `tools/check.py` and the written notes are original work.
