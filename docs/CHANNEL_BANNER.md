# Bharat Mode — Approved YouTube Channel Cover

**Status:** Owner-approved artwork, **both PNG files committed to the repository** on 22 November 2026. Exact Git blobs and SHA-256 checksums were validated against the local files.

## Canonical source (unchanged, uploaded by owner)
- Git path: [`public/brand/BM_Youtube_Cover.png`](../public/brand/BM_Youtube_Cover.png)
- Resolution: **2048 × 1152 px** (16:9); meets YouTube's minimum banner resolution.
- Bytes: **2,557,370**
- Git blob SHA-1: `11c394d13b3cb80a962d2e3c39f50b3156483b0e`
- SHA-256: `cc732add91a1104492d06522db65871547918a482fae6166919e6c34b8a104ae`
- **This is the exact uploaded PNG, not an AI regeneration and not altered.**

## YouTube upload-ready size (resampled, not independently redesigned)
- Git path: [`public/brand/BM_Youtube_Cover_2560x1440.png`](../public/brand/BM_Youtube_Cover_2560x1440.png)
- Resolution: **2560 × 1440 px** (16:9), YouTube's recommended canvas size.
- Created only by Lanczos resampling from the original 2048 × 1152 source. No elements or logo shapes were redesigned.
- Bytes: **2,233,322**
- Git blob SHA-1: `2ff92cc7d917a14caec49d002bb30eb3031a9e19`
- SHA-256: `a75d719a398e88bf5937bea6e27a3e50209994250be3927479de51037da564d6`
- Upscaling changes pixels but **cannot restore photographic/vector detail** beyond the source; keep the original as the creative master.

## Cropping review is still needed
YouTube displays channel banners using different crops on mobile, desktop and TV. Official specifications: https://support.google.com/youtube/answer/10456525 At the original 2048 × 1152 canvas, the approximate central mobile-safe area is **1235 × 338 px**, centered near **x≈407–1642, y=407–745**. The logo edges approach or extend beyond this region, meaning **some badge edges could crop on mobile** even with a correctly sized image.

Before final publication, inspect the device crop preview inside YouTube Studio. If essential content is clipped, create a separately approved mobile-safe re-layout using the exact authorized badge SVG. Do **not** generate a replacement/altered logo.

## Brand consistency
- Final owner-approved logo sources: [badge](../public/brand/bharat-mode-badge.svg) and [avatar](../public/brand/bharat-mode-avatar.svg).
- The badge embedded in the source PNG is part of the artwork. Do not overlay another copy on top or redraw it.
- Keep both covers, source, documentation and checksums in Git; continue excluding rendered videos and regenerated narration.
- `npm run cover:check` validates dimensions and SHA-256 of both PNG files, preventing an accidental replacement.

## Next milestone
Review actual YouTube mobile crop, then finish Remotion on-screen typography, narration/caption timing, motion components and three visually distinct pilot Shorts. See [ROADMAP.md](ROADMAP.md).
