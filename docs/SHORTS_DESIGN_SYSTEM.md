# Bharat Mode — Shorts design system, Stage 1: Frame architecture

**Status: FRAME ARCHITECTURE APPROVED. Motion behavior is a separate proposal awaiting sign-off; see [MOTION_SYSTEM.md](MOTION_SYSTEM.md).** Brand colors, Sora display / Manrope SemiBold reading, and the owner-approved badge/avatar are locked. The layout rules below are an initial design proposal until three 9:16 frames are reviewed on real phones. No change to final logo artwork is authorized.

## What comes first

Before deciding transitions, scene templates, narration pacing, or an end-to-end video workflow, approve the **frame architecture**. Each viewer should immediately see **one central fact** and understand its evidence. This is a reusable visual grammar, not a fixed slideshow.

## Video foundation
- 1080 × 1920 (9:16), 30fps.
- Safe zones are tentative, not official universal YouTube crop guarantees. Start with 88 px left margin, 165 px right margin, and avoid key facts below y=1570. Avoid cramped top placement and inspect actual Shorts overlays on multiple phones before freezing.
- Editorial content usually occupies roughly x=88–915, y=240–1350; spoken captions around y=1370–1550 when present. Prefer source credits adjacent to the underlying graphic rather than hidden behind bottom controls.
- Topic: single topic-only contrasting pill (SCIENCE, HEALTH, etc.); no numbering or /001.
- Bottom: no source/date stamp, no INDIA/INNOVATION/IMPACT, no 01/03 text. Use flexible chapter progress segments instead.
- Logo: use **only** `public/brand/bharat-mode-avatar.svg` via `BrandAvatar` and `public/brand/bharat-mode-badge.svg` via `BrandBadge`. Do not recreate letters in Sora, and do not redraw/recolor marks.
- No forced branded intro. Hook must appear in the first 1–3 seconds. Badge should be secondary during the story; a short outro is optional.

## Reading order
1. **Hook/headline**: one clear promise or surprising, verifiable fact.
2. **Evidence**: one actual photo, chart, document excerpt, mechanism or map.
3. **Meaning**: one explanatory statement or nuanced caveat.
4. **Captions**: two short lines maximum, with coherent phrase-based timing.
5. **Chapter progress**: a slim, unlabeled segmented strip at the lower edge, derived from story-specific editorial chapters. Sources and publication dates appear in the YouTube description instead of an on-video footer; essential as-of qualifiers stay with claims when needed.

Not all elements are always shown; remove secondary UI when it competes with evidence.

## Approved typography applied to Shorts
- Sora 700–800: large hooks ~92–116px; hero figures ~140–190px. These are ranges, not a mandate.
- Manrope 600: explanation ~42–52px; spoken captions ~44–54px; evidence labels ~28–36px; source/date ~24–30px.
- Light scenes: Graphite Navy `#283039` headline on Warm Ivory `#FFF7EB`; primary large accent Classic Saffron `#E8752E`. For small saffron letters, use accessible `#A63F17`.
- Dark scenes: Warm Ivory headline on Deep Charcoal `#0B1018`; saffron key evidence and teal only where semantically useful.
- No artificial font stretching. Use font size, weight and line breaks to create hierarchy.
- Caption contrast must remain strong on photographs with a translucent or solid backing if needed.

## Three layout proofs to approve next

### A — Ivory editorial / discovery
- Hero: crisp Sora question or unexpected insight; gentle saffron underline accent.
- Middle: evidence-focused photo/diagram or simple chart.
- End: precise Manrope takeaway, slim caption backing.
- Feel: inviting, bright, expert, unhurried.

### B — Deep Charcoal / breakthrough
- Hero: ivory statement and saffron centerpiece (number or actual innovation image).
- Middle: single source-labeled chart, device detail or spatial illustration.
- Supporting teal: one secondary cue only; never compete with saffron.
- Feel: high-impact and cinematic without sensationalism.

### C — Saffron feature / people & progress
- Prefer an ivory or charcoal main canvas with a short full-saffron highlight scene; avoid long sections of small text on bright saffron.
- Evidence: a rights-cleared portrait, before/after comparison or a clearly labeled place.
- Feel: celebratory and human, not patriotic stock graphics.

**Test requirement (prototypes available; see [STYLE_PROOFS.md](STYLE_PROOFS.md)):** Three actual 1080×1920 mockups using the same type system, but different evidence hierarchy. Render at full size; inspect on phone, and test captions with audio off. The composition choices must differ structurally, not just by color.

## Reusable interface components (later)
- `BrandAvatar` and `BrandBadge` — exact approved SVGs.
- `HookHeading`, `EvidenceFrame`, `FactStat`, `ProcessDiagram`, `SourceFootnote`, `CaptionLine`, `StageBadge` and `QuietOutro`.
- Components are shared primitives, not a single repeated scene sequence. See `docs/VARIETY_RULES.md`.

## Acceptance criteria before motion/production work
- [ ] Review A/B/C vertical static frames at small-device size.
- [ ] Headline and any captions immediately readable with sound off.
- [ ] No important fact hidden by device controls/captions.
- [ ] Confirm final logo appears as supplied, with no alterations.
- [ ] Evidence carries source/date/claim-stage context where relevant.
- [ ] Avoid generic cards pasted in every scene; one key visual idea per frame.
- [ ] Approve typography scale and captions, then implement Remotion layout primitives.

## Status of chosen refinements
The user approved contrasting topic-only pills, no persistent source/date footer, no numbered footer, flexible chapter-based progress and subtle abstract backgrounds. These are reflected in the editable style proof sources and proposed motion primitives. Source URLs/dates are retained in story JSON and the video description for publication.

## Next work, after frame sign-off
1. Build reusable visual components and responsive-safe positioning rules.
2. Agree on motions and original audio cues (music and SFX stored in Git).
3. Build word/phrase-level caption timing and TTS generation.
4. Create three **different** factual pilot Shorts, reviewing image licensing and real-world accuracy.
5. Validate at real phone size and compare multiple videos back-to-back for repetition.

## V2 caption direction
The preferred motion uses a typewriter effect for main onscreen headlines, **one-line running spoken-word captions** that reveal words in sync with the voice, a moving active-word highlight, no caption pill/card, and a farther-right topic tag. See [TYPEWRITER_KARAOKE_V2.md](TYPEWRITER_KARAOKE_V2.md). Awaiting visual sign-off.

## Motion direction V3
The current draft retains Saffron Process-style directional transitions while using typewriter headlines **without** a cursor. Caption words appear individually with a 200ms spring-like pop, one line over a dark semi-transparent rectangular strip; active spoken word changes color temporarily; no underlines or greyed previous words. Topic tag weight is 500. See [CAPTION_MOTION_V3.md](CAPTION_MOTION_V3.md). This is not final until owner reviews rendered behavior.

## Most recent caption design — V4
Source of truth for the currently proposed caption rendering: [CAPTION_MOTION_V4.md](CAPTION_MOTION_V4.md). Semi-transparent compact backing follows the visible words (not an edge-to-edge strip); editorial phrase groups replace each other, with word-at-a-time entrance, full normal past-word color and only the current word highlighted. The directional motion and cursorless headline behavior are unchanged. Pending final review.
