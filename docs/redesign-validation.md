# Redesign validation

Reviewed 30 October 2026 against the baseline commits in [the inventory](redesign-inventory.md). Changes are isolated to public README/asset work, profile documentation, and the profile asset generator. The portfolio repository changes only README.md.

## Checks

- Playbook: 101 tests passed (52 MCP, 49 evaluation runner/scorer/judge); Ruff passed; repository claims and curriculum snapshot checks passed; all three notebooks validated and executed successfully using temporary local kernels.
- Resolve: 90 offline unit, workflow, privacy, and HTTP contract tests passed. The 60-case regression report and the historical 0-of-16 challenge result match the committed report. Recorded model-screen results replay unchanged. No live model calls were made.
- Markdown: the playbook's complete Markdown lint command passed. The same configured rules (heading increments, trailing spaces, tabs) passed for all edited README and profile documentation files. Other repositories have no existing Markdown lint configuration or test pipeline for README images.
- All original evidence sections in the playbook, Resolve, and portfolio README are byte-for-byte unchanged. Original outlined project text and diagram paths are unchanged. All five capability descriptions are preserved exactly.
- All 34 SVGs decode successfully as browser image elements in Chrome 156.0.8078.74. New SVG text fits within its source viewBox. SVGs contain no scripts, foreignObject elements, embedded raster images, web fonts, or external resources.
- Desktop and 375 px mobile asset PNGs were visually inspected in both themes. Profile and portfolio README previews were also checked in Chrome in all four combinations, with reduced motion requested and no horizontal overflow. These are local previews approximating GitHub typography, not screenshots of GitHub's production sanitizer.
- Both social PNG exports are 1280 by 640 pixels and were visually inspected. They were exported from committed SVG sources through sharp with no resize.

## Contrast

Ratios use the WCAG sRGB relative-luminance formula, calculated from the actual tokens rather than inferred from appearance. Text is kept off the gradient accent. Tables below show the minimum across background and surface where both are used. Decorative grid lines have no content meaning and are excluded from UI-border requirements.

| Theme | Foreground / use | Backgrounds checked | Minimum ratio |
|:--|:--|:--|--:|
| Dark | `#f5f7fb` body | `#070910`, `#0d111c` | 17.58:1 |
| Dark | `#a4aec2` muted body | `#070910`, `#0d111c` | 8.45:1 |
| Dark | `#a99fff` violet labels | `#070910`, `#0d111c` | 8.16:1 |
| Dark | `#61ddec` cyan labels | `#070910`, `#0d111c` | 11.72:1 |
| Dark | `#596780` meaningful borders | `#070910`, `#0d111c` | 3.30:1 |
| Light | `#172033` body | `#f5f7fb`, `#ffffff` | 15.17:1 |
| Light | `#4b5870` muted body | `#f5f7fb`, `#ffffff` | 6.68:1 |
| Light | `#5140b5` violet labels | `#f5f7fb`, `#ffffff` | 7.12:1 |
| Light | `#086779` cyan labels | `#f5f7fb`, `#ffffff` | 6.07:1 |
| Light | `#73809b` meaningful borders | `#f5f7fb`, `#ffffff` | 3.70:1 |
| Both / project filled labels | `#ffffff` | `#5140b5` | 7.64:1 |
| Both / project filled labels | `#ffffff` | `#6352c8` | 5.88:1 |

Dark filled diagram markers (`#6352c8` against `#070910`) measure 3.38:1. Light markers (`#5140b5` against `#f5f7fb`) measure 7.12:1. All body-text pairs exceed 4.5:1; meaningful UI pairs exceed 3:1.

## Asset sizes

Bytes on disk, uncompressed. Existing project diagrams retain outlined text for exact wording, appearance, and geometry; they remain larger and gain only a small gradient accent definition. New profile images use system text to reduce payload substantially.

| Repository / SVG | Before bytes | After bytes |
|:--|--:|--:|
| `ellehelvig/card-playbook-dark.svg` | 19683 | 1569 |
| `ellehelvig/card-playbook-light.svg` | 19683 | 1569 |
| `ellehelvig/card-playbook-mobile-dark.svg` | 20070 | 1716 |
| `ellehelvig/card-playbook-mobile-light.svg` | 20070 | 1716 |
| `ellehelvig/card-portfolio-dark.svg` | 10512 | 1503 |
| `ellehelvig/card-portfolio-light.svg` | 10512 | 1503 |
| `ellehelvig/card-portfolio-mobile-dark.svg` | 9830 | 1494 |
| `ellehelvig/card-portfolio-mobile-light.svg` | 9830 | 1494 |
| `ellehelvig/card-resolve-dark.svg` | 11651 | 1529 |
| `ellehelvig/card-resolve-light.svg` | 11651 | 1529 |
| `ellehelvig/card-resolve-mobile-dark.svg` | 10982 | 1520 |
| `ellehelvig/card-resolve-mobile-light.svg` | 10982 | 1520 |
| `ellehelvig/profile-dark.svg` | 73175 | 2163 |
| `ellehelvig/profile-light.svg` | 73175 | 2163 |
| `ellehelvig/profile-mobile-dark.svg` | 71327 | 2314 |
| `ellehelvig/profile-mobile-light.svg` | 71327 | 2314 |
| `hr-ai-transformation-playbook/journey-dark.svg` | 131358 | 131565 |
| `hr-ai-transformation-playbook/journey-light.svg` | 131358 | 131565 |
| `hr-ai-transformation-playbook/journey-mobile-dark.svg` | 133583 | 133790 |
| `hr-ai-transformation-playbook/journey-mobile-light.svg` | 133583 | 133790 |
| `hr-ai-transformation-playbook/playbook-dark.svg` | 83046 | 83253 |
| `hr-ai-transformation-playbook/playbook-light.svg` | 83046 | 83253 |
| `hr-ai-transformation-playbook/playbook-mobile-dark.svg` | 81692 | 81899 |
| `hr-ai-transformation-playbook/playbook-mobile-light.svg` | 81692 | 81899 |
| `hr-ai-transformation-playbook/social-preview.svg` | new | 1846 |
| `peopleops-resolution-agent/resolve-dark.svg` | 90106 | 90313 |
| `peopleops-resolution-agent/resolve-light.svg` | 90106 | 90313 |
| `peopleops-resolution-agent/resolve-mobile-dark.svg` | 87623 | 87830 |
| `peopleops-resolution-agent/resolve-mobile-light.svg` | 87623 | 87830 |
| `peopleops-resolution-agent/roles-dark.svg` | 136056 | 136263 |
| `peopleops-resolution-agent/roles-light.svg` | 136056 | 136263 |
| `peopleops-resolution-agent/roles-mobile-dark.svg` | 134857 | 135064 |
| `peopleops-resolution-agent/roles-mobile-light.svg` | 134857 | 135064 |
| `peopleops-resolution-agent/social-preview.svg` | new | 1689 |

## Deliberate choices and limits

- Static images keep the visual complete under reduced motion and GitHub image sanitization. No animation was necessary.
- Original project serif headings remain outlined; the new profile/cards and social previews use system sans. Preserving the explanatory diagrams avoids introducing transcription errors or changed meanings. Their palette now follows the same brand tokens.
- Existing narrative, limitation disclosures, failure results, and production restrictions remain visible. No factual claim or tool count was added to the cards. Stack labels were confirmed in Python source, HTML/CSS, MCP facades, CI, evaluation code, and human-review implementation.
- CI badges report current main, with links to the real workflows. They do not imply production approval. Optional dependency installation, Windows-only checks, and paid model evaluations were not rerun locally for this asset-only change; existing hosted CI remains the environment-specific check.
- Social preview files are prepared in the repository. Repository social-image settings were not changed.
- The portfolio README references the profile's new assets by immutable commit SHA. The website HTML, CSS, behavior, and deployment configuration are unchanged.

## Review images

Profile asset comparisons: [before dark](../assets/review/before-dark.png), [after dark](../assets/review/after-dark.png), [before mobile light](../assets/review/before-mobile-light.png), [after mobile light](../assets/review/after-mobile-light.png). All light/dark desktop/mobile combinations are saved alongside these files.

Full README examples: [profile mobile](../assets/review/profile-readme-after-mobile-light.png), [portfolio before](../assets/review/portfolio-readme-before-dark.png), [portfolio after](../assets/review/portfolio-readme-after-dark.png).
