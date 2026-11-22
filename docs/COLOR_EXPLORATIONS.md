# Bharat Mode — Saffron selection study (draft)

Status: **AWAITING OWNER SELECTION**. Do **not** silently replace Remotion's canonical `BRAND.primary` with a candidate until the user selects it. Comparative preview frames are generated locally for decision-making and are not finished video stills.

## Neutral colors: keep the roles separate

| Role | Proposed name | Hex | Meaning |
|---|---|---|---|
| Light canvas | Warm Ivory | `#FFF7EB` | Main bright story background |
| Primary small/body text | Graphite Navy | `#283039` | Neutral dark slate; **not teal** |
| Secondary data accent | Ocean Teal | `#117A7A` | Diagrams, supporting chart series |
| Dark canvas | Deep Charcoal | `#0B1018` | Much darker than teal, for cinematic variants |
| Light text | Soft Ivory | `#F9F7F3` | Text over dark backgrounds |
| Pastel panels | Apricot Tint | `#FFE3CC` | Soft cards / details |

Deep Charcoal must remain noticeably darker than the teal and graphite text to preserve distinct light/dark systems. The primary saffron is the focus; teal is not a second primary.

## Five saffron candidates (compare in a complete 9:16 story design)

1. **Classic Saffron — `#E8752E`**: versatile orange-saffron, previously proposed
2. **Bright Bharat — `#F28A1E`**: lively, attention-grabbing warm saffron
3. **Soft Premium — `#E98B4A`**: gentler pastel-leaning editorial style
4. **Burnt Saffron — `#C96122`**: earthy, darker, mature
5. **Golden Saffron — `#F4A340`**: golden optimism, less red than other options

Recommendation to test first: **Bright Bharat `#F28A1E`** or **Soft Premium `#E98B4A`**. On pale ivory, primary saffron may not pass small-type contrast; use neutral graphite for body copy and a darker saffron token for small labels once the primary is chosen.

## Preview requirements for the final decision

- Match composition across all five studies (same story, text, teal and dark canvas).
- Preview vertically at phone size. Compare saffron legibility against both ivory and charcoal.
- Use warm ivory across light scenes, neutral graphite for body, Ocean Teal for technical diagrams, Deep Charcoal for dark scenes.
- Typographic reference: Bricolage Grotesque (display), Manrope (body). Some standalone palette mockups may use a local font substitute; **Remotion source retains the planned actual font system**.
- Do not present speculative or generated photographic technical equipment as evidence of a real event.
- After approval, update `src/brand.js` and both dark/light Remotion themes, then test 9:16 renders and mobile legibility.
- These comparisons supplement `docs/BRAND.md`, which remains a previous proposal until the new color selection is confirmed.
