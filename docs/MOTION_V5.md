# Bharat Mode — Motion V5: direction and scene transitions

**Status: DRAFT FOR OWNER REVIEW (23 November 2026).** This revision responds to the owner’s request to restore directional motion of **all on-screen elements, including headline text while it types**, raise the hero element, center grouped captions, and introduce visible scene-to-scene motion. The approved logo itself is unchanged. V1–V4 studies remain for reference.

## Core rule: directional entrances AND typewriter effect

- Each **headline block moves in from the right** (initially +106 px, easing over 0.54 s), while characters appear at roughly 25 characters per second. **No cursor.**
- Kicker/supporting copy enters from the right (+90 px over ~0.55 s), not just fading in.
- Hero panel enters from the right (+142 px and +16 px down over ~0.74 s), with a staggered rack reveal from left (~82 px offset, ~0.42 s staggering) and a teal–saffron line that grows directionally.
- Decorative background waves/glows remain slow and subordinate. Not every content element must use an identical direction in final videos; use motions that reinforce the story.

## Stronger scene-to-scene transitions

- Demo scenes are each independent layers, intentionally **overlapping for 0.64 s** around boundaries. Incoming begins 0.24 s before the nominal chapter boundary.
- Outgoing layer moves 110 px left and fades. Incoming enters from 150 px right and fades in, with ease-out timing.
- A brief **diagonal saffron + teal transition streak** travels horizontally across the viewport. It is deliberately limited in strength (max 62% alpha), and disappears between boundaries.
- The approved BM avatar and topic pill live in a **stationary shared header**. They do not duplicate or jump during a scene transition.
- This is a proposed signature transition, **not a rule to use it between every micro-scene**. Future videos can use clean cuts for high-frequency information and transitions only when changing narrative chapter or treatment.

## Hero placement

- Old V4: evidence panel top around **y=920** (on 1080×1920).
- New V5: evidence panel top at **y=777**, **143 px higher**, so the visual sits closer beneath the title. Keep sufficient padding under longer headings.
- As scenes vary in headline length, final Remotion layout should consider dynamic height measurements or editorial scene override. This prototype uses a fixed sample with two-line headlines.

## Grouped captions remain centered

- Captions are a **stationary global overlay** anchored at x=540, not children of a scene that slides. They remain centered even while the scene behind transitions.
- Outer safe bounds are x=140…940 (140 px margin on both sides). Caption text is a **single line**, with font reduced only where an unusually long phrase risks spilling beyond the margin.
- Semi-transparent compact backing only wraps visible words, not full-width black strip. Theme-specific backing: rgba(11,16,24,.18) on saffron, rgba(23,40,50,.30) on charcoal, rgba(11,16,24,.10) on ivory.
- Each word starts at 60% scale, overshoots to 112%, settles to 100%, and fades in over ~0.20 s. Only currently spoken word changes to the highlight; prior words return to their normal full-color state. No underline.
- Caption groups replace earlier groups when the next phrase begins. **Do not fade out the last spoken word before it finishes**; the phrase remains legible until the next begins.
- Caption group text originates from **illustrative timings** in this silent proof, not actual audio. Production requires word timestamps from actual narration, verified manually when uncertain.

## Topic pill and brand

- Topic-only pill, e.g. `SCIENCE`, uses non-bold Manrope Medium (500), near right edge of safe header. Uses dark-on-light or light-on-dark contrast.
- The exact final owner avatar `public/brand/bharat-mode-avatar.svg` is embedded in standalone HTML and loaded through `BrandAvatar` in the Remotion study. No redraws of the logo.
- Sora for headlines, Manrope for captions. Browser prototypes load via Google Fonts when online; system-font fallback possible offline.

## Example structure, not mandatory editorial structure

The 16-second study has three beats for a supercomputing example: research backbone → government-reported deployment → significance. **Chapter number and sequence are never fixed across stories.** Subject/source qualifiers belong in the actual narration when needed. Detailed citation remains in the description / story metadata.

## Direct review links

- [Mixed backgrounds](../previews/html/bharat-mode-motion-v5-mixed.html)
- [Ivory-only theme](../previews/html/bharat-mode-motion-v5-ivory.html)
- [Charcoal-only theme](../previews/html/bharat-mode-motion-v5-dark.html)

Play/Pause/Replay/Speed/Scrub and **jump-to-transition** buttons are included in all files. No code setup on the user’s device.

## Remotion source and tests

- `src/motion-v5.jsx` — new 1080×1920 30fps `BharatMotionPreviewV5` composition, 16 seconds.
- `src/motion-v5-timing.js` — pure timing helpers for typed text, directional overlapping scene layers, wipe amount and chapter selection.
- `scripts/test-motion-v5-timing.mjs` — checks scene overlap at t=4.95, entering/exiting directions, clean settled time, wipe boundaries, character counts.
- `npm run motion:preview` targets V5 after this revision; V4 remains available with `npm run motion:preview:v4`.

**QA:** Standalone HTML has been tested through headless Chromium using local font fallback. Caption bounding-box center stayed within 1.5px of canvas x=540 and within x=140…940 for sampled time points. Scene layer overlap and theme switches were verified. The Remotion MP4 has **not** yet been rendered with actual Google fonts or synchronized audio. It remains a draft for owner visual sign-off, not a publishable Short.
## Superseded by simpler V6 transition
The V5 diagonal streak and large scene-slide were rejected. V6 adopts a restrained 0.34s dissolve and restores the missing chapter-progress CSS colors in the browser preview. See [MOTION_V6.md](MOTION_V6.md). V5 remains available for historical comparison.
