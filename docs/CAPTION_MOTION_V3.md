# Bharat Mode — Caption & Headline Motion V3

**Status: OWNER-DIRECTED REVISION, awaiting visual approval of the finished behavior.** Replaces the V2 caption style but does **not** replace the previously approved logo, brand palette or flexible editorial chapter structure.

## Changes requested and implemented

1. **Headline animation only:** A Sora ExtraBold headline types character by character at approximately 26 characters/second. **No caret, cursor, blink or final cursor hold**. This changes the main headline treatment, not supporting animations.
2. **Directional movement retained:** Preserve the earlier Saffron Process stage, kicker slide-in, evidence panel moving from the right, staggered hardware/diagram reveals, flow-line tracing and gentle abstract backgrounds. Motion should explain the story, not be busy decoration.
3. **Caption background restored:** One continuous, dark, semi-transparent **rectangular strip**, not a rounded capsule/pill. Scene-dependent opacity is about 75–89%. Keep it visually separate from the chapter-progress bar.
4. **Caption typography increased:** Manrope SemiBold/Bold, starting at **60px in a 1080×1920** composition, one running line. Final size/length must pass phone and platform-overlay checks.
5. **Color semantics:** Every previously spoken word stays at the normal high-contrast ivory text color, **not greyed out**. The word being spoken temporarily receives a warm saffron/peach highlight; after speech it immediately reverts to the standard color. **No active-word underline.**
6. **Word entrance animation:** At the actual word start timestamp, start at scale **0.60** with opacity 0; animate through **1.12 overshoot** near 120 ms, settle to **1.00** by 200 ms, and fade in over approximately 190–200 ms. No bounce on the entire line. The effect should be short and subtle.
7. **Topic tag:** Contrasting, topic-only pill at approximately 72px from the right frame edge, using **Manrope Medium (500)** instead of bold. Do not add /001, chapter numbers or dates.
8. **Chapter progress:** Keep subtle, segmented, story-driven progress bars. Grouping and chapter length follow each story; do not enforce a fixed five-chapter formula.
9. **Sourcing:** No persistent source/date footer; include citations and publication dates in the YouTube description. Retain essential claim qualifiers as spoken words when necessary, e.g. *deployed by September 2026*.
10. **Avatar:** Display the EXACT owner-approved `public/brand/bharat-mode-avatar.svg`; no font-based redraws.

## Files for browser review — no local code required

- [Mixed saffron → charcoal → ivory animation](../previews/html/bharat-mode-motion-v3-mixed.html)
- [Ivory-only preview](../previews/html/bharat-mode-motion-v3-ivory.html)
- [Charcoal-only preview](../previews/html/bharat-mode-motion-v3-dark.html)

Each standalone HTML preview includes Play/Pause, Restart, a speed selector, timeline scrubber and optional theme switching. The owner-approved SVG avatar is embedded directly. Their word timing is ILLUSTRATIVE and the demos contain no generated narration.

## Editable Remotion proof

- `src/motion-v3.jsx` defines `BharatMotionPreviewV3` (1080×1920, 30 fps, 16 seconds) and reusable `TypewriterHeadlineV3` / `WordFollowCaptionV3` components.
- `src/motion-v3-timing.js` defines deterministic word-entry/active-word helpers.
- `npm run motion:preview` points to V3; `npm run motion:preview:v2` and `npm run motion:preview:v1` preserve earlier proofs.
- `npm run motion:timing:check:v3` verifies the 60% → 112% → 100% 200ms envelope and highlight reset after a word ends.
- `scripts/build-motion-v3-html.py` reproduces standalone browser previews from the approved SVG and implementation source.
- Generated MP4s, voice recordings and review screenshots are NOT committed to Git.

## Production timing rule — do not guess

The HTML and Remotion demo use **illustrative per-word timestamps**, with no voice playing. Production must use real narration and a supported source of word timestamps (TTS metadata or forced alignment of the final audio). At the exact start boundary for each word, trigger the pop-in; highlight it only over its `[start,end)` speech interval. If the speech includes pauses, leave the previous words fully visible in their normal color without highlighting a nonexistent word. Review phonetic accuracy, speed changes and silence manually before publishing.

## QA and outstanding review

- Browser-checked: mixed-background V3 at 1.0, 8.3 and 14.0 seconds; no JS page errors; topic font weight 500; visible caption size 60px; no cursor or underline; staged equipment enters directionally.
- Timing helper tests: passed locally.
- JSX parser check: passed locally.
- **Not yet done:** successful full Remotion MP4 render with approved font files; actual generated voice and forced alignment; check YouTube Shorts UI overlays on real mobile devices; editor sign-off on V3 style.

This design is a **review candidate**, not a locked, approved video motion system.
## V4 revision supersedes V3 caption backing and scrolling
The owner requested a much more transparent caption backing **only around the visible text**, with short phrase groups that replace older ones rather than a continuous scrolling line. The font size, word pop, active-word highlight, cursorless title and directional motion remain. The new version is [CAPTION_MOTION_V4.md](CAPTION_MOTION_V4.md), awaiting visual approval.
