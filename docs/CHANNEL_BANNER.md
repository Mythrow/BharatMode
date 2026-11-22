# Bharat Mode — Approved YouTube Channel Cover

**Design status:** owner-approved in chat on 22 November 2026.
**Git repository binary status:** NOT YET COMMITTED. The GitHub connector can save text/vector source files but cannot transfer this uploaded PNG's binary bytes. Do not claim that the PNG is committed until `public/brand/BM_Youtube_Cover.png` actually exists in the Git tree.

## Canonical file to add

- Original uploaded filename: `BM_Youtube_Cover.png`
- Git path: `public/brand/BM_Youtube_Cover.png`
- Source dimensions (verified by Pillow): **2048 × 1152 px** (16:9)
- Source PNG mode: RGBA
- Source byte length: **2,557,370**
- SHA-256 of owner-uploaded original: `cc732add91a1104492d06522db65871547918a482fae6166919e6c34b8a104ae`
- YouTube minimum channel art size: 2048 × 1152 (source meets minimum).
- Preferred production canvas: 2560 × 1440. Upscaling this image to 2560 × 1440 changes its pixels and does not improve real detail.
- Do not recreate or regenerate the approved BM badge; it is already composited into the approved PNG. The standalone approved editable badge/avatar SVGs remain at `public/brand/bharat-mode-badge.svg` and `public/brand/bharat-mode-avatar.svg`.

## Installing in repository

From the GitHub repository navigate to `public/brand`, select **Add file → Upload files**, select the user-approved `BM_Youtube_Cover.png`, and commit directly or through a review branch. Alternatively, using a local checkout, copy the approved source file to `public/brand/BM_Youtube_Cover.png`, then `git add`, `git commit`, and `git push`.

After upload, run `npm run cover:check` (once this verifier is available) to check its PNG signature, dimensions and SHA-256. **Do not substitute** a merely visually similar regenerated PNG.

## Channel art crop and mobile checks

YouTube displays different crops on mobile, desktop and TV. At the source's 2048 × 1152 canvas, the approximate central mobile safe area is **1237 × 338 px**, centered at x=405…1642 and y=407…745. Some edges of the current prominent badge may sit just outside this area, and supporting illustration elements intentionally fall outside mobile crop.

Before installing the banner in YouTube Studio, use the built-in device crop preview to confirm that the entire brand mark and tagline remain legible. If the mark is clipped, ask for a separately approved **mobile-safe composition**, not an unauthorized brand logo redraw.

## Follow-up
Once the verified file exists in GitHub, mark this as installed and update the brand task. Next: finalize video typography/layout, voice/caption pipeline, real-image pipeline and three genuinely distinct editorial Remotion pilot Shorts. Rendered MP4s and generated narration remain excluded from Git.
