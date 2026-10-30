# GitHub brand system

The portfolio is the source of truth. GitHub uses the same cool dark surfaces, violet emphasis, cyan metadata, and direct language. Assets are static and self-contained.

## Palette

| Token | Dark | Light |
|:--|:--|:--|
| Background | `#070910` | `#f5f7fb` |
| Surface | `#0d111c` | `#ffffff` |
| Text | `#f5f7fb` | `#172033` |
| Muted text | `#a4aec2` | `#4b5870` |
| Violet text | `#a99fff` | `#5140b5` |
| Cyan text | `#61ddec` | `#086779` |
| Meaningful border | `#596780` | `#73809b` |
| Decorative grid | `#182132` | `#e3e8f2` |

The portfolio's `#8b7cff` remains an accent reference. New gradients use bright violet to cyan. Existing project labels use white on violet (`#6352c8` in dark mode, `#5140b5` in light mode), which retains text contrast. Gradients and grids never carry body text or encode outcomes.

## Type and layout

New SVGs use system-ui sans headings and ui-monospace labels, with no web-font dependencies. Desktop profile: 80 px name, 36 px positioning, 20 px labels. Cards: 48 px title, 27 px description, 19 px metadata. Mobile source width is 720 px, displayed at 375 px during review; 66 px name and 43 px card titles. Project diagrams retain outlined text and geometry so their meaning remains unchanged.

Use a 4 px spacing unit, 40 to 64 px content insets, 16 px frame radius, 8 px chip radius, and 1 px source borders. Cards share consistent alignment and label positions. Topic chips describe governance, evaluation, and adoption; they do not imply availability or deployment approval. Five unchanged capability descriptions sit in a two-column semantic HTML table, with the last cell spanning both columns. The table has no invented column headings because it is layout rather than comparative data.

## Delivery and accessibility

All banners and cards retain four variants and the 600 px breakpoint. Every README image has meaningful alt text. Project evidence remains visible and unchanged. No animation is used; reduced-motion preferences need no special fallback. All labels are static. Decorative grids may have low contrast; meaningful borders and text are measured separately in the validation report.

Regenerate profile assets with `python3 scripts/generate_brand_assets.py`. Export each committed project social SVG at its intrinsic 1280 by 640 size, for example `sharp -i assets/social-preview.svg -o assets/social-preview.png` when sharp-cli is installed. The implementation used the sharp JavaScript API, `await sharp(source).png().toFile(destination)`, with no resize. Review PNGs live in `assets/review/`.

See [the inventory](redesign-inventory.md), [prompt review](redesign-prompt-review.md), and [validation report](redesign-validation.md).
