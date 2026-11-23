# Production guide

**For a new session, read [PROJECT_STATUS.md](PROJECT_STATUS.md) first.** Before any story work, check the [permanent Content Log](../content/CONTENT_LOG.md) and [Content Pipeline](CONTENT_PIPELINE.md); existing story drafts have matching `story.contentId` references. It is the canonical resume point; [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) contains the locked V6 visual rules. Do not assume the legacy `BharatShort` renderer fully implements the approved motion/voice system.

## Prerequisites
- Node.js 20+ / npm, internet access for initial dependency installation.
- Optional supported speech TTS provider; API key set as environment variable.
- Comfortable video rendering hardware; Remotion may download Chromium during setup.
- An original or appropriately licensed soundtrack and rights-cleared imagery.

## Make the first sample
```bash
npm install
npm run validate
npm run variety:check
npm run studio
npm run render:sample
```
Rendered file: `out/param-rudra.mp4` — **ignored by Git**. Do **not** publish the silent starter.

## Music status and review gate

**Music has not yet been owner-approved.** The tracked music/SFX listed below are starter prototypes. Three separate 20-second original music directions with approved Qwen narrator comparisons were created for review on 23 Nov 2026. See [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md) and `scripts/generate_music_auditions.py`. Do not mistake a generated demo for the final loop or full-song mixing. The owner will select a sound direction before the first publishable BM-0003 trial; existing master audio and V6 visual code remain untouched. The demos are external, untracked review artifacts.

## Tracked music and SFX

The repo includes original authored audio masters:

- `public/music/ambient.wav` — 9.6-second ambient music loop, repeated quietly under narration.
- `public/sfx/metric-rise.wav` — soft accent on statistical scenes.
- `public/sfx/mode-on.wav` — short end-signature sound.

These assets **are committed** and therefore do not need to be generated on every machine. To rebuild them intentionally, run `npm run audio:generate` and review/commit the updated WAV files. Edit the generator, not only the WAV output, when changing the sound. Generated voice in `public/voice/` remains untracked. Sound designs are original programmatic synths; replace them with appropriately licensed music or professional compositions when moving to production, while retaining source and license details.

## Approved TTS engine — Qwen3-TTS, open-weight (23 November 2026)

The owner preferred Qwen3-TTS over Kokoro, approved Qwen3-TTS as the production **engine**, and, after A/B listening on 23 November 2026, **approved the original synthetic narrator's audible consistency as the permanent voice**. **An exact 7.6-second reference WAV is available privately and SHA-verified**; it is not committed. See `config/narrator-reference.json` and `scripts/qwen_reference.py`. The previous Brian recording was a professional-tone inspiration only; vidIQ's credit-bound path is rejected. No Indian accent required.

Use the Apache-2.0 [Qwen3-TTS-12Hz-1.7B-VoiceDesign model](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign) to design an ORIGINAL narrator and the official documented [Base model + reusable clone prompt](https://github.com/QwenLM/Qwen3-TTS) for consistent repeated production. This uses the channel's own synthetic reference, **not the Brian voice**. Details in [VOICE_DIRECTION.md](VOICE_DIRECTION.md) and `config/voice.json`.

**Hard cost boundary:** no paid voice subscriptions, no TTS API charges and no limited or renewable speech credits. Downloadable weights are unmetered for local inference, but compute is necessary. Qwen 1.7B is substantially heavier than Kokoro; **no free remote GPU budget has been verified**. Do not automatically buy cloud resources or ask the channel owner to run code.

**Completed:** `scripts/qwen_base_voice_test.py` ran successfully offline in Work Mode (8.8-second WAV; 22/22 ASR words; 0.724 speaker cosine; 7.68 GiB peak RSS; 103.5 seconds warm-model test). Owner approved auditory consistency. **Next:** generate complete PARAM Rudra narration with the locked private reference, verify proper names and spoken transcript, run real word alignment on final audio, and integrate the approved V6 renderer, original SFX/music and phone QA. `npm run voice` still invokes the old OpenAI-only experimental generator and does not represent the Qwen pipeline. Generated audio and MP4s must not be committed.

## Word-aligned captions — engineering foundation (not finished)

The production approach uses local WhisperX acoustic alignment on **final Qwen narration**; see [AUDIO_ALIGNMENT.md](AUDIO_ALIGNMENT.md), `scripts/align_qwen_words.py`, `src/aligned-caption-timing.js`, and `src/aligned-captions.jsx`. The Python script writes an exact-word-match, checksum-linked output when the actual acoustic model supplies valid timestamps. It refuses to fabricate timings from text duration. Offline contract tests pass; WhisperX inference and end-to-end narrated rendering have **not** run.

Use the new overlay only with a genuine alignment JSON and keep `src/approved-shorts-template.jsx` and owner-approved V6 layout unchanged. The legacy generic `BharatShort` renderer is still to be upgraded after successful Qwen Base identity/compute testing.

## Add voice (legacy experimental OpenAI workflow; NOT the selected free-production direction)
```bash
# PowerShell example:
$env:OPENAI_API_KEY = "your-secret-key"
$env:OPENAI_TTS_MODEL = "supported-tts-model"
npm run voice -- stories/param-rudra.json
```
Review every `public/voice/param-rudra/<scene>.wav` against the allocated scene length (e.g. 6–9s), edit the script or extend the scene as needed, then set `stories/param-rudra.json` field `hasVoice: true`. Run `npm run validate`, render, review. TTS costs money and available model IDs change. Never commit credentials.

## Visual and title rotation

Each story now carries: `visualTheme`, `visualFamily`, `hookType`, `topic`, `thumbnailStyle`, `thumbnailText`, `youtubeTitle` and `narrativeAngle`. Add the slug to `publishing/queue.json` in planned upload order. `npm run variety:check` flags repeated creative patterns. See [VARIETY_RULES.md](VARIETY_RULES.md).

Custom thumbnails: run `npm run thumbnail:sample` (or `remotion still src/index.jsx BharatThumbnail out/your-thumb.png --props=stories/your-story.json`). Shorts custom uploads may be available only to eligible accounts; otherwise select a suitable in-video frame.

Fonts: Remotion downloads OFL-licensed Sora and Manrope via `@remotion/google-fonts` during rendering. Internet access is needed for the initial dependency/font fetch, unless a separate approved caching strategy is configured.

## New stories
Copy a JSON file in `stories/`; set slug, date, claim stage, source URL, source context, a 5–7-scene storyboard, narration and scene durations. Run validation. Render via:
```bash
npx remotion render src/index.jsx BharatShort out/your-story.mp4 --props=stories/your-story.json --codec=h264
```
All videos are vertical 1080×1920 at 30fps; runtime is computed from scene durations.

## Before YouTube upload
- Primary source and date checked again, facts and nuance reviewed.
- Visuals do not misrepresent a prototype as a deployed product.
- Copyright, license and source attribution checked for every asset.
- Captions legible on a phone and not obstructed by YouTube controls.
- Voice pronunciation, timing and narration clarity reviewed.
- Music intelligible under speech; playback levels checked.
- AI-generated voice/realistic imagery disclosed where appropriate.
- Description includes source URL, claim status and as-of date.
- Human final approval. Upload and publish manually in the starter version.

## Non-video file policy
Keep **all editable source, scripts, story JSON, docs, original background music masters, and SFX masters** in Git. Never commit generated narration, .mp4/.mov/.webm, temporary renders, source keys, or heavy raw production footage. If adopting non-reproducible licensed audio or photos later, keep a license manifest in the repo; store the large binaries in approved external media storage.

## Approved brand artwork
Use `src/brand-assets.jsx` to render the owner-approved `public/brand/bharat-mode-badge.svg` and `public/brand/bharat-mode-avatar.svg`. These assets are stored in Git and do not require external fonts. Do **not** replace them with older generated/sketch logos. Run `npm run logo:check` before release to validate the locked SVG originals. The badge/avatar SVGs include their own author-selected color shades even though other scene visuals use `src/brand.js` palette tokens.

## Approved visual/motion template (23 November 2026)

The owner approved V6 with centered chapter bars; see [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md). `src/approved-shorts-template.jsx` is the reusable visual frame. `src/motion-v6.jsx` is the approved-style **silent demonstration**. `npm run motion:preview` generates the demo under `out/` (`out/bharat-motion-preview-v6.mp4`), not a publishable Short. **Do not require the owner to run any commands**; deliver reviewable HTML or rendered outputs in chat. The generic `BharatShort` story renderer remains legacy and needs full V6 integration, word-level voice alignment, factual/evidence checks, phone-safe layout and actual audio mixing before any publication. Run `npm run template:check` to verify progress centering.
