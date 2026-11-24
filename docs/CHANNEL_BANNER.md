# Bharat Mode — Approved YouTube Channel Cover

> **24 November crop correction:** Owner supplied YouTube crop screenshot showing the badge is too high/large for all devices; asked to lower badge and subtitle together. Two image-generated correction drafts were delivered (not exact original pixel transforms; 1672×941 each). Draft 1 was rejected as still too high. Draft 2 lowers the combined group; owner has not explicitly approved the resulting artwork or confirmed its actual Studio crop. Private Library: draft 1 `/BharatMode/brand/banner-safe-area-draft-1.png` ID `libfile_c6001779fbdc8191960b08d160e142c2`, SHA-256 `6cbedb56321ffac8d17518ece941c72bfa4e41275fe5f8122fca2e35097f83f6`; draft 2 `/BharatMode/brand/banner-safe-area-draft-2.png` ID `libfile_59ccbdd299608191b4f4eaa8aa59eb48`, SHA-256 `dce270930e6326784a375558720e1caaa1921e60f74788cbf48e36d4e20a60a8`. Do not overwrite original artwork or call either candidate final. Final goal: 2560×1440, essential logo/text within central approx. 1544×423 region, combined group centered with generous margin, exact approved mark, verify mobile/desktop/TV preview. If further correction needed, prefer precise original asset repositioning rather than regenerating logo. Owner's re-upload of source image was 2048×1152 but bytes differ from original canonical Git PNG; preserve Git original.


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
