# Assets

## Wallpapers

All four wallpapers are AI-generated painterly interpretations of Goethe’s ideas. `01`–`03` were made with the built-in OpenAI image generation tool, guided by DESIGN.md; their exact prompts are recorded in GENERATION.md. `04-grenze.png` was made earlier, in ChatGPT, and its prompt was not kept.

| File | Idea |
|---|---|
| `01-farbenkreis.png` | Six pigment veils around a dark center, reflected in water |
| `02-truebe.png` | Warm light and cool darkness seen through atmospheric haze |
| `03-kanten.png` | Cool and warm fringes at the boundary between light and dark stone |
| `04-grenze.png` | Newton’s prism and Goethe’s world of perceived color in a painterly landscape |

All four PNGs are 1672×941, the native resolution returned by the generator. They are not native 4K images, and a 4K screen upscales them about 2.3×. Inspect cropping on the intended display: `04-grenze.png` carries text near all four edges and loses parts of it on a 21:9 or 16:10 crop.

The checker uses black and white bounds instead of samples from the old artwork, so its overlay contrast checks apply to all four wallpapers at the modeled opacity values.

## Preview

`preview.png` is a real 3840×2160 Omarchy desktop screenshot showing Bash, Neovim displaying colors.toml, btop CPU/memory graphs, the open Omarchy menu, the live bar and a smaller exposed area of the replacement Farbenkreis wallpaper. The demonstration editor uses an isolated configuration with colors from the theme; it does not represent the default Neovim setup. It was captured on 2026-09-17. The wallpaper is scaled by the desktop from its native 1672×941 image; the screenshot does not make the source artwork native 4K.

## License

The repository’s MIT license remains in place. All four wallpapers are AI-generated; the earlier claim that every wallpaper was drawn with Pillow no longer applies to any of them. The palette, `tools/check.py` and the written notes are original work.
