# Bharat Mode — Three Shorts style proofs

**Status:** three concept frames ready for OWNER VISUAL REVIEW; they are not approved final motion templates.

## Evidence used for this example
Example fact: **As of September 2026, 6,000 Rudra servers had been deployed in PARAM Rudra supercomputers**, according to PIB, published on 4 October 2026.

- Primary: https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=160306&lang=1&reg=48
- The three images show **illustrative rack diagrams, not photographs of the real deployed equipment**.
- All examples use the exact approved owner avatar SVG in `public/brand/bharat-mode-avatar.svg`.
- Do not present a story's stage as independently verified; the figures are government-reported.
- Distinguish the 6,000 deployed figure from the separately reported 1,500 still under manufacturing.

## The three design treatments
1. **A — Ivory Editorial.** Headline-led, evidence illustration in an editorial paper panel. Best for discovery explainers.
2. **B — Dark Cinematic.** Hero-number-led, one prominent fact, dark industrial-looking schematic. Best for significant statistics and HPC/engineering.
3. **C — Saffron Feature.** Process-led, warm color field and three stages — design, manufacture, deploy. Best for explaining progress and processes.

The designs intentionally do **not** share an identical storyboard. Exact palette `src/brand.js` is used throughout, while the approved avatar retains its owner-authored color values.

## Editable Remotion source
- `src/style-proofs.jsx` contains **three editable Still components**.
- `src/root.jsx` registers their 1080×1920 compositions.
- Generate exact-font stills with:
  ```bash
  npm install
  npm run styleproof:ivory
  npm run styleproof:dark
  npm run styleproof:saffron
  ```
- Remotion uses **Sora** and **Manrope** via `src/fonts.js`. Generated outputs go into ignored `out/`, not Git.

## Current review caveat
The initial screenshots shared in conversation were produced via an offline programmable SVG renderer, because the local machine cannot download the Sora and Manrope font families or Remotion dependencies. Those screenshot PNGs therefore use **Inter as a stand-in** and are concept/layout proofs, not verified Remotion stills. The editable Remotion sources specify the approved font families, but still require a full render and phone review. Do not label a concept as an actual Remotion render.

## Review checklist
- [ ] Compare three 1080×1920 proofs on a phone.
- [ ] Confirm Sora weight and Manrope caption contrast in real Remotion still output.
- [ ] Check YouTube Shorts overlay/safe areas and avoid label clipping.
- [ ] Ensure exact owner avatar artwork is unmodified.
- [ ] Refine caption placement and source label size.
- [ ] Approve design treatments before adding motion.
- [ ] Make reusable motion and captions responsive to content, never mass-produce interchangeable sequences.

## 23 November feedback implemented in source
- Topic label is a **contrasting pill containing only the topic** (no /001 or invented channel index).
- Removed visible source, publication date, `INDIA / INNOVATION / IMPACT` and `01 / 03` footers.
- Added unlabeled segmented chapter bars in the bottom area; demo chapters are editable per story and not a fixed five-step sequence.
- Decorative abstract backgrounds kept.
- Existing previously exported static PNG concept screenshots may **predate this edit**. Regenerate via the three `npm run styleproof:*` commands for the updated visuals. Remotion preview has not yet been verified by a successful export in this environment.
