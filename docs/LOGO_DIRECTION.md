# Bharat Mode — Approved brand marks

**Status: FINAL — APPROVED by the owner on 22 November 2026.**

This document supersedes every previous BM redraw, concept board, early SVG and HTML preview. **Do not recreate the logo, change its colors, remap letters, or use the old sketches.**

## Canonical artwork — exactly the two owner-supplied SVG files

| Role | Approved repository file | Dimensions / format |
| --- | --- | --- |
| Main badge / horizontal logo | [`public/brand/bharat-mode-badge.svg`](../public/brand/bharat-mode-badge.svg) | SVG with `viewBox="22 221 1405 369"` |
| Channel avatar / icon | [`public/brand/bharat-mode-avatar.svg`](../public/brand/bharat-mode-avatar.svg) | SVG with `viewBox="0 0 320 320"` |

The assets use **vector paths only**, with no external fonts or linked images. Their exact silhouettes, spacing, counters, underline proportions, color fills, wordmark and tagline were supplied and finalized by the owner. These are source-of-truth files; **not generated equivalents**.

### Locked source file checksums (SHA-256)
- `bharat-mode-badge.svg`: `03ec4a83ed34255427724c1b3f77dbe7654d5f31f99e081d570d446d8d5707b5`
- `bharat-mode-avatar.svg`: `0a608f57cb93033a36bce5bd2a7a45bc15bfc3dd26d58478fbf7134d981f818a`

### Actual SVG colors
The owner-provided artwork embeds **its own specific shades**:
- Saffron `#EE7B29`
- Warm ivory `#FDF5EA`
- Teal `#0A8B8C`
- Dark background `#0C141B`

These differ slightly from the separately approved **video UI color tokens** (`src/brand.js`). The logo must **not** be recolored to match UI tokens. Existing UI palette remains unchanged unless separately approved.

## Required usage
- Use the badge for channel banners, brand sheets and understated closing frames.
- Use the avatar in circular YouTube profile contexts, small corner branding and thumbnails.
- In Remotion, import `BrandBadge` or `BrandAvatar` from `src/brand-assets.jsx`. They load the exact SVG files through `staticFile()`.
- Preserve the aspect ratio, background, colors and clearspace of each asset; never stretch or crop the letterforms.
- Do not typeset the original outlined badge wordmark in Sora: the logo is custom vector artwork. **Sora** remains the display typeface for other video content and **Manrope SemiBold** for captions/reading.
- Keep generated voice and final video files out of Git. The logo SVG sources are explicitly approved for Git.

## Change control
Any future brand revision must use a newly approved owner-supplied master and update these files and checksums together. `npm run logo:check` verifies that approved masters have not been accidentally modified.

**Avatar and badge are complete; video layout/caption components still need full render QA.**
