# Bharat Mode — Grouped captions V4 (review draft)

**Status: awaiting owner's visual approval.** This refines caption presentation only. Preserve V3's directional entrances, staggered server diagrams, animated connecting line, subtle backgrounds, cursorless typewriter headline, topic-only pill using Manrope Medium, and flexible chapter progress bars.

## Changed from V3
- **No full-width caption band:** the background is a compact, translucent box that hugs the words currently visible. In the 1080×1920 canvas it occupies the central safe area at y≈1460 and is capped to available width.
- **Much more transparent:** saffron scene uses `rgba(11,16,24,0.24)`, dark scene `rgba(13,23,32,0.32)`, ivory scene `rgba(11,16,24,0.11)` with graphite text to preserve readability. A 5px backdrop blur is optional, never a thick opaque pill.
- **Natural phrase grouping:** the narration is divided into short editorial phrases. Each phrase replaces the preceding phrase as its first word is spoken; the previous words disappear. No continuous marquee or accumulated sentence.
- **Progressive individual words:** words pop into the current phrase one at a time at the spoken-word timestamp. Spring scale 60%→112%→100%, approximately 200ms; fade ~190ms. Only the currently spoken word uses the highlight color. Previous words remain full normal text color. **No underline.**
- **One line only:** use 2–5 words / short natural clauses, constrained by available rendered width rather than mechanically fixed word counts. The example phrases are editorially chosen and can vary by story.

## Real audio synchronization
- This HTML review is **silent** and uses estimated character-weighted word times. It must not be described as audio aligned.
- Final published Shorts must use time-aligned word boundaries from the actual voice recording, with manual correction as needed.
- Phrases are editorial groupings of consecutive words; the grouping validator rejects omissions, additions or reorderings relative to the transcript. Timed word data + phrase boundaries may be saved in Git; voice/MP4 files stay out of Git.

## Review files
- [Mixed-theme animated HTML](../previews/html/bharat-mode-grouped-captions-v4-mixed.html)
- [Ivory HTML](../previews/html/bharat-mode-grouped-captions-v4-ivory.html)
- [Dark HTML](../previews/html/bharat-mode-grouped-captions-v4-dark.html)
- Remotion implementation: `src/motion-v4.jsx`, registered as `BharatMotionPreviewV4` at 1080×1920, 30fps, 16 seconds.
- Timing helper: `src/motion-v4-timing.js` with `groupWordRanges()` and `groupedVisibleWords()`.
- Tests: `scripts/test-motion-v4-timing.mjs`; `npm run motion:timing:check:v4`.

## QA remaining
- A full Remotion MP4 render with exact Sora and Manrope fonts has not been verified here. Browser preview layout tested with an offline font fallback. Precise final caption line breaks and contrast must be verified on a phone and over real imagery.
- Word grouping, amount of glass opacity, box corner radius and type size remain subject to owner's approval.