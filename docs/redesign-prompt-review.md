# Redesign prompt review

The brief has a clear direction and unusually useful evidence boundaries. Keep the portfolio palette, four image variants, plain language, and preserved disclosures. The current main branches match the described image structure. Older local checkouts do not, so inspect current main before planning changes.

Resolve these ambiguities before implementation:

- **Scope:** name the journey and roles diagrams as well as banners and cards. Otherwise the old palette remains visible. The portfolio repository permits README edits only; reuse the profile's hosted images there rather than adding local assets.
- **Evidence:** compare against current main, preserve every limitation paragraph verbatim, and verify stack labels in executable code and CI. A passing badge means CI passed, not that deployment is approved.
- **Badges:** read the actual license and runtime requirements. Link to CI instead of inventing a static passing-test count. Keep Resolve's experimental status visible.
- **Accessibility:** measure actual foreground/background pairs. Subtle grid lines are decorative; meaningful UI borders need their own contrast check. Test each mobile variant at a real 375 px display width.
- **Typography and size:** use system text for the new profile assets; retain existing outlined project diagrams to preserve wording and geometry. Report size changes separately rather than promising every asset will shrink.
- **Review:** save source-controlled before/after PNGs and a repeatable SVG export command. Check the SVGs as browser image elements as well as through a PNG exporter.
- **Publication:** make one review branch and PR per public repo. Do not merge, change repository settings, run paid model evaluations, or edit private repositories.

See [the revised implementation prompt](github-redesign-prompt-revised.md) and [the brand system](brand-system.md).
