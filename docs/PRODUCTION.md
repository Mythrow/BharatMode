# Production — current workflow

Follow [editorial gates](CONTENT_PIPELINE.md), [approved visual rules](APPROVED_SHORTS_TEMPLATE.md), [recovery contract](PRODUCTION_REPRODUCIBILITY.md), [media rights](MEDIA_RIGHTS_PIPELINE.md), [thumbnail/export](THUMBNAIL_AND_EXPORT_DIRECTION.md), [publishing](PUBLISHING_PAGE.md).

## Responsibilities

Work Mode is audio-only: pinned Qwen3-TTS 1.7B Base, approved original reference WAV with SHA-256 validation, exact script per scene, offline ASR/pronunciation QA and real WhisperX word alignment. Never task Work with video/graphics/mix placement/encoding. Main ChatGPT conversation owns actual story-specific visuals, approved V6 compositing, music placement and mix, captions, encoding, review and direct media delivery. Do not ask the owner to run code locally.

## Audio

Read [voice config](../config/voice.json), [reference manifest](../config/narrator-reference.json), [music config](../config/music.json) and [alignment](AUDIO_ALIGNMENT.md). Do not regenerate or replace approved narrator identity. Clear international English using the exact approved narrator identity; an Indian accent is not mandatory, but correct Indian pronunciation is mandatory for Indian names, places, institutions, languages, culturally specific words and terms. Verify story-specific pronunciations with authoritative or native-speaker evidence where available; listen separately from ASR and forced alignment. Keep pronunciation-only synthesis input changes separate from canonical approved script/captions, and regenerate audio hashes and actual alignment after any audio change. Do not change narrator identity to obtain an accent. Calm confidence and subtle enthusiasm; exact script QA each story. Use exact private verified MUSIC-06; Option B 88 narrator/55 music between speech/32 under speech, 24 ms attack/280 ms release. These are linear gains, not perceived loudness. Do not let a built-in track outro silence the final phrase; edit beat-aligned passages with seamless crossfades. Music resolves after last narration (~0.8s default), then one second completely silent final composition. No spoken tagline.

Paid voice subscriptions/APIs/expiring credits are not authorized. OpenAI TTS and Kokoro are historical experiments/fallback only, not the approved voice. MUSIC-01–05 and public ambient.wav/SFX belong to historical demos. Existing paid ElevenLabs Music generation reported by owner is not authorization for new spending; exact tier/receipt and asset rights remain to be verified privately. Never redistribute the track.

## Rendering and QA

Use editable story-specific native source and measured timings; approved frame/caption primitives are reusable, but generic historical renderer/sample and prototype V6 timings are not publishable. Each scene must have unique contextual background and separately animated evidence. Verify actual frame samples before/at/after cues, bounds, safe margins, fonts, captions, chart geometry, continuous motion, scene transitions, progress completion and silent hold. Decode every segment and final video; require exact frame count and consecutive PTS, A/V durations, audio payload/peak/loudness/fade and no unintentional freeze or cutoff. Verify phone/Shorts overlays and audible pronunciation. No upscaled/crop-copy bridge for new production.

Final delivery: byte-identical canonical `BM-###-<slug>.mp4` and `-thumbnail.png`, direct links; no re-encode of approved media. Source, checksums and private recovery package required; published media never regenerated. Audio audition is a private self-contained HTML player with 0–100 fader meters, with usable fallback. Publishing dashboard is chat-first, not ZIP/HTML-only. Do not upload without explicit owner authorization.

## Tool status

Node 22, Python 3.12, Remotion/React pinned where possible, FFmpeg and actual fonts. Historical studies are retained as references, not authority. Run `npm run check`; model inference/phone playback/render QA are distinct from offline checks. See [roadmap](ROADMAP.md) for outstanding integration. [Historical runbooks](archive/README.md).
