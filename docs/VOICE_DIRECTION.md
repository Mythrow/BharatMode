# Bharat Mode — Approved Voice Direction

**Owner approval:** 23 November 2026  
**Status:** Narrator identity APPROVED; integration, commercial rights and full-video audio QA PENDING.

## Locked decision

- **Voice:** Brian — Deep, Resonant and Comforting
- **Voice ID:** `nPczCjzI2devNBz1zQrb`
- **Selection provider:** vidIQ voiceover (the specific available voice is also listed in the premade ElevenLabs catalog; the current usage path is through vidIQ)
- **Delivery:** professional, informative, clear, credible, warm and composed. Avoid forced hype.
- **Language:** English. **No Indian-accent requirement.**
- **Cost direction:** **no paid voice subscription** and no automatic upgrades. Use available renewable vidIQ credits for prototype work, with balance check and approval if credits prove insufficient. Never assume free means unlimited or commercially licensed.
- **Scope:** default narrator across Bharat Mode content pillars unless the owner changes this decision.
- **Previous auditions:** Callum and Liam were generated, then superseded by Brian.

## Real sample evidence

A Brian audition was generated on 23 November 2026 from this test script:

> India is building more of its own supercomputing infrastructure. Take PARAM Rudra, for example. But how much has actually been deployed, and what can scientists do with it? Here's what the evidence shows.

Audio duration reported by vidIQ: **12.28 seconds**. This short test is not an editorially fact-checked publishable story. Generated voice files are not stored in Git.

## Credit and publication restrictions

At the selection checkpoint, vidIQ reported **38 renewable credits remaining of a 150-credit plan allowance**, next renewal **21 December 2026 IST**. Its current voiceover tool costs **28 credits per started 1,000 text characters**. These balance/pricing figures may change and should be rechecked at generation time.

**Rights gate:** availability of credits and a playable audition sample do **not** by themselves establish commercial-use rights for final YouTube uploads. Confirm licensing and allowed use with vidIQ and relevant voice terms before any public/monetized release. Do not subscribe or pay without explicit permission.

## Integration contract — pending implementation

1. Keep a provider-independent voice profile (see `config/voice.json`) rather than embedding voice IDs into the visual renderer.
2. Generate/receive Brian speech using the available vidIQ tool, download/import final audio to an approved private render workspace. The existing `scripts/tts-openai.mjs` is unrelated to Brian and is **not** the production implementation.
3. Measure duration and perform **true word-level alignment against the final actual audio** using a suitable alignment engine. The vidIQ voiceover result supplies duration and audio, not per-word timing.
4. Normalize word timestamps into the story data model, derive one-line phrase groups, and drive the frozen V6 karaoke caption animation. Validate no missing/duplicated words or overlaps.
5. Connect audio, original music/SFX, dynamic ducking and loudness QA to the migrated full-story V6 renderer, then verify a real 1080×1920, 30fps MP4 on mobile.
6. Preserve original approved narration/voice configuration and proof of commercial rights in private production metadata. Do not commit generated MP3/WAV, video files or credentials.

**Next engineering task:** implement the audio-import and forced-alignment contract, then integrate that timing into `src/short.jsx` with the approved V6 frame. This checkpoint records a voice decision **only** and does not claim a completed pipeline.
