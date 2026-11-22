# Bharat Mode — Brand Kit v1: Saffron + Ivory + Teal

## Brand position
Bharat Mode = a mindset of inventing, building, discovering and making progress in India. Signature: **MODE: ON**. Tagline: **Big Ideas. Real Progress.**

**Direction selected:** rich modern saffron as hero color, creamy ivory rather than clinical white, deep ocean teal as a secondary accent. Deep ink anchors contrast. No flag-stripe look. Warm, curious, editorial and credible.

## Canonical palette (approved color direction; exact v1 hex values subject to exported-video review)

| Token | Color | Hex | Usage |
|---|---|---|---|
| primary | Surya Saffron | `#E8752E` | Distinctive brand orange, large accents, lines and fills |
| saffronText | Burnt Saffron | `#A63F17` | Accessible small text and numbers on ivory |
| ivory | Warm Ivory | `#FFF7EB` | Light background, not pure white |
| teal | Ocean Teal | `#117A7A` | Technical diagrams, data series and supplementary accents |
| tealSoft | Sea Mist | `#E0F0EC` | Teal supporting background |
| ink | Deep Ink | `#183139` | Headlines and dark background |
| peach | Apricot Tint | `#FFE3CC` | Cards and quiet shapes |
| darkHighlight | Warm Saffron | `#F4A767` | Accessible highlight on deep ink |

Contrast guidance (WCAG approximate):
- `#E8752E` on `#FFF7EB` is around 2.8:1: **do not use for small text**.
- `#A63F17` on `#FFF7EB` is around 5.9:1: suitable for normal-sized labels.
- `#117A7A` on `#FFF7EB` is around 4.8:1: suitable for normal-sized teal labels.
- `#183139` on `#FFF7EB` is around 12.8:1: excellent for main reading text.

## The three background treatments

- **Ivory editorial:** target ~65% of uploads. White/peach cards, dark ink headings, saffron numbers.
- **Midnight cinematic:** target ~25%. Deep ink background with saffron and teal highlights.
- **Saffron feature:** target ~10%. One-off milestones and striking art-direction; not for long dense paragraphs.

These are rolling creative targets, not mechanical quotas. Do not place the same `visualFamily` consecutively; theme variation alone does not create originality.

## Typography: no generic sans branding
- **Headlines and logo:** **Bricolage Grotesque**, expressive and slightly eccentric, weights 700–800.
- **Narration captions/body/source:** **Manrope**, weights 400–700, editorial readability.
- **Numbers:** Bricolage Grotesque bold with tabular numeral option; separate number font can be assessed after initial renders.
- Load using `@remotion/google-fonts`; both families are OFL-licensed via Google Fonts. Do not commit font binary files.
- Use sentence case for story headlines; limit all-caps to small labels.

## Layout and accessibility
- Video 1080 × 1920; protect phone safe zones for YouTube overlays.
- Headline hierarchy is strong; short text blocks, one main number per scene.
- Captions are essential for final production (current starter still requires caption pipeline).
- Source attribution stays visible; no implied proof from abstract diagrams.
- Keep branded intro **under 0.5 seconds or omit entirely**; hook first.
- Logo and signature small, not a repetitive giant end slate.
- Use movement to explain data, not simply animate every word.

## Thumbnail system
- Five families: **stat, statement, diagram, split, portrait**.
- 2–5 useful words, never copy the full video title or misstate the story.
- Multiple framing choices: centered numeral, person/innovation photo (licensed), schematic, before/after (only with evidence), and typography-first.
- Custom Shorts thumbnail uploads were announced for YPP creators on desktop in July 2026. Always make an in-video frame that also works if custom upload is not available.
- Design separate stills via Remotion (`BharatThumbnail`); final upload selection depends on account features.

## Non-repetition
See [VARIETY_RULES.md](VARIETY_RULES.md); queue lint checks structured metadata. No simple slides/news reader formula; the story must provide original educational explanation. Review batches visually before publication.

## Sound
Original background music and SFX masters stored in Git. Synthetic narration is regenerated and excluded.
