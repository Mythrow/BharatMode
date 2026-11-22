# Bharat Mode

**Big Ideas. Real Progress.** — A research-led, faceless YouTube Shorts brand uncovering India's inventions, breakthroughs, people, and measurable progress.

> Status: production starter / pre-launch. The five official colors are approved: Classic Saffron `#E8752E`, Warm Ivory `#FFF7EB`, Ocean Teal `#117A7A`, Graphite Navy `#283039`, and Deep Charcoal `#0B1018`. Sora and Manrope SemiBold typography confirmed; the owner's final badge and avatar SVGs are approved. Video render QA is still outstanding. This repo stores code, story briefs, research standards, brand guidelines and process docs. It **tracks original background music and sound effects**, but does **not** store rendered videos or generated narration.

## Quick start

Install Node.js 20+ and npm. From the repository root:

```bash
npm install
npm run validate
npm run brand:check
npm run logo:check
npm run variety:check
npm run studio
npm run render:sample
```

- `studio`: open the Remotion editor.
- `render:sample`: create `out/param-rudra.mp4` (1080 × 1920, 30 fps).
- `render:icmr`: render a second sample.
- `thumbnail:sample`: generate a 9:16 still for eligible Shorts thumbnails or social preview.
- `variety:check`: inspect planned publishing order for repetitive layouts, hooks, titles and topics.
- Samples start without voice (`hasVoice: false`) so they can render after music generation. **Do not publish a silent demo.**
- To add natural narration, set `OPENAI_API_KEY`, run `npm run voice -- stories/param-rudra.json`, then change that story's `hasVoice` to `true` and render again. Natural TTS needs a supported provider/model and paid API access; its model identifier is configurable via `OPENAI_TTS_MODEL`.
- Original audio masters are checked in under `public/music/` and `public/sfx/`; run `npm run audio:generate` only when intentionally regenerating these files and review the changes before committing.
- Generated narration in `public/voice/` and rendered videos in `out/` are ignored. Keep licensed third-party assets externally and track license details in story metadata.
- Never commit API keys, .env files, confidential material, third-party footage without repository redistribution rights, rendered MP4s, or generated voice.

## Repo layout

| Location | Purpose |
| --- | --- |
| `src/` | Remotion components, style treatments, font loader and thumbnail composition |
| `stories/` | Story briefs, scenes, narration, source links and claim stages |
| `publishing/queue.json` | Planned sequence to check for repetitive creative patterns (not publication history) |
| `scripts/` | Validation, reproducible original music/SFX generation, and optional TTS generation |
| `docs/EDITORIAL.md` | Sourcing, fact checks, ethics and verification checklist |
| `docs/CHANNEL_BLUEPRINT.md` | Positioning, content pillars, cadence and production plan |
| `docs/PRODUCTION.md` | Reproducible rendering, audio, QA and upload checklist |
| `docs/BRAND.md` | Approved five-color brand kit and typography |
| `docs/LOGO_DIRECTION.md` | FINAL approved owner SVG badge/avatar, exact color values and checksum policy |
| `docs/CHANNEL_BANNER.md` | Owner-approved YouTube cover metadata, Git installation and safe area review |
| `public/brand/` | Approved SVG badge/avatar plus original & 2560×1440 channel banner PNGs |
| `src/brand-assets.jsx` | Reusable Remotion components rendering the approved SVG artwork |
| `docs/TYPOGRAPHY_VISUAL_SYSTEM.md` | Proposed mobile type scales and scene visual grammar (awaiting approval) |
| `docs/SHORTS_DESIGN_SYSTEM.md` | Approved frame architecture |
| `docs/STYLE_PROOFS.md` | Three candidate layout designs for phone review and Remotion still commands |
| `docs/MOTION_SYSTEM.md` | V1 proposed motion rules, flexible chapter timing, captions, transitions and audio behavior |
| `src/motion-system.jsx` | Reusable topic pill, chapter progress and motion primitives |
| `src/motion-preview.jsx` | 14-second Remotion motion study, not ready for publishing |
| `docs/MEDIA_RIGHTS_PIPELINE.md` | Image rights, public-figure photographs, trademarks and asset handling |
| `media/manifest.json` | Approved real-image / third-party-logo licensing registry (currently empty) |
| `docs/ROADMAP.md` | Launch milestones and acceptance criteria |
| `docs/VARIETY_RULES.md` | Rotation rules for visual layouts, thumbnails, titles and storytelling |
| `docs/SAMPLE_YOUTUBE_DESCRIPTION.md` | Publishing copy reference |
| `.github/workflows/validate.yml` | Lightweight story validation CI |

## Audio policy

| Tracked in Git | Ignored and regenerated |
| --- | --- |
| `public/music/ambient.wav` | `public/voice/**` |
| `public/sfx/*.wav` | `out/**`, renders and `*.mp4`, `*.mov`, `*.webm` |
| Audio generation and attribution documentation | Temporary media caches |

Sound design: understated ambient bed; subtle metric cue; a short **Mode: ON** stinger. Audio masters may be replaced by later original or properly licensed masters, with rights documented.

## Canonical creative direction

Bharat Mode is a **phrase / mindset**, not a literal category. A remarkable thing is being built, invented, improved or discovered? *Bharat Mode: ON.* Use the logo/signature as a subtle closing device, never at the expense of the opening hook.

**Editorial promise:** evidence-first optimism. Research ≠ launch, licensed ≠ approved, planned ≠ completed. Every claim must identify its stage, data's as-of date, original source, and any major caveat.

## Status and limitations

This repository is a working starter. There is no automated discovery, upload service, production-ready natural voice pipeline or rendered MP4 in this repo. Validate stories and run Remotion in an environment with npm access before publishing. Recheck source facts before each upload, including older example stories.

No trademark or YouTube handle availability is verified by this repo. Confirm independently.

## Logo sources of truth
The only current, approved logo files are [`public/brand/bharat-mode-badge.svg`](public/brand/bharat-mode-badge.svg) and [`public/brand/bharat-mode-avatar.svg`](public/brand/bharat-mode-avatar.svg), supplied and approved by the owner. Historical experimental logo sketches have been removed from the current repository tree. Remotion uses these exact SVGs in scene branding and thumbnails. The SVG colors are slightly different from the scene UI palette; **do not recolor these final artwork files**.

## Channel banner status
The owner-approved [original channel cover](public/brand/BM_Youtube_Cover.png) is now in Git **byte-for-byte unchanged** at **2048×1152**. An optional [2560×1440 YouTube export](public/brand/BM_Youtube_Cover_2560x1440.png) is also committed. Both versions are protected by `npm run cover:check`. See [docs/CHANNEL_BANNER.md](docs/CHANNEL_BANNER.md) for exact source checksums and the pending YouTube mobile crop review.

## Design proofs
Three editable 1080×1920 Remotion stills are registered: `BharatProofIvory`, `BharatProofDark` and `BharatProofSaffron`. Run `npm run styleproof:ivory`, `npm run styleproof:dark`, `npm run styleproof:saffron`. These are review candidates; see [docs/STYLE_PROOFS.md](docs/STYLE_PROOFS.md) for content source, caveats and QA steps. Generated PNG files stay out of Git under `out/`.

## Motion study (draft for approval)
`npm run motion:preview` creates the animated 14-second `BharatMotionPreview` study in ignored `out/`. It uses true editable Remotion elements, the owner-approved avatar SVG, Sora and Manrope, contrasting topic-only pills, and per-story chapter timing. The sample captions are **not voice-synchronized**; never publish the preview. See [docs/MOTION_SYSTEM.md](docs/MOTION_SYSTEM.md).

## Browser-based motion review
You can review three interactive HTML motion alternatives without installing tools: [Quiet Editorial](previews/html/bharat-mode-a-quiet-editorial.html), [Cinematic Data](previews/html/bharat-mode-b-cinematic-data.html) and [Saffron Process](previews/html/bharat-mode-c-saffron-process.html). Each is standalone, with the exact approved avatar embedded, play/pause and scrubbing. See [review documentation](docs/MOTION_OPTIONS.md). These are browser concepts, not publishable Shorts; no narration/video files are committed.

## Latest motion study — V2 (awaiting final review)
The owner prefers Saffron Process directional movement, typewriter headlines and one-line karaoke word-follow captions. Compare the [mixed-theme HTML browser demo](previews/html/bharat-mode-typewriter-karaoke.html), [ivory demo](previews/html/bharat-mode-typewriter-karaoke-ivory.html), and [charcoal demo](previews/html/bharat-mode-typewriter-karaoke-dark.html). No local code required for these HTML previews. V2 Remotion source: `src/motion-v2.jsx`; new default render command: `npm run motion:preview` (legacy V1 remains `npm run motion:preview:v1`). Full production voice timing requires word alignment to actual audio; prototype timings are simulated. Details: [V2 specifications](docs/TYPEWRITER_KARAOKE_V2.md).

## Current Shorts motion preview V3 (awaiting visual approval)
The latest [motion V3 specification](docs/CAPTION_MOTION_V3.md) responds to feedback: no typewriter cursor, preserved directional animations, a semi-transparent dark rectangular one-line caption backing, 60px Manrope word pop (60% → 112% → 100% in 0.2s) with only the currently spoken word highlighted, and a Manrope Medium topic pill. Open [mixed](previews/html/bharat-mode-motion-v3-mixed.html), [ivory](previews/html/bharat-mode-motion-v3-ivory.html), or [dark](previews/html/bharat-mode-motion-v3-dark.html) HTML demos without installing code. Remotion composition `BharatMotionPreviewV3` is registered; `npm run motion:preview` now targets V3, while older studies are retained at V2 and V1 scripts. `npm run motion:html:v3` reproduces the HTML previews from the exact approved avatar SVG. **Word timing is illustrative until real generated/recorded narration is aligned.**

## Caption Motion V4 — current review
The latest owner feedback replaces the full-width caption band with a **lightly translucent, content-sized box**. Spoken words arrive with the existing 200ms pop/highlight; **older phrase groups disappear when the next phrase starts**. Headlines remain cursorless typewriter and all directional evidence motion is preserved. The [interactive mixed HTML preview](previews/html/bharat-mode-grouped-captions-v4-mixed.html), [ivory](previews/html/bharat-mode-grouped-captions-v4-ivory.html) and [dark](previews/html/bharat-mode-grouped-captions-v4-dark.html) run directly in a browser. Remotion source is `src/motion-v4.jsx`, specification [docs/CAPTION_MOTION_V4.md](docs/CAPTION_MOTION_V4.md). `npm run motion:preview` now targets V4; older variants remain available. **The demo's word timing is estimated; actual narration alignment is still required.**

## Motion V5 — current review
Following V4 feedback, the latest [V5 motion specification](docs/MOTION_V5.md) adds directional sliding to kicker and **whole headline text block while it types**, raises the hero panel by 143px, retains staggered racks and flow-line animation, introduces 0.64s overlapping slide + diagonal wipe scene transitions, and anchors compact grouped captions to the **screen center** so they never slide along with scenes. Open [mixed](previews/html/bharat-mode-motion-v5-mixed.html), [ivory](previews/html/bharat-mode-motion-v5-ivory.html) or [charcoal](previews/html/bharat-mode-motion-v5-dark.html) browser previews; no code installation required. `npm run motion:preview` now targets `BharatMotionPreviewV5`; V4 remains accessible via `npm run motion:preview:v4`. Production voice alignment and full MP4 render QA are still pending.
