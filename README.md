# Bharat Mode

**Big Ideas. Real Progress.** — A research-led, faceless YouTube Shorts brand uncovering India's inventions, breakthroughs, people, and measurable progress.

> Status: production starter / pre-launch. The color palette is **provisional** until approved. This repo stores code, story briefs, research standards, brand guidelines and process docs. It does **not** store rendered videos.

## Quick start

Install Node.js 20+ and npm. From the repository root:

```bash
npm install
npm run validate
npm run music:generate
npm run studio
npm run render:sample
```

- `studio`: open the Remotion editor.
- `render:sample`: create `out/param-rudra.mp4` (1080 × 1920, 30 fps).
- `render:icmr`: render a second sample.
- Samples start without voice (`hasVoice: false`) so they can render after music generation. **Do not publish a silent demo.**
- To add natural narration, set `OPENAI_API_KEY`, run `npm run voice -- stories/param-rudra.json`, then change that story's `hasVoice` to `true` and render again. Natural TTS needs a supported provider/model and paid API access; its model identifier is configurable via `OPENAI_TTS_MODEL`.
- Generated voice/music assets are ignored by Git because they are reproducible or replaceable. Keep licensed masters externally and track rights in story metadata.
- Never commit API keys, .env files, unreleased confidential material, licensed third-party footage, or rendered MP4s.

## Repo layout

| Location | Purpose |
| --- | --- |
| `src/` | Remotion components and palette tokens |
| `stories/` | Story briefs, scenes, narration, source links and claim stages |
| `scripts/` | Validation, music generation, and optional TTS generation |
| `docs/EDITORIAL.md` | Sourcing, fact checks, ethics and verification checklist |
| `docs/CHANNEL_BLUEPRINT.md` | Positioning, content pillars, cadence and production plan |
| `docs/PRODUCTION.md` | Reproducible rendering, audio, QA and upload checklist |
| `docs/BRAND.md` | Identity and candidate palettes (awaiting approval) |
| `docs/SAMPLE_YOUTUBE_DESCRIPTION.md` | Publishing copy reference |
| `.github/workflows/validate.yml` | Lightweight story validation CI |

## Canonical creative direction

Bharat Mode is a **phrase / mindset**, not a literal category. A remarkable thing is being built, invented, improved or discovered? *Bharat Mode: ON.* Use the logo/signature as a subtle closing device, never at the expense of the opening hook.

**Editorial promise:** evidence-first optimism. Research ≠ launch, licensed ≠ approved, planned ≠ completed. Every claim must identify its stage, data's as-of date, original source, and any major caveat.

## Status and limitations

This repository is a working starter. There is no automated discovery, upload service, production-ready natural voice pipeline or rendered MP4 in this repo. Validate stories and run Remotion in an environment with npm access before publishing. Recheck source facts before each upload, including older example stories.

No trademark or YouTube handle availability is verified by this repo. Confirm independently.
