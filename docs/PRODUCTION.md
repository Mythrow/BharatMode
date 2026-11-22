# Production guide

**For a new session, read [PROJECT_STATUS.md](PROJECT_STATUS.md) first.** It is the canonical resume point; [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) contains the locked V6 visual rules. Do not assume the legacy `BharatShort` renderer fully implements the approved motion/voice system.

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

## Tracked music and SFX

The repo includes original authored audio masters:

- `public/music/ambient.wav` — 9.6-second ambient music loop, repeated quietly under narration.
- `public/sfx/metric-rise.wav` — soft accent on statistical scenes.
- `public/sfx/mode-on.wav` — short end-signature sound.

These assets **are committed** and therefore do not need to be generated on every machine. To rebuild them intentionally, run `npm run audio:generate` and review/commit the updated WAV files. Edit the generator, not only the WAV output, when changing the sound. Generated voice in `public/voice/` remains untracked. Sound designs are original programmatic synths; replace them with appropriately licensed music or professional compositions when moving to production, while retaining source and license details.

## Add voice
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
