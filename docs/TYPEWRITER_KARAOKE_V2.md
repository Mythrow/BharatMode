# Bharat Mode — Typewriter and Word-Follow Captions V2

**Status: USER-DIRECTED MOTION DESIGN, IMPLEMENTATION DRAFT.** The owner prefers directional movement, typewriter headlines and a single-line running spoken-word highlight. Exact motion/timing/phone QA is not yet approved.

## Direction and behavior

1. **Directional movement:** Keep the Saffron Process style of intentional left-to-right movement for explanations, with calmer transitions elsewhere; no distracting bouncing.
2. **Typewriter headlines:** Reveal prominent Sora ExtraBold text character-by-character, initially ~24–30 characters/second. The cursor is temporary and disappears when the line finishes. Do not typewrite dense chart text or every label.
3. **Single-line running captions:** Manrope SemiBold, one horizontal line only, with each new word revealed when spoken. The currently spoken word has the strongest highlight and underline; previously spoken words stay briefly, subdued. The Remotion draft currently retains approximately four preceding words, and never displays future words prematurely.
4. **No caption pill or caption card:** Use a subtle, full-width **bottom legibility gradient**, not a rounded container behind the caption text. Adjust base and active-word color for actual background contrast. Dark/strong saffron scenes use a charcoal lower scrim; ivory scenes use an ivory scrim.
5. **Topic pill:** Upper-right at roughly 72 px from the right canvas edge (previously ~165 px), with contrast against the background; inspect actual YouTube overlays on mobile before sign-off.
6. **Story-driven chapters:** The segmented chapter bar follows editorial beats in each story. No prescribed chapter count, chapter names, 01/03 labels or persistent source/date footer.
7. **Approved brand:** Use the exact user-approved avatar SVG, without recoloring or redrawing. Decorative gradients, waves and diagrams remain secondary to evidence.
8. **Factual qualifiers:** Full source information lives in the YouTube description/internal records, but date/stage qualifiers essential to understanding a statistic must still be spoken/captioned (e.g. "6,000 Rudra servers deployed by September 2026").

## Actual narration synchronization contract

The production caption highlight must follow **audio timing**, not estimate speech pace from text length:

1. Lock the script and chapter boundaries.
2. Produce narration or record a licensed narrator. Generated voice WAV/MP3 remains Git-ignored as requested.
3. Obtain reliable word-level start/end times from a TTS provider if it supports that, or force-align the transcript to the completed audio. Check proper names and spoken number expansion.
4. Store timing metadata in story source JSON, not the generated audio binary.
5. At each frame, select the active word from actual word timestamps. Reveal it progressively and fade prior words. Show only one line, with overflow/safe area checks.
6. Correct uncertain word boundaries by listening; publish only after reviewing actual synchronized audio and mobile overlays.

### Required metadata (example structure, not measured real speech)

```json
{
  "captionWords": [
    {"text":"Rudra", "start": 2.1, "end": 2.5},
    {"text":"servers", "start": 2.51, "end": 2.94}
  ]
}
```

## Interactive review artifacts

- [Mixed background version](../previews/html/bharat-mode-typewriter-karaoke.html)
- [Ivory version](../previews/html/bharat-mode-typewriter-karaoke-ivory.html)
- [Charcoal version](../previews/html/bharat-mode-typewriter-karaoke-dark.html)

Each is HTML with Play/Pause/Replay/Speed/Scrub, the exact embedded approved SVG, typewriter heading and word-follow highlighted captions. They use **illustrative timing and no actual voice recording**. Google Fonts loads Sora/Manrope online; a local fallback may appear offline. These are not publishable videos.

## Editable Remotion study

- `src/motion-v2.jsx` — V2 `BharatMotionPreviewV2` 1080×1920, 30fps, 16s.
- `src/motion-v2-timing.js` — pure timing and visible-window helper.
- `npm run motion:preview` — V2 render to ignored `out/bharat-motion-preview-v2.mp4`.
- `npm run motion:preview:v1` — earlier historical variant.
- `npm run motion:timing:check` — basic timing unit tests.

**Caveat:** Browser demo playback was checked. The Remotion V2 composition has only received a syntax/transpilation check; a successful full Remotion export with Sora and Manrope and real voice/audio sync has not yet been verified.

## Owner review questions

- Does the text type quickly enough to keep momentum?
- Is the active-word highlight + underline strong enough without a card?
- Is the four-word history enough context while reading?
- Is the lower scrim subtle enough in all three theme types?
- Is the far-right topic pill comfortably clear of YouTube's overlay in an actual mobile crop?
## Superseded in V3
The owner subsequently requested removing the cursor and caption underline, restoring a semi-transparent rectangular caption backing, preserving directional animations, enlarging caption text, popping words in from 60% to 112% to 100% over ~0.2s, keeping previously spoken words full color, and using a nonbold topic tag. See [CAPTION_MOTION_V3.md](CAPTION_MOTION_V3.md) for the current review version.
