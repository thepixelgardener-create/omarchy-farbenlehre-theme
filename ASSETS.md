# Assets

## Wallpapers

The six wallpapers are AI-generated painterly interpretations of Goethe’s ideas, guided by DESIGN.md. The first three were made with the built-in OpenAI image generation tool; `04-daemmerung.webp` was made later in ChatGPT from a much shorter prompt, `05-winterzug.webp` from a prompt that follows Goethe's own drawing of the Brocken, and `06-werdende.webp` from a long prompt of its own. All six prompts are recorded in GENERATION.md.

| File | Idea |
|---|---|
| `01-farbenkreis.webp` | Six pigment veils circling a dark center over moonlit water, watched from the ruins by a seated figure |
| `02-truebe.webp` | Warm light and cool darkness seen through atmospheric haze |
| `03-kanten.webp` | Cool and warm fringes at the boundary between light and dark stone |
| `04-daemmerung.webp` | Goethe’s study at dusk: warm candlelight on the desk against the last blue twilight in the window, watched by his bust |
| `05-winterzug.webp` | The Brocken by moonlight after Goethe's sketch from his winter journey of 1777: snow gold where the light falls, lilac in shadow, under a stormy night sky |
| `06-werdende.webp` | Das Werdende, Goethe's becoming: an ambiguous organic form of hollow arches, membranes and filaments growing out of the dark, amber and gold at its edges, lavender and violet in its depths |
| `intros/04-daemmerung.mp4` | Dämmerung's intro: the candle flickers and the room brightens and dims with it |

All six wallpapers are 3840×2160 WebP files, lossy at quality 92 like the WebP wallpapers of the built-in Omarchy themes (about 4.1 MB for all six instead of 45 MB as PNG, with no visible difference). The generator returned them at 1672×941; they were enlarged 4× with Real-ESRGAN (`realesrgan-x4plus`), resized to 3840×2160 with Lanczos, and blended 65 % Real-ESRGAN with 35 % of a plain Lanczos enlargement of the original. The blend keeps Real-ESRGAN's sharper edges without its smoothed, plastic surfaces, and holds average brightness within 4 % of the original. The upscaled detail is synthesized, not recovered: fine texture at 4K is the upscaler's interpretation of the original. Inspect cropping on the intended display.

`intros/04-daemmerung.mp4` is a 7-second, 30 fps H.264 intro at 2560×1440, the size of the built-in themes' intros, generated procedurally from the 4K still rather than by a video model. The flame is warped in place to sway from its tip and stretch about the wick; the light around the candle and, more gently, across the whole room rises and falls with it in a warm tint, while the twilight seen through the window glass stays steady. The motion is built from noise that rises out of the still over the first second and settles back over the last two, so the first and last frames are the still itself and the intro hands over to it without a jump. Every frame keeps the still's composition, so the overlay notes below apply to it too.

`04-daemmerung.webp` keeps its middle a dark wall and curtain, so the lock screen and launcher text never land on the candle or the window. A 21:9 crop trims the top of the window and the rug. A 16:10 crop cuts through the bust of Goethe at the right edge, and a 3:2 crop loses it entirely; the candle, desk and window survive every crop.

`05-winterzug.webp` keeps the summit and the forest bands across the middle, with the brightest snow below them and the moon's glow at the upper-left edge. A 21:9 crop trims the clouds and the nearest snow; 16:10 and 3:2 crops narrow the glow at the left edge and lose it at 3:2, while the summit and forest bands survive every crop.

`06-werdende.webp` puts its brightest arch left of centre and its golden wave on the right, with dark ground along the bottom and dark sky above. Lock screen and launcher text in the middle can land on the lit arch; the overlay checks below cover that case. A 21:9 crop trims the top of the wave and the dark ground; 16:10 and 3:2 crops trim the outer edges of the form, and its central arch survives every crop.

The overlay contrast checks use black and white bounds instead of samples from the old artwork, so they apply to all six wallpapers at the modeled opacity values.

## Preview

`preview.webp` is a real 3840×2160 Omarchy desktop screenshot, saved as WebP at quality 90 (675 KB instead of 5 MB as PNG), showing Bash, Neovim on `colors.toml`, btop, the live bar and the middle of the 4K Farbenkreis wallpaper. Neovim is an ordinary Omarchy LazyVim setup rendering the theme's generated colors, not a mock. btop shows only its CPU, memory and disk panels, so the capture publishes neither a list of what was running nor a network address. Captured on 2026-10-22.

## License

The repository’s MIT license remains in place. The six wallpapers are AI-generated; the earlier claim that every wallpaper was drawn with Pillow no longer applies to any of them. The palette and the written notes are original work.
