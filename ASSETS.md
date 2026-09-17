# Assets

## Wallpapers

The first three wallpapers were replaced using the built-in OpenAI image generation tool, guided by DESIGN.md. These are painterly interpretations of Goethe’s ideas. Exact prompts are recorded in GENERATION.md.

| File | Idea |
|---|---|
| `01-farbenkreis.png` | Six pigment veils around a dark center, reflected in water |
| `02-truebe.png` | Warm light and cool darkness seen through atmospheric haze |
| `03-kanten.png` | Cool and warm fringes at the boundary between light and dark stone |
| `04-grenze.png` | Existing composition, preserved byte-for-byte |

The new PNGs are 1672×941, the native resolution returned by the generator. They are not native 4K images. Inspect cropping on the intended display.

`tools/wallpapers.py` remains a legacy generator for the original procedural images. Running it against `backgrounds/` overwrites the new artwork; use a separate scratch output directory instead. `tools/wallpaper-colors.json` contains the original illustrative color samples, not measurements of the new PNGs.

## Preview

`preview.png` is a rendered mock of an Omarchy desktop, not a screenshot, and still shows the original wallpaper. A current desktop screenshot is still needed before listing the theme.

## License

The repository’s MIT license remains in place. The replacement images are AI-generated; the previous claim that all wallpapers were drawn solely with Pillow no longer applies. The provenance of `04-grenze.png` is unchanged by this replacement.
