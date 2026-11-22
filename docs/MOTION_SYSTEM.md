# Bharat Mode — Shorts Motion System v1

**Status: V1 HISTORICAL DRAFT; THE OWNER SELECTED A V2 DIRECTION.** See [TYPEWRITER_KARAOKE_V2.md](TYPEWRITER_KARAOKE_V2.md) for current review. No animation rules are final until reviewed. Our logo, channel color identity and video font pairing are already approved.

## First principle: chapters follow the story

The default question is **"What does the audience need to understand, and in what order?"** NOT "How do we force the news into five labeled boxes?"

Examples of acceptable sequences:
- Scientific deployment: question → what's deployed → why it matters.
- Medical research: licensing milestone → difference between licensing and patient availability → what comes next.
- Human story: person → challenge → invention → impact.
- Policy implementation: announced → funded → implemented → measured result, where evidence exists.
- A simple discovery may need **2 or 3** beats; a nuanced account may need **7**. There is **no fixed chapter count or mandatory names**.

Write the actual story first; then group related scenes into editorial chapters. The source data has optional `story.chapters`: ordered `{id,title,sceneStartIndex}` entries. The first must start at scene 0, and indices must increase. One chapter may span several scenes. If omitted, a fallback chapter is created per scene, but editors should explicitly group longer stories when appropriate.

The chapter-progress indicator has **one equal-width segment per defined chapter**; each segment fills over its own actual duration. Different length chapters fill at different speeds. There are no numeric chapter labels or noisy bottom metadata.

## Motion design parameters (30fps)

| Element | V1 timing | Behavior / design intent |
| --- | --- | --- |
| Opening hook | visible by 0.0–0.4s | No animated full-screen logo intro; first frame already promises a story |
| Headlines | 12–18 frames (0.40–0.60s) | Ease-out fade + rise 18–28px; no bounce or text distortion |
| Secondary sentence | stagger 5–10 frames after heading | Single phrase enters; longer holds for comprehension |
| Hero number | 18–30 frames (0.60–1.00s) | Smooth reveal, unit stays visible; no fake "world record" counters |
| Simple bar/line diagram | 18–40 frames (0.60–1.33s) | Trace only grounded data; move diagram parts to explain causality |
| Process steps | about 8–14 frames apart | Stage appears only when narrator introduces it |
| Authentic photo | scale 1.0→1.04 over 3–5s if warranted | Gentle movement; never pan to invent presence or context |
| Standard scene transitions | mostly clean direct cuts | 6–10 frame crossfades for actual scene continuity; occasional directional wipe only with meaning |
| Background accents | drift no more than 2–4% of frame width over scene | Decorative, slower than foreground, no perpetual distracting parallax |
| Outro | 0–0.8s or omit | May show exact approved badge briefly; never a lengthy repeated end-slate |

All numbers are editable *starting parameters*, not rigid rules or compulsory animation. Pause longer for dense explanations or detailed photographs. A Short needs moments of stillness.

## Progressive topic pill

- Pill label contains **topic only**: e.g. `SCIENCE`, `HEALTH`, `SPACE` — no `/001` or serial number.
- Warm Ivory → Deep Charcoal pill with ivory text.
- Deep Charcoal → Warm Ivory pill with charcoal text.
- Saffron feature → Deep Charcoal pill with ivory text.
- Do **not** animate the topic repeatedly throughout the story. A simple 8–10-frame fade on its first appearance is enough.
- The brand corner logo always loads the **exact approved owner SVG** through `BrandAvatar`; never recreate B/M in text.

## Captions and source handling

- Spoken captions use **Manrope SemiBold** at about 44–54px; normally no more than two lines.
- Phrase-based, timestamp-aligned to actual speech (not fixed scene intervals); keep words still while they are spoken, and use an understated 5–8 frame fade when phrases replace each other.
- Do **not** animate each word, use typing effects, or highlight every syllable.
- Source URLs, citation lists, publishing date and generic labels belong in the **YouTube description and internal record**, not a persistent video footer.
- Keep source metadata in story JSON, and automatically generate the upload description once that pipeline exists.
- The date/stage may still need to be *spoken or attached to the actual claim* when omission would mislead viewers (e.g. "6,000 deployed by September 2026" versus manufactured but not deployed). This is not a date/footer label.
- Underlying documentary visuals require rights review; illustrative graphics must not masquerade as actual footage.

## Chapter progress bar

- Slim (about 8–11 px) with gaps of about 10–14 px.
- Place in a low-attention strip near the **lower safe region**, provisionally y≈1650–1700 on 1920p; actual Shorts overlay checks are required.
- Equal-width chapter segments, saffron progression on ivory/charcoal; charcoal on full saffron.
- Completed chapters: fully filled. Current chapter: fills continuously with actual time. Future chapters: muted.
- No chapter numbers, percentage, small title or progress at the top of the video.
- If there are too many chapters to retain legible gaps, editors must simplify the visual grouping without falsifying the narrative; don't force a fixed maximum at data level.

## Sound behavior

- Our original music and SFX WAV masters stay in Git.
- Narration is the priority; music should be audibly quieter and automatically duck under speech.
- Reserve subtle SFX for meaningful reveals, transitions or one brand closing gesture; **not** every chart tick.
- Start mix target (subject to actual ear-level testing): music roughly 15–20 dB quieter than narration. Avoid sharp volume jumps. Do not promise loudness compliance without audio measurement.
- Generated narration audio and MP4s stay out of Git; timing metadata and source code may be stored.

## Three visual families retained

1. **Ivory Editorial** — comfortable, bright; headlines, genuine evidence, gentle abstract textures.
2. **Dark Cinematic** — high contrast; saffron key fact, low-noise diagrams.
3. **Saffron Feature** — energetic feature moments; charcoal panels protect readability.

Abstract decoration is welcome, but restrained around charts and text. Do not use background movement as a substitute for an original explanation.

## Video preview for review

Registered `BharatMotionPreview` is a **14-second motion sandbox** with three sample beats (a different chapter configuration can be used on real stories). It demonstrates heading motion, number reveal, simple schematic, topic pills, caption card, sound effects and chapter progress.

Run:
```bash
npm install
npm run motion:preview
```
Output: `out/bharat-motion-preview.mp4`, intentionally Git-ignored.

**Disclosure:** demo captions have manually authored cue text, not actual voice-synchronized timestamps. Music/SFX are sample-level only; this is not yet a ready-to-publish Short. The approved Sora and Manrope fonts load through the Remotion font loader on systems with access to Google Fonts. A full successful render and phone QA have not been verified in this environment.

## Review decisions requested
1. Are the transitions too subdued, too energetic or appropriate?
2. Is the chapter strip in the right position and sufficiently subtle?
3. Should captions sit on a dark rectangular band or on per-phrase translucent backing?
4. Should the topic pill remain fixed throughout a video or appear only at certain points?
5. How frequently should the badge appear? Recommendation: small avatar during the story, full badge only if an outro is used.

The principles and technical parameters above remain flexible until reviewed.

## V2 update
The owner now prefers Saffron Process directional motion, typewriter-style headlines and **one-line word-follow highlighted captions** without rounded background pills. The topic tag moves further right. Prior V1 suggestions against animated word emphasis are superseded by [the V2 design](TYPEWRITER_KARAOKE_V2.md).

## Current creative direction — V3
The owner refined V2 in [CAPTION_MOTION_V3.md](CAPTION_MOTION_V3.md): **no cursor**; preserve all directional entrances, evidence and flow motion; one-line **60px** word-follow captions over a **semi-transparent dark rectangular overlay**; **no underline**, normal brightness for previous words, active spoken word temporarily saffron; each word pops in over ~0.2 seconds from 60%, briefly overshoots to 112%, settles to 100%; topic pill uses Manrope Medium 500. V1/V2 remain historical references. Full voice alignment and output QA remain pending.

## Current draft: V5
V5 restores *directional movement for the entire headline block during character-by-character typing* and the kicker/hero, adds an overlapping scene transition (incoming from right, outgoing left, branded diagonal streak), moves the hero higher and pins grouped captions to the screen center with 140px margins. All V4 word-pop, phrase grouping and active-word color rules remain. [Current V5 spec](MOTION_V5.md). This is a review draft rather than an approved template.

## Current review: Motion V6
The owner requested simpler premium scene transitions, visible bottom chapter bars and a light-scene caption-color check. In [Motion V6](MOTION_V6.md) the transition is now a short, subtle dissolve, the bar is repaired/visible, and previous caption colors are explicitly preserved. V5 colored streak and large scene slide should not be reused without new approval.
