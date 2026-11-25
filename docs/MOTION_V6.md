# Motion V6 — Premium dissolve, restored chapter bar

> **Caption position refinement — owner instruction, 25 November 2026:** Lower the centered word-caption layer by 64px, matching the earlier progress-bar shift. Native 1080×1920: canonical caption outer top y1469 (previously 1405), height 175, centered x540, 140px side margins; BM-002 native compositor uses compact 112px backing at y1501 (previously 1437), baseline y1578 (previously 1514). Retain 24px radius, single-line phrase width, current-word pop/highlight, no shadows/blur and real acoustic timing. Progress stays at y1721. Check actual phone/Shorts overlays before publication. This supersedes the previous instruction to leave captions unmoved; do not reopen published episodes.


> **Owner-approved progress bar refinement — 25 November 2026:** Lower the centered chapter progress indicator by 64 px on the native 1080×1920 canvas: top y=1721, height 13, bottom inset 186, left/right insets 84, total width 912. Keep rounded fills, segment spacing, actual chapter timing and fixed center unchanged; do not move captions or other branding. This supersedes y=1657 / bottom=250 for all new production, starting BM-002. Preserve already-published videos. Verify physical Shorts UI cropping on device before publication. Historical preview files retain their original design unless explicitly regenerated.


**Status: APPROVED VISUAL/MOTION TEMPLATE by owner, 23 November 2026.** The approved version includes a final symmetric chapter-bar alignment fix. Audio is not yet included and word timings remain illustrative. Canonical specification: [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md).

## What changed

1. **Scene transition**: remove the V5 colored diagonal streak and large lateral slide. Crossfade outgoing and incoming themes over **0.34 seconds**, with only **12 px outgoing / 18 px incoming drift**. Backgrounds remain soft and premium.
2. **Within-scene elements**: preserve directional movement: kicker from right (+90px), entire headline block from right (+106px) while typing, hero from right (+142px), staggered racks, expanding directional connection line. Hero remains elevated (y=777), not y=920.
3. **Bottom progress bar**: restored and **centered**, 13px tall at y=1657 (bottom=250), left/right insets both 84px, track width 912px, with 3 example chapter segments. The original V5 HTML had a CSS scoping bug: --bar and --progress were defined on each `.scene`, while the fixed `.progress` element is a sibling, so colors did not resolve. V6 defines them on the parent `.screen` based on `data-active-theme`. Bar is above scene layers with z-index:73. On ivory and midnight it fills saffron; on saffron it fills ivory.
4. **Light-scene caption color**: unchanged from V4 and V5: normal text Graphite Navy `#283039`, current spoken word Deep Saffron `#A63F17`. This follows the approved background-aware caption rule, despite a perceptual difference from light-on-dark scenes. Saffron/dark themes use normal ivory `#FFF7EB` and highlight `#FFBE91`.
5. **Captions**: same V4 grouped word-by-word 0.20-second pop, 60% → 112% → 100%, previous words normal color, current word highlighted briefly, compact translucent backing rather than full-width, x=140..940 centered globally and stationary during scene crossfades.
6. **No cursor**, topic-only medium-weight pill far right, exact official BM avatar.
7. **Variable chapters**, not a fixed editorial structure; the 3 demo groups are only an example.

## Browser review

- [Mixed themes](../previews/html/bharat-mode-motion-v6-mixed.html)
- [Ivory only](../previews/html/bharat-mode-motion-v6-ivory.html)
- [Charcoal only](../previews/html/bharat-mode-motion-v6-dark.html)

All HTML demos contain controls for playback, replay, scrubbing, speed and jump-to-transition. Each is self-contained, including the exact approved logo SVG, and requests Sora/Manrope when online.

## Remotion

`src/motion-v6.jsx` and `src/motion-v6-timing.js` contain the V6 example composition, which now uses reusable `src/approved-shorts-template.jsx` for branding and **centered** chapter progress. `npm run motion:preview` will point to V6 with the earlier versions retained for historical comparison. No MP4 has yet been rendered/verified with aligned narration, so these are design proofs, not publication-ready videos.

## Approval and next work

The owner approved this motion/visual design on 23 November 2026 after requesting the symmetric progress-bar fix. Continue using the exact approved template; no more static-design approval is needed before production trials. **Publication is not approved yet**: obtain real narration with word alignment and a full Remotion render, validate captions and overlay crop on a phone, and review evidence sourcing. Keep source URLs/dates in upload descriptions except when a qualifier is necessary to understand the actual claim.