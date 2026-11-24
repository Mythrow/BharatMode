# Bharat Mode — Approved Shorts Visual Template

**APPROVED by the owner: 23 November 2026** (final design adjustment: center chapter progress bar).

This is the official **visual and motion-language baseline** for Bharat Mode Shorts, not a completed or published video. It replaces V1–V5 proposals and the V6 *review* status. Subsequent changes to the approved look should be explicitly reviewed. Script structure, evidence type and the number of chapters must remain flexible.

**Final production direction APPROVED (24 November 2026):** The owner reviewed and accepted the actual BM-0003 Revision 5 video. The [approved open-canvas motion direction](OPEN_MOTION_DIRECTION.md) is mandatory alongside locked V6 chrome. Episode Revision 5 is not the old template V5. This is the creative reference for future videos; separate publication approval remains required.

## Approved visual rules

| Element | Final approved behavior |
| --- | --- |
| Format | 1080 × 1920, 9:16, **60 fps minimum** (owner update 24 Nov 2026); animate at actual output timestamps |
| Branding | Exact owner-approved `public/brand/bharat-mode-avatar.svg` / badge SVG; do not redraw |
| Colors | Classic Saffron `#E8752E`, Warm Ivory `#FFF7EB`, Ocean Teal `#117A7A`, Graphite Navy `#283039`, Deep Charcoal `#0B1018` |
| Type | Sora ExtraBold headings; Manrope for reading/captions, normal-weight topic pill |
| Scene families | Ivory editorial, deep-charcoal cinematic, selective saffron-feature scenes, with restrained abstract accents |
| Opening and within-scene motion | Directional entrances/exits for kicker, **whole headline block even while typewriting**, and independent story-specific visual elements; continuous eased camera and environment movement |
| Title | Character-by-character typewriter without a cursor |
| Hero | Open-canvas, integrated into scene; elevated near title, no enclosing evidence cards or bordered hero boxes |
| Scene changes | **0.34-second clean dissolve**, with slight **12 px outgoing / 18 px incoming** lateral drift; no streak or aggressive wipe |
| Captions | A **single-line**, screen-centered short group of words; compact very translucent rectangular backing only behind the visible phrase, not a full-width band |
| Caption animation | Each word pops from 60% → briefly 112% → 100%, with ~0.20-second fade/scale motion. Normal words stay full-color; **only current spoken word** receives a temporary contrasting highlight. No underline. Old phrase group disappears when new group begins |
| Light-scene caption ink | Graphite Navy `#283039`; active word Deep Saffron `#A63F17` |
| Dark/saffron-scene caption ink | Warm Ivory `#FFF7EB`; active word light saffron `#FFBE91` |
| Topic | Contrasting single-topic pill such as SCIENCE; regular/medium weight, near the top-right |
| Chapter indicator | Segmented progress bar derived from **actual story beats**, unlabeled and always visible |
| Statistics | Eased count-up to verified value; dates/model names are identifiers; collision-free labels and correct range direction |
| Background | Contextual moving depth, paths, perspective or particles; no mere static color change |
| Geography / identity | Natural Earth boundaries and verified locations; relevant organization names and rights-cleared marks |
| Delivery | Plain direct MP4 download link always; no dependency on HTML/Play/Open preview |
| Lower metadata | No persistent sources, dates or numbered footer. Full citations appear in video description; essential *as-of* qualifiers must remain in narration/graphics where needed |

## Final progress-bar alignment

The owner specifically asked to center the lower chapter indicator:

- Canvas width: **1080 px**.
- **Left inset: 84 px. Right inset: 84 px.**
- Resulting track width (all segments including gaps): **912 px**.
- Center: **x=540 px** — exactly the video center.
- Bottom: 250 px; track height: 13 px; gaps: 14 px in the approved V6 motion example.
- Progress **fills only** are animated within the centered fixed bar, not translated with scene transitions.
- Adapt the number and duration of segments to the actual story; no prescribed three- or five-chapter sequence.

## Authoritative repository implementation

- `src/approved-layout.js`: canonical dimensions and symmetric progress geometry (importable pure JS).
- `src/approved-shorts-template.jsx`: **reusable approved visual frame**, including fixed top brand strip and centered segmented chapter bar; receives story-specific moving scenes and a caption component as slots.
- `src/motion-v6.jsx`: reviewed and now **approved visual/motion demonstration** implemented using `ApprovedShortsFrame`. Its three demo chapters and example scientific fact are **not** mandated for actual stories.
- `src/motion-v6-timing.js`: V6 soft-dissolve and typewriter math.
- `src/motion-system.jsx`: shared chapter bar, with centered defaults.
- `previews/html/bharat-mode-motion-v6-*.html`: three corrected browser previews for comparison; their CSS uses the same 84 px left/right insets.
- `scripts/test-approved-template.mjs`: prevents accidental reintroduction of asymmetrical bar positions in the approved sources.

## Distinction between approved design and production readiness

**Approved:** the appearance, transitions, typography behavior, progress geometry, caption style, branding and use of varied scenes.

**Still required before publication:**
1. Replace simulated demo caption timing with word-level timestamps aligned to **actual generated/recorded narration**.
2. Parameterize the story-specific motion/content renderer to use the approved V6 frame and captions. The current `src/short.jsx` (`BharatShort`) remains an **older generic scene renderer**; its progress bar is now centered, but it **does not yet fully implement** V6 headline, scene or grouped-caption motion.
3. Source and license authentic visuals, verify story claim wording, and produce genuine visual evidence instead of presenting abstract illustrations as documentary photography.
4. Render a full MP4 with Remotion using actual approved fonts and music/SFX, inspect on phones including Shorts overlay safe zones, and adjust music ducking/loudness.
5. Review three visually varied real-story pilots before scheduling any upload.

**Repository policy:** store brand source SVGs, Remotion/HTML/code, approved specification, and original background music/SFX. Do **not** commit rendered MP4 or generated voice files.

## History

Old template V1–V5 artifacts and earlier BM-0003 episode cuts remain historical. The approved baseline is V6 with centered chapter bars plus the owner-approved **BM-0003 Revision 5** open-canvas treatment; [OPEN_MOTION_DIRECTION.md](OPEN_MOTION_DIRECTION.md) records the final approval and reference.
