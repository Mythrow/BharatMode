# Bharat Mode

**Big Ideas. Real Progress.** — A research-led, faceless YouTube Shorts brand uncovering India's inventions, breakthroughs, people, and measurable progress.

> Status: production starter / pre-launch. The saffron + ivory + teal creative direction is selected; exact brand tokens remain subject to visual QA. This repo stores code, story briefs, research standards, brand guidelines and process docs. It **tracks original background music and sound effects**, but does **not** store rendered videos or generated narration.

## Quick start

Install Node.js 20+ and npm. From the repository root:

```bash
npm install
npm run validate
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
| `docs/BRAND.md` | Saffron, ivory and teal brand kit |
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
