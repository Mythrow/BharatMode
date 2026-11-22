# Bharat Mode — Typography & On-screen Visual Grammar (proposed)

**Status: DRAFT for owner approval before finalizing Shorts templates.** Palette confirmed; typography values and components are proposed for phone-scale QA. Existing Remotion code is an early starter and not guaranteed to implement every specification below.

## Font pairing
- **Display / wordmark / striking numbers:** Bricolage Grotesque, 700–800. Expressive, contemporary and memorable; avoid using it for dense paragraphs.
- **Narration captions / explanation / facts:** Manrope, 500–700. Clear, friendly and crisp.
- **Source/date/micro labels:** Manrope, 500–700, letter spacing reserved for short uppercase labels.
- Both available under SIL OFL; load via `@remotion/google-fonts`. Do not commit font binaries. Keep font legal notices accessible in project documentation as required by the provider's licensing terms.

## 1080×1920 reference scale
These are starting points; verify sizes on a **real phone**, not merely desktop preview.

| Element | Typeface | Typical size | Notes |
| --- | --- | --- | --- |
| Main headline | Bricolage 750–800 | 90–116px | 2–4 short lines, natural line breaks |
| Intro hook | Bricolage 800 | 92–128px | Front-load the most surprising fact |
| Hero numeral | Bricolage 800 | 140–210px | Do not use a numerical reveal in every video |
| Evidence label | Manrope 700 | 30–38px | Short, no overlong uppercase copy |
| Body explanation | Manrope 600 | 42–52px | Maximum 2–3 short lines per moment |
| Spoken captions | Manrope 700 | 42–54px | Max 2 lines, synced with voice, high-contrast backing |
| Source/date | Manrope 600 | 24–30px | Compact but still legible; detailed credits in description |
| Branding bug | Custom logo | 56–88px | Tiny, secondary, not a repeated giant stamp |

Use optical rather than only numeric alignment for huge numerals. Do not use type distortion or fake condensed/stretch effects. Keep English editorial copy in sentence case, not every headline in ALL CAPS.

## Safe areas and mobile layout
- 1080×1920; allow roughly **80–100px left margin** and **100–170px right margin** when YouTube UI icons can cover content.
- Avoid putting subtitles or key facts in the lowest **300–400px**. Check actual mobile UI overlays because Shorts controls vary.
- Prioritize 1 central piece of evidence per scene: a photo, chart, map, document, quote, or mechanism.
- First frame must work silently and promise a specific explanation. Brand animation must never delay the hook.

## Component vocabulary (not fixed template)
- `BrandBug`: tiny saffron icon; can appear at top, not competing with main story.
- `StageBadge`: research / tested / deployed / approved / licensed. Accurate status matters.
- `StoryHeading`: headline + small eyebrow for topic/context.
- `EvidencePanel`: one rights-cleared photo or annotated source document.
- `FactCard`: one statistic with unit, time window and scope.
- `ProcessDiagram`: mechanism with 2–4 stages.
- `QuoteCard`: short attributed quotation only when rights/context permit.
- `MapLocator`: simple location context (not misleading geographic claims).
- `Comparison`: clear same-unit/same-period before/after.
- `CaptionLine`: voice-linked text with anti-clutter timing.
- `SourceFootnote`: source, date and explanation-stage note where relevant.

## Five **visual evidence** treatments
1. **Photo-led** — portrait or genuine institution/field photo, with supporting text.
2. **Diagram-led** — original SVG/Remotion illustration with labeled parts.
3. **Data-led** — verified chart + one careful comparison.
4. **Source-led** — annotated press release, paper or patent, with copyright review.
5. **People-led** — real licensed portrait, person's name/role, clear achievement.

Do not try to fill every scene with a photo or giant statistic. All layouts are assembled from a shared kit, but editorial story shape controls where evidence appears.

## Animation
- Deliberate motion: fade/rise for explanation, line trace for a process, number reveal only where the number is central.
- Avoid bouncing every word, excessive camera zooms, repeated large-card rotations, particles or looping animated flags.
- Transitions typically 8–14 frames at 30fps; let complex diagrams stay on screen longer.
- Closing Mode: ON signature may be <1s with soft committed SFX; skip repeated slow outro.

## Visual QA checklist
- Compare five consecutive Shorts back-to-back on a phone.
- Check 50% scale for source labels and number units.
- Ensure readable subtitles with audio off.
- Confirm a person's face isn't obscured by captions or UI.
- Use `docs/VARIETY_RULES.md` and planned queue checker; not substitutes for human editorial judgment.
- Request owner approval before the final typography/video style system is marked complete.
