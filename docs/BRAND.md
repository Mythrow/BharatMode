# Bharat Mode — Official Brand Kit v1

**Status: APPROVED — 22 November 2026.** Palette approved by the owner. This document is the canonical source for brand identity and implementation; see `src/brand.js` for code tokens.

## Brand
- Name: **Bharat Mode**
- Promise: uncover verified Indian inventions, discoveries, builders and measurable progress.
- Tagline: **Big Ideas. Real Progress.**
- Signature: **MODE: ON**
- Character: optimistic, knowledgeable, human, curious, calm; no partisan or government-channel visual cues.

## Five approved brand colors

| Brand role | Name | Hex | Primary application |
| --- | --- | --- | --- |
| Hero | **Classic Saffron** | `#E8752E` | Logo highlight, major figures, markers, graphic flourishes |
| Light canvas | **Warm Ivory** | `#FFF7EB` | Main light video background; avoid pure white as default |
| Secondary accent | **Ocean Teal** | `#117A7A` | Supporting diagrams and charts (not a second headline color) |
| Neutral typography | **Graphite Navy** | `#283039` | Body text and headings over ivory; visually distinct from teal |
| Dark canvas | **Deep Charcoal** | `#0B1018` | Near-black nighttime variant, deliberately much darker than teal |

Only the five above are official primaries. Derived supporting tones may be used **to ensure legibility**: darker saffron `#A63F17` for small text on ivory, light saffron `#FFBE91` for small text on charcoal, light teal `#70D3CC` on charcoal, soft peach `#FFE3CC` for cards, and near-ivory `#FFFCF6` for surfaces.

### Color rules
1. Saffron is the **primary highlight** — Ocean Teal is a supporting accent only.
2. Use Graphite Navy for readable type on Warm Ivory; use Warm Ivory for readable type on Deep Charcoal.
3. **Do not** set small Classic Saffron text directly on ivory: its 2.82:1 contrast is too low for normal text. Use `#A63F17` (~5.91:1) instead.
4. Ocean Teal on Warm Ivory is ~4.83:1. Graphite Navy on Warm Ivory is ~12.57:1.
5. Deep Charcoal on Warm Ivory is ~17.93:1; Classic Saffron on Deep Charcoal is ~6.37:1.
6. Do not fill the screen with literal flag stripes. Convey Indian character through saffron's warmth, deliberate details and editorial content.
7. Reserve full-screen saffron for brief feature moments; use strong neutral contrast.
8. All examples require a real-phone export review; contrast numbers are computed against color tokens, not guaranteed against photographic backgrounds.

## Mixed-theme system
Targets for a sufficiently large run of uploads:
- **65% Ivory editorial:** warm, clean explainers with saffron key figures.
- **25% Deep Charcoal cinematic:** achievements where drama and contrast help clarity.
- **10% Saffron feature:** short, distinctive landmark stories or big reveals.

Targets guide a rotation; they are not a rigid publishing quota. Story form, imagery, hook and narrative must vary independently from color. See [Variety Rules](VARIETY_RULES.md).

## Typography
- **Sora**: confirmed display font for headlines, title cards, brand wordmark and large stats. The custom italic BM icon uses vector paths, not generic typed Sora glyphs.
- **Manrope SemiBold**: confirmed reading font for explanations and captions, with lighter weights available for sources.
- Both loaded via `@remotion/google-fonts`; font binaries should **never** be checked into this repo.
- Prefer sentence case in narrative; do not use all-caps in entire scripts.

## Video treatment
- 9:16, 1080×1920, 30 fps; safe margins for YouTube overlays and subtitles.
- No mandatory intro; surprise and meaning in the first 1–3 seconds.
- Evidence-specific visuals: diagram for how-it-works, credible photo for person-led, validated chart for numbers.
- Reuse a quiet identity dot and understated **Mode: ON** outro without making scenes interchangeable.
- No generated technical event footage passed off as a real recording.
- Sound: original source and SFX stored in repo; generated narration and exported video excluded.

## Thumbnail / cover
- Typography-first, number-first, data diagram, sourced portrait, verified before/after — five layout families.
- Frame selection is necessary when a channel cannot upload custom Shorts thumbnails.
- The first three seconds of every Short must also carry its own identity and hook.

## Current implementation
- Color tokens: `src/brand.js`
- Three treatments: `getTheme('ivory'|'midnight'|'saffron')`
- Video scenes: `src/short.jsx`
- Cover composition: `src/thumbnail.jsx`
- Fonts: `src/fonts.js`
- Brand contract check: `npm run brand:check`

Palette is confirmed, but **a rendered Remotion QA pass remains outstanding**. The original **BM + Underline** icon and horizontal wordmark direction is selected; final exact-shape vector work and visual QA are still outstanding.

## Approved SVG brand marks (owner originals)
The approved badge and avatar are `public/brand/bharat-mode-badge.svg` and `public/brand/bharat-mode-avatar.svg`. Their internal saffron `#EE7B29`, ivory `#FDF5EA`, teal `#0A8B8C` and charcoal `#0C141B` are **intentional logo-specific values**, distinct from the five existing channel video UI tokens above. Preserve the owner's artwork exactly, with no attempts to restyle its letters or replace it with typed text. The actual badge contains fully outlined wordmark paths and does not depend on Sora being installed.

## Channel banner
The approved channel cover design is described in [CHANNEL_BANNER.md](CHANNEL_BANNER.md). The final uploaded PNG must be copied without recreation; its source dimensions are 2048×1152. Both the unmodified 2048×1152 original and a 2560×1440 Lanczos-resampled export are now committed in `public/brand/` and protected by `npm run cover:check`. Mobile/desktop cropping still requires YouTube Studio QA. The separate approved SVG badge/avatar are already present in Git.
