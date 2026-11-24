# Production guide

> **CURRENT — 24 November 2026:** Owner approved the actual BM-0003 Revision 5 video and the open-canvas 60fps direction. **V6 + approved episode Revision 5** is the reference; [visual rules](OPEN_MOTION_DIRECTION.md) and [template](APPROVED_SHORTS_TEMPLATE.md) are authoritative. Creative review complete; phone QA and explicit publication approval remain separate. Always deliver a direct downloadable MP4. Work stays audio-only. No new render or audio regeneration needed for this approval.

**Historical checkpoints below record what was true at the time; earlier pending review statements are superseded by this approval.**

> **Owner approval / refinements (24 Nov 2026):** V4 open-canvas format approved. Revision 5 requested: true 60fps story animation, quantitative count-ups, minimal meaningful labels, ascending value range and non-overlapping map/network labels. Direct MP4 preferred because embedded-video HTML does not play in owner's chat preview. [Permanent rules](OPEN_MOTION_DIRECTION.md). V5 validation/review pending; do not publish.

> **Latest visual direction (24 Nov 2026):** BM-0003 V4 open-canvas motion review rendered here, replacing static boxed heroes with independently animated graphics and moving backgrounds. Original voice/music unchanged; owner review pending. [Details and permanent visual rules](OPEN_MOTION_DIRECTION.md).

> **Approved geographic storytelling:** Natural Earth 1:10m map data + Remotion (no paid mapping subscription), see [Map Direction](MAP_DIRECTION.md). The current BM-0003 V3 video was actually composed here from the prior private cut using OpenCV/FFmpeg; the Remotion map component is prepared for future from-audio rendering. Work scope stays AUDIO ONLY.

**For a new session, read [PROJECT_STATUS.md](PROJECT_STATUS.md) first.** **OWNER MANDATE:** [PRODUCTION_RESPONSIBILITIES.md](PRODUCTION_RESPONSIBILITIES.md) enforces Work Mode for **AUDIO ONLY** (Qwen WAV, audio QC, alignments); all visual production and MP4 renders happen in this main ChatGPT chat. Previous video rendering in Work was a scope error. Before any story work, check the [permanent Content Log](../content/CONTENT_LOG.md) and [Content Pipeline](CONTENT_PIPELINE.md); existing story drafts have matching `story.contentId` references. It is the canonical resume point; [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) contains the locked V6 visual rules. Do not assume the legacy `BharatShort` renderer fully implements the approved motion/voice system.

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

## MUSIC-06 owner-approved reference mix — Option B

Owner selected MUSIC-06 as the sound identity **and Option B as the reference music/voice balance** on 23 November 2026. `config/music.json.approvedMix` is authoritative: Qwen narrator **88/100**, music between spoken phrases **55/100**, music underneath voice **32/100**, envelope attack **24ms**, release **280ms**. These are **relative linear mixer fader values**, not ear-perceived percentages. **Do not use the original Option A settings (40/16) in future mixes**.

`scripts/preview_signature_mix.py` now takes the approved gains from that config; it produces a *technical reference preview*, not the full story audio. During actual BM-0003 production, mix these stems at the approved baseline, listen for bass/frequency masking, check peak and mobile speech intelligibility and adjust **only if technical QA reveals a problem**, documenting the adjustment. BM-0003 full-story Qwen narration, acoustic alignment and approved V5 MP4 have been completed. Present each next audio check as a self-contained HTML playback page.

## Music volume control for owner review — 23 November 2026

Owner requested music louder than the first mix and **readable 0–100 mixer level meters instead of negative-dB-only figures**. Reproducible `scripts/generate_music06_level_comparison.py` creates **one self-contained HTML** with three embedded 20-second A/B/C music mixes and live fader bars. Use original private input MP3 (MUSIC-06 SHA) and approved Qwen reference WAV (private SHA). Never commit the resulting HTML (it embeds private/externally licensed music). Agent commands:

```sh
python scripts/generate_music06_level_comparison.py \
  --music /private/path/techno-thriller-final.mp3 \
  --voice /private/path/approved-qwen-reference.wav \
  --out out/music06-level-review
```

Audition candidates (gain levels **relative to each stem's original signal**, not subjective loudness):

| Mix | Voice | Music between speech | Music during speech | Active speech voice–music RMS gap |
| --- | --- | --- | --- | --- |
| A / historical | 88/100 | 40/100 | 16/100 | 19.7 dB |
| B / recommended | 88/100 | 55/100 | 32/100 | 13.8 dB |
| C / stronger | 88/100 | 66/100 | 44/100 | 11.0 dB |

The extra musical attenuation is therefore smaller in B/C (music sounds louder beneath the narrator). **Option B is now owner-approved** as the channel reference balance; full episode loudness and mobile-device mastering remain pending. The demos use the previous 7.6-second reference speech, not BM-0003. Peak check passed for each pre-encoding float mix. Phone/speaker and full-video loudness QA remain pending.

## Audio review UX — self-contained HTML (owner preference, 23 November 2026)

For **every future music candidate, narrator audition, voice check and voice/music mix review**, present an **HTML playback preview** in the conversation instead of requiring the owner to download MP3/WAV files or install tooling. Use the generic `scripts/build_audio_review_html.py` helper to embed several review takes in **one self-contained HTML file** (native `<audio controls>`, no network or other file dependencies). Deliver a link to that generated HTML artifact in the same response, not just audio file download links.

Example **for a coding/Work agent**, not the owner:
```bash
python scripts/build_audio_review_html.py \
  --title 'Bharat Mode — audio test' \
  --track 'Ducked mix=out/private/ducked.mp3' \
  --track 'No ducking=out/private/unducked.mp3' \
  --track 'Narrator only=out/private/voice.mp3' \
  --out out/audio-test-preview.html
```
The resulting HTML **contains the full audio bytes encoded internally** and is private media. Do not check it into public Git, email it, or distribute it without the owner's authorization/rights check. MP3/WAV originals are still retained privately for production; the HTML is just a streamlined audition interface.

**Verified MUSIC-06 reference mix levels** (from `scripts/preview_signature_mix.py`, measured using the exact existing voice/music source hashes on 23 Nov 2026):

| Stem | Linear gain | Fader gain in dB | RMS during active speech in 20s preview |
|---|---:|---:|---:|
| Approved Qwen narrator WAV | 0.88 | −1.11 dB | −20.17 dBFS |
| Selected MUSIC-06 without voice | 0.40 | −7.96 dB | — |
| Selected MUSIC-06 ducked during voice | 0.16 | −15.92 dB | −39.90 dBFS |

The music gain is `0.40*(1-0.60*speech_envelope)`: **up to another −7.96 dB**, reducing the music's *signal amplitude* by **60%** while actively speaking. Voice−music RMS level difference during the actively ducked portions was **19.74 dB**, but this is an overlap-window RMS metric, not a LUFS loudness standard. Envelope smoothing: **24 ms attack, 280 ms release** exponential time constants. Tested 20s file uses **original approved narrator audition** (not BM-0003 production script); listening on real phones and full-video mastering are outstanding.

## BM-0003 pilot workflow — offline voice and selected score, 23 November 2026

- Owner selected **MUSIC-06** (private MP3, checksum in `config/music.json`) and confirmed a **paid ElevenLabs Music plan**. Current [Music Terms](https://elevenlabs.io/music-terms) permit commercial YouTube video synchronization without attribution on paid plans. Exact tier/receipt not independently inspected. Do not upload or redistribute stand-alone music files.
- First new story is [BM-0003 L&T Chennai](../content/research/BM-0003.md), source-checked six-scene script [here](../stories/lt-chennai-ai-cluster-order.json), **48 seconds provisional**, status In Progress. No actual voiced story audio and `hasVoice=false`.
- A genuine **20-second MUSIC-06 + approved old Qwen reference** narration ducking demo has been generated using `scripts/preview_signature_mix.py`; input SHAs and peaks verified. This demo is **not the BM-0003 voice** or completed audio mastering.
- `scripts/produce_story_audio.py` generates per-scene commands from the script, pinning the offline Base model and requiring original approved narrator reference. Six offline contract tests pass; full Qwen synthesis requires capable permitted Work Mode CPU. See [BM-0003 production runbook](WORK_MODE_BM0003_RUNBOOK.md).
- Do not mark published or create synthetic video timestamps until real WAVs, transcript, alignment, selected music, approved V6 rendering and phone QA are complete.

## Previous music audition history (archival)

**Historical:** music had not been owner-approved when the early procedural demos were created. **MUSIC-06 was subsequently owner-selected.** The tracked music/SFX listed below are starter prototypes. Three separate 20-second original music directions with approved Qwen narrator comparisons were created for review on 23 Nov 2026. See [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md) and `scripts/generate_music_auditions.py`. Do not mistake a generated demo for the final loop or full-song mixing. The owner will select a sound direction before the first publishable BM-0003 trial; existing master audio and V6 visual code remain untouched. The demos are external, untracked review artifacts.

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

**Completed:** `scripts/qwen_base_voice_test.py` ran successfully offline in Work Mode (8.8-second WAV; 22/22 ASR words; 0.724 speaker cosine; 7.68 GiB peak RSS; 103.5 seconds warm-model test). Owner approved auditory consistency. **Next active story:** BM-0003 L&T Chennai; generate its complete Qwen narration from the same locked reference, verify named entities and numbers, run real alignment, and integrate V6 plus selected MUSIC-06. PARAM Rudra is separate earlier pilot. `npm run voice` still invokes the old OpenAI-only experimental generator and does not represent the Qwen pipeline. Generated audio and MP4s must not be committed.

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
All new production videos are vertical 1080×1920 at native 60fps minimum; runtime is computed from verified narration and actual scene timing. Historical demos and legacy renderer may still be 30fps and are not the approved export standard.

## Before YouTube upload

Creative approval of BM-0003 Revision 5 is recorded. Check device playback, rights and factual qualifiers; deliver direct downloadable MP4 and source-backed upload package. Obtain explicit owner permission to publish; creative approval alone is not upload authorization.
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
