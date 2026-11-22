# Motion V6 — Premium dissolve, restored chapter bar

**Status: REVIEW DRAFT**, not approved final. HTML preview was built by editing the owner's earlier V5 HTML motion study. Audio remains absent and word timings are illustrative.

## What changed

1. **Scene transition**: remove the V5 colored diagonal streak and large lateral slide. Crossfade outgoing and incoming themes over **0.34 seconds**, with only **12 px outgoing / 18 px incoming drift**. Backgrounds remain soft and premium.
2. **Within-scene elements**: preserve directional movement: kicker from right (+90px), entire headline block from right (+106px) while typing, hero from right (+142px), staggered racks, expanding directional connection line. Hero remains elevated (y=777), not y=920.
3. **Bottom progress bar**: restored, 13px tall at y=1657 (bottom=250) with 3 example chapter segments. The original V5 HTML had a CSS scoping bug: --bar and --progress were defined on each `.scene`, while the fixed `.progress` element is a sibling, so colors did not resolve. V6 defines them on the parent `.screen` based on `data-active-theme`. Bar is above scene layers with z-index:73. On ivory and midnight it fills saffron; on saffron it fills ivory.
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

`src/motion-v6.jsx` and `src/motion-v6-timing.js` add a V6 composition. `npm run motion:preview` will point to V6 with the earlier versions retained for historical comparison. No MP4 has yet been rendered/verified with aligned narration, so these are design proofs, not publication-ready videos.

## Review

Assess the transition subtlety, bottom chapter-bar visibility, light-scene caption contrast, and the overall content rhythm. Keep source URLs/dates in upload description except when the qualifier is necessary to explain the actual claim.