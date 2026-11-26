# Bharat Mode — Variety and originality rules

> **Owner clarification — 26 November 2026:** Mixed-theme proportions are flexible editorial targets, not quotas. Do not force a saffron background where the subject or contrast is better served by charcoal or ivory. BM-005 uses charcoal for its machinery opening at owner direction; reserve the full saffron feature for a suitable beat in the next video if appropriate. Saffron accents remain part of the brand.


> **MANDATORY — scene-level mixed themes (owner approved 26 November 2026):** Plan themes by narrative purpose, not just dominant upload color. Aim approximately 50% Warm Ivory, 30% Deep Charcoal, 20% Classic Saffron across scenes over multiple videos; these are editorial targets, not rigid quotas. Include at least one full saffron feature scene per video where visually appropriate; document a reason if omitted. Prefer saffron for major announcements, landmark figures or a strong closing reveal; ivory for facts, comparisons and instructional diagrams; charcoal for cinematic machinery, space, technology and contrast-rich environments. Technical mechanisms can use ivory or charcoal. Vary sequence with story and avoid forced predictable alternation. All scenes still need unique contextual backgrounds and meaningful motion; changing only color is insufficient. Check actual rendered contrast of all text, labels, captions and progress tracks. Saffron uses dark readable editorial ink, ivory progress fill and sufficiently dark neutral caption backing when needed for ivory/peach caption legibility. This supersedes the old 65/25/10 upload-dominant mix. Do not re-render previously approved releases solely for rotation.


> **MANDATORY — distinct scene backgrounds, owner correction 24 November 2026:** Each narrative scene must have a visibly different story-specific background composition and contextual motion, not a common decorative base with a changed color, gradient, glow or repeated curve. Theme colors may repeat; the artwork, geometry, depth and movement must change to support the content. A continued beat inside the same scene may retain its environment for continuity. V6 locks the branding/chrome (logo, topic pill, typography, captions and centered chapter progress), not background artwork. Before storyboard delivery, assign a unique scene-level background design ID and show actual native-resolution frames; audit the contact sheet for repeated geometry, not just palette, and verify distinct scene background layers in editable source. Before draft delivery, inspect representative rendered frames and within-scene background motion at native 60fps. If this gate fails, correct the source and regenerate before review. Do not reintroduce the prototype V6 radial glow + ellipse as a universal background. Do not include editorial reference labels.

The goal is **recognizable branding without interchangeable videos**. These are internal production heuristics, not YouTube-imposed limits.

## 1. What stays consistent
- Identity: Bharat Mode, saffron/ivory/teal, headline/body font pairing.
- Editorial accuracy: primary source, clear as-of date and caveats.
- Modest source label, clean captions and subtle *Mode: ON* signature.
- Friendly, research-first, evidence-led optimism.

## 2. What rotates

| Dimension | Our rule | Examples |
|---|---|---|
| Dominant background | Aim 50% ivory / 30% dark / 20% saffron across scenes; include saffron where appropriate, no rigid alternation | Ivory explainer, midnight milestone |
| Visual family | **No same visualFamily on consecutive uploads** | data-led, explainer, field-report, people-first, timeline |
| Hook | No hook type three times in a 7-video window | question, unexpected number, contrast, person, mystery |
| Topic | Flag four of the same topic in 7 uploads | research / health / agriculture / communities |
| Thumbnail | Flag same layout three times in 7 uploads, or identical text | stat, statement, diagram, split, portrait |
| Main evidence | Change the storytelling proof, not just the color | source photo, annotated chart, mechanism, map, interview quote |
| Story focus | Vary **how it works**, **why now**, **who benefits**, **what changed**, **what is still unproven** | avoid repeating 'India did X' |
| Pacing | Adapt to topic; normally 30–55 seconds, but not fixed | quick reveal vs chronological narrative |

The new `publishing/queue.json` is a **planned** queue, not proof of publication. Run `npm run validate && npm run variety:check` and review the last 7–10 published videos before scheduling. The tool flags meta-patterns; it **cannot** detect similar imagery, generic scripts or factual errors on its own.

## 3. Five repeatable *but distinct* video genres

1. **The surprising number** — open with a metric then explain precisely what it counts.
2. **How it works** — diagram of an invention or system, then real-world implications.
3. **Meet the builder** — person-led narrative with proof of their contribution.
4. **Before and after** — contextual comparison with same units and time periods.
5. **The untold follow-up** — what happened after the original announcement, including caveats.

The visual family describes the type of evidence. Never fabricate a photo of a real experiment or claim an illustration depicts actual equipment.

## 4. Title guardrails

- Usually 40–70 characters; clarity wins over arbitrary limits.
- Mention the achievement, outcome or concrete benefit; avoid empty 'Great news for India!' titles.
- Rotate opening structures: a number, question, named inventor, consequence, comparison, or location.
- No more than one sensational adjective; **never** invent 'first', 'biggest', or 'world record'.
- Never write a title that asserts testing, licensing or planning equals completion.
- If two titles look substantially interchangeable, rewrite one before publication.

Example title families:
- 'Why India's New Research Machine Matters'
- 'The Village Idea That Saved Water'
- 'What 100 Health Research Deals Really Mean'
- 'How a Small Team Solved a Big Engineering Problem'
- 'This Indian Invention Is Still in Testing — Here's Why It Matters'

Titles above are **examples**; they must not be posted as factual claims without sources.

## 5. Thumbnails / feed frames

- A thumbnail must communicate a **specific story** in 2–5 words.
- A number alone is not enough; contextualize it in visual.
- Use 5 visual families, varying hierarchy, crop and imagery.
- Do not use identical saffron full-screen blocks three times in a row.
- Verify images are owned/licensed; no falsified 'before/after' scenes.
- Shorts feed views usually start playback without the viewer choosing a thumbnail; prioritize the first three seconds of the video too.
- Some channel accounts support uploading custom thumbnails for Shorts; others depend on selecting video frames.

## 6. Script originality review
For **each** Short, reviewer must answer:
1. What new, verifiable fact did the viewer learn?
2. What original explanation, comparison or context did Bharat Mode add?
3. What is the current stage of this achievement?
4. What are its limits, unresolved issues, or date caveats?
5. Is the rhythm, visual evidence and opening different from recent uploads?

**Reject** generic article readings, a pile of stock images, vague AI-written praise, and stories with only one promotional source when impact is disputed. No more than one 'subscribe' request in the video, preferably none.

## 7. Review before publishing
Run the queue lint, skim thumbnails in a 3x3 grid, watch five Shorts back-to-back muted and with audio. If any two look or sound indistinguishable, redesign one even if lint passes.

## 8. Platform rationale
YouTube policy: https://support.google.com/youtube/answer/1311392
YouTube explicitly allows common intros/outros and recurring formats when the actual content is materially varied, original and educational. The risk is mass-produced, interchangeable content. Our rotation heuristics are a **quality tool**, not a guarantee of monetization.
