# Bharat Mode — Project Status / New-Chat Handoff

**THIS IS THE CANONICAL RESUME POINT.**

Last verified: **23 November 2026**. Work Mode generated and technically validated a Qwen3-TTS Base narrator-consistency sample. Consult Git history for the latest commit. After a task is completed, update this file *in the same commit as the task*, revise the roadmap, and note the actual GitHub commit and any incomplete checks. GitHub is authoritative; old conversation snippets and historical V1–V5 examples are not.

## What the project is
**Bharat Mode** is a research-led, faceless YouTube Shorts channel highlighting verified Indian discoveries, inventions, builders, science, technology and meaningful national progress. Content should find underreported stories without sensationalizing or claiming unsupported "firsts". Voice, evidence and readable vertical animation are core to the product.

Repository: https://github.com/Mythrow/BharatMode

## Current stage — V6 visuals and narrator approved; paid MUSIC-06 selected; first BM-0003 voice and V6 pilot NEXT

### BM-0003 — story/audio preparation completed 23 November 2026

- **Owner-selected first new content:** `BM-0003`, L&T's **23 November 2026** additional Chennai NVIDIA B300 GPU order. Re-verified L&T's **23 November** release and separate **13 August** 10,000-GPU plan. [Six-scene script](../stories/lt-chennai-ai-cluster-order.json) drafted, **48 seconds provisional**, clearly distinguishes newly announced order from planned installed capacity. Linked into the permanent [content registry](../content/registry.json) and creative queue. No duplicate ID or published video.
- **MUSIC-06 licensing:** owner confirmed **paid ElevenLabs Music plan** at generation. Official [9 October 2026 Music Terms](https://elevenlabs.io/music-terms) allow ordinary monetized YouTube audiovisual synchronization without mandatory attribution on Starter-or-higher paid tiers. Exact individual tier/generation receipt not independently inspected; do not redistribute as a standalone music library.
- **Real preview mix created:** original private MUSIC-06 MP3 and existing approved Qwen voice reference were SHA-verified; 20-second stereo ducked music+voice preview generated, peak 0.821 before encoding, no clipping. It contains the **old approved narrator audition, NOT BM-0003 story narration**; phone and full-story mix QA pending.
- **Offline Qwen execution plan prepared:** `scripts/produce_story_audio.py` dry-run produces six exact scene commands using the official pinned Base model. Six Python contract tests passed. The **actual** full BM-0003 WAVs and WhisperX alignment have **not run**; 5.8 GiB chat RAM is below the previously measured 7.68 GiB Qwen Base peak.
- **NEXT:** run real scene narration/ASR/acoustic alignment on permitted free Work Mode compute; pair with MUSIC-06 and owner-approved V6 visual frame; deliver a first complete voiced MP4 for owner review. [Runbook](WORK_MODE_BM0003_RUNBOOK.md). No paid TTS credits/API/compute, no publishing without final sign-off.

### Previously selected music master — MUSIC-06 (archival checkpoint)

### MUSIC-06 signature master selected — 23 November 2026

- User approved their uploaded `techno-thriller-final.mp3` for Bharat Mode. Exact original MP3 stored privately at `BharatMode/music/techno-thriller-final.mp3` in ChatGPT Library, SHA-256 `adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9`, 54.99 seconds, stereo 44.1 kHz MP3 192 kbps. Original master is **not** public Git media. Details in [config/music.json](../config/music.json) and [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md).
- Use as the recognizable default for first ~5–10 Shorts with varied sections, levels, cuts and Qwen narration ducking. Later maintain 2–3 related textures to avoid repetitive identical soundtracks. MUSIC-01–05 are superseded; do not re-request selection.
- **Updated after this selection:** owner confirmed paid ElevenLabs Music plan; official current terms allow ordinary commercial YouTube video synchronization without attribution for paid tiers. The exact account tier/receipt was not independently inspected. Final mixed-video QA and publication permission still pending.
- The existing `public/music/ambient.wav`, original SFX and approved V6 visual template remain untouched. Next: mixed BM-0003 pilot with final voice alignment, licensed soundtrack verification and phone QA.



### Historical/superseded audition — MUSIC-05 melodic techno, 23 November 2026

- Owner rejected the MUSIC-04 hip-hop feel and wants **modern melodic techno**, with a **deeper low/mid synth melody and prominent bassline**, not high-key keyboard notes.
- Created **MUSIC-05 Deep Current**, an original 30.968-second, 124 BPM, four-on-the-floor F-minor techno candidate. Music-only and approved-Qwen-narrator-mixed WAVs/MP3s were generated, with stereo PCM16 WAV readback and no clipping; exact SHA hashes and code in [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md) and `scripts/generate_melodic_techno_audition.py`.
- **Superseded:** owner subsequently chose the separate paid ElevenLabs MUSIC-06 techno-thriller recording. V6 and approved narrator remain unchanged; MUSIC-05 was not adopted.


### Historical MUSIC-04 lo-fi audition — superseded by MUSIC-05

- Owner listening feedback on earlier scores: **MUSIC-01 too boring/simple**; likes MUSIC-03 rhythm and MUSIC-02 tune; wants a lo-fi beat with both traits. This is **directional feedback, not soundtrack approval**.
- Created a 31.304-second original **MUSIC-04 Lo-Fi Motion** audition at 92 BPM: swung hip-hop drums, warm Rhodes-style harmonic progression, brighter original melodic hook and subtle tape texture. Music-only and Qwen-narrator-mixed WAV/MP3 previews delivered in chat. Original reproducible source in `scripts/generate_lofi_audition.py`, details/checksums in [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md).
- Both 44.1 kHz stereo PCM16 WAVs passed readback, finite-sample and peak tests with no clipping; the mixed preview uses the exact owner-approved private reference. **Human listening is pending.** No soundtrack or SFX masters replaced and no V6 modifications.
- **Superseded:** owner rejected the hip-hop feel and requested MUSIC-05 instead. If it matches the desired groove, iterate to a real loopable, length-adaptable production music bed and matching minimal sonic stinger, then verify voice mixing and phone playback before locking music.



### New soundtrack selection checkpoint — 23 November 2026

- **Historical, pre-MUSIC-06 checkpoint:** old repository `public/music/ambient.wav` and `public/sfx/*.wav` were starter placeholders; the owner later selected MUSIC-06 as the new signature soundtrack, while production integration remains pending.
- Created three original, no-subscription procedural 20-second music candidates: `MUSIC-01 Quiet Momentum` (understated warm editorial), `MUSIC-02 Curious Discovery` (airy science-optimism), and `MUSIC-03 Built Forward` (restrained engineering momentum). Each has an instrumental-only WAV and an audition mix with the exact **approved private Qwen3 narrator**. Three narrated MP3 previews also generated for convenient listening in this chat.
- All six WAV previews were generated and checked as stereo 24 kHz PCM16, 20 seconds, below clipping; Python generator syntax and an instrumental-only run without a private voice passed. No preview has been **human auditioned/approved** yet; no long seamless looping/music loudness phone QA or final SFX identity has been verified.
- Composer source: [generate_music_auditions.py](../scripts/generate_music_auditions.py); editorial options and approval criteria: [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md). Preview binaries remain untracked, and **all existing production music/SFX masters and the approved V6 frame are unchanged**.
- **Superseded:** owner completed music selection with MUSIC-06. No further MUSIC-01/02/03 auditions needed. Work on actual BM-0003 narration and V6 integration.



### Permanent content ID registry launched — 23 November 2026

- **Single source of truth:** [Content Log](../content/CONTENT_LOG.md) (human-readable boards: Idea, In Progress, Published), [Canonical registry JSON](../content/registry.json), and [one research sheet per ID](../content/research/). Every candidate and completed Short retains a permanent, never-recycled `BM-####` ID. See [CONTENT_PIPELINE.md](CONTENT_PIPELINE.md).
- **Imported existing work:** `BM-0001` PARAM Rudra (In Progress); `BM-0002` ICMR 100 tech-transfer deals (Idea, despite having an unvoiced storyboard); `BM-0003` L&T's **23 Nov 2026 new NVIDIA B300 Chennai order** (**In Progress**, owner chose to trial; **not published**); `BM-0004` IIT Madras 22 Nov sleep/autism labs (Idea).
- Story briefs `param-rudra`, `icmr-tech-transfer` and now `lt-chennai-ai-cluster-order` match their permanent content IDs; the selected [BM-0003 dated research](../content/research/BM-0003.md) and 48-second provisional storyboard exist. No full Qwen story narration or video upload yet. Keep the legacy `publishing/queue.json` for already-written story slugs only, not as the content registry.
- `scripts/content-registry.mjs` allocates IDs, searches all stages, enforces duplicate event/source/title and same-topic follow-up checks, validates stage transitions, and generates the content log. **Fourteen local automated tests passed**, including no deletion/reuse, duplicate intake, transition/published gates, cross-link requirements and stale-log detection. CI now checks the registry (note: unrelated GitHub Actions runner startup issues remain possible).
- **Editorial rule:** every daily candidate is compared against **all IDs including Published**. New developments in previously covered topics need a distinct event, related ID and explicit reason. A topical or semantic overlap still requires human editorial assessment; mechanical dedupe isn't perfect.


### Permanent narrator approved — 23 November 2026

- **Owner reviewed both WAVs and explicitly approved their similar, consistent voice.** This finalizes the identity of Bharat Mode's original Qwen3 synthetic documentary narrator; **do not ask for another A/B approval**.
- Reference SHA: `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c` (7.6s, 24 kHz mono PCM16). Exact private reference transcript and VoiceDesign model revision are frozen in `config/narrator-reference.json`. Qwen3-TTS 1.7B **Base** revision `fd4b254389122332181a7c3db7f27e918eec64e3`, new-line test SHA `c2a323ced010a718a90e03bdd365fe9b15a2d8b5ff6446ab71302cf6b0d6688b` (8.8s; 22/22 ASR words; 0.724 embedding cosine).
- **Approved voice identity ≠ all future takes approved.** The original `PARAM` pronunciation remains unverified: offline ASR transcribed "Parum". Check proper names, all spoken words and loudness for each final story.
- **Active pilot is now BM-0003 L&T Chennai** using the approved voice reference; generate its full script on permitted Work Mode CPU, measure pronunciation and throughput, align real WAVs, and integrate locked V6. PARAM Rudra BM-0001 remains a separate in-progress earlier pilot, not the current daily-story production target.


### Verified Base narrator-consistency test — 23 November 2026

- Used the original private 7.600 s VoiceDesign WAV after re-verifying its SHA-256 and 24 kHz mono PCM16 format against [the reference manifest](../config/narrator-reference.json).
- Ran the official Qwen3-TTS 1.7B Base checkpoint offline on four CPU threads, with staged float32 processing and the exact private reference transcript. Generated 8.8 s of new speech. The real-file integrity gate passed with no clipped samples. Offline Whisper Tiny English recovered all 22 words of the new passage.
- Speaker-embedding cosine similarity was **0.724** between the reference and the new sample using SpeechBrain ECAPA-TDNN. The two halves of the reference scored 0.638 and the two halves of the new sample scored 0.793. This supports consistency for this pair. Owner A/B listening is now **approved**, while original `PARAM` pronunciation review remains open.
- **Measured:** 103.5 s from model loading through WAV write, including 101.8 s for the staged generation path. Peak process RSS **7.68 GiB** on a 9.7 GiB Work Mode workspace. Installation and weight downloads are excluded. No paid compute, speech APIs, subscriptions or credits.
- The private WAV was delivered in the Work Mode conversation. Model revision, checksums, timing breakdown and the tested command are in the [Base runbook](WORK_MODE_BASE_RUNBOOK.md).

### Verified Qwen3-TTS Work Mode audition — 23 November 2026

- Downloaded the official 1.7B VoiceDesign weights and speech tokenizer, verified their SHA-256 hashes, and ran inference from local files with Hugging Face offline mode on a CPU-only Work Mode workspace (9.7 GiB reported RAM). No paid compute, metered voice API, subscription, or voice credits were used.
- Fed the voice prompt from [config/voice.json](../config/voice.json) and the exact PARAM Rudra audition text from [the smoke script](../scripts/qwen-voice-design-smoke.py). Verified a 7.6-second, 24 kHz mono PCM WAV. The owner can play the sample in the Work Mode conversation. The WAV is kept outside Git.
- The audition now serves as the verified engineering reference. The owner can compare it with the new Base sample.
- Earlier GitHub Actions [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) still records a separate runner startup failure before any step. Work Mode testing used the repository smoke script with a pinned local snapshot, a fixed seed, and staged float32 processing. The all-float32 attempt was killed under memory pressure and an INT8 sample failed the transcript check. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) for settings and timings.

### Caption alignment engineering checkpoint — 23 November 2026

- Built `scripts/align_qwen_words.py` to use a locally installed open-source WhisperX forced aligner on **real finalized narration WAVs**, writing checksum-linked word starts and ends. It rejects missing words, invented words, overlapping/invalid times, and transcript mismatches rather than estimating word times.
- Built `src/aligned-caption-timing.js` and `src/aligned-captions.jsx` as an **optional** centered word-synced V6 caption overlay. Group timing comes exclusively from a `final-audio-acoustic-alignment` file, never the old simulated demo timings. The approved V6 frame, layout and legacy story renderer were **not changed**.
- **Tests actually executed here:** eight Python alignment-contract tests, thirteen JS assertions, real reference-WAV header/hash check. All passed. Tests do **not** exercise WhisperX inference or Qwen Base.
- **Still pending:** run WhisperX on finalized narration, verify actual word timing, and render with V6. See [AUDIO_ALIGNMENT.md](AUDIO_ALIGNMENT.md).

**Completed and approved by channel owner**
- Channel name: **Bharat Mode**; tagline: **Big Ideas. Real Progress.**
- Brand palette: Classic Saffron `#E8752E`, Warm Ivory `#FFF7EB`, Ocean Teal `#117A7A`, Graphite Navy `#283039`, Deep Charcoal `#0B1018`.
- Typography: **Sora** for headlines/display; **Manrope SemiBold** for reading and captions.
- Exact SVG **badge and avatar** are approved source artwork under `public/brand/`; do not redraw or recolor the logo's internal colors.
- YouTube channel-cover design approved; see [CHANNEL_BANNER.md](CHANNEL_BANNER.md). Verify actual YouTube device crops before relying on it.
- **Official Shorts V6 visual/motion template APPROVED on 23 November 2026** after the final bar-centering adjustment. The source of truth is [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md); reusable visual component is [`src/approved-shorts-template.jsx`](../src/approved-shorts-template.jsx).
- **Progress bar perfectly centered** on 1080px canvas: 84px left + 912px bar + 84px right. A regression checker exists at `scripts/test-approved-template.mjs`.
- Approved look: directional character-by-character headline typing **without cursor**; entrances for text, hero and diagrams; raised hero; 0.34s subtle scene dissolve; topic-only pill; flexible chapter segmentation rather than fixed five-step formula; one-line *centered* phrase-group captions with very light, content-sized translucent backing, ~0.2s word pop from 60% to slight overshoot, transient highlight on spoken word; old phrases disappear.
- Earlier browser HTML preview variants under `previews/html/` are retained as design history. **V6 with symmetric progress** is the only current approved visual baseline.
- **Narrator engine selected 23 November 2026:** owner auditioned Qwen3-TTS and prefers its audio to Kokoro. **Approved engine: self-hosted Qwen3-TTS 1.7B VoiceDesign** (Apache-2.0); **no paid TTS subscriptions, metered API charges or voice credits**, and no Indian-accent requirement. Brian is professional-tone inspiration only. The original synthetic reference has been verified and retained privately. Kokoro is a fallback. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) and [`config/voice.json`](../config/voice.json).

**Not yet completed / not approved for publication**
- The `BharatShort` production renderer in `src/short.jsx` is **still a legacy renderer**, not yet fully upgraded to approved V6 motion and per-word aligned captions. Its bar alignment has been fixed.
- No end-to-end **voice-aligned, fully rendered, phone-tested** publishable Short has been verified.
- The **permanent narrator identity is owner-approved** following A/B listening. Full-script pronunciation and delivery, actual word-level alignment, and sound-mix QA remain pending. The old vidIQ Brian and OpenAI TTS production paths are ineligible under the zero-credit requirement.
- Word-level caption timestamps must come from real finalized narration audio (TTS word timestamps or forced alignment), not the manually estimated prototype timings.
- Evidence/rights pipeline, upload-ready sourcing, audio ducking/loudness QA, actual YouTube crop/safe-area QA, and three distinct finished pilots are outstanding.

## Exactly where to resume in the next chat

**NEXT TASK — Produce full PARAM Rudra narration with the approved Qwen3 Base narrator, verify the final speech and run real word alignment.**

The narrator is approved. Synthesize full story WAV(s) from its locked private reference, verify pronunciation and transcript (including PARAM), then run actual WhisperX word alignment on finalized audio. Integrate the alignment and narration into the V6 story renderer with original music/SFX. End-to-end timing, full-script throughput, recurring compute, and phone review are open.

Current implementation tracker: [GitHub issue #5 — voice-synced V6 renderer and first pilot](https://github.com/Mythrow/BharatMode/issues/5).

## Non-negotiable workflow preferences
- **The owner does not want to run code or install tools on their device.** Deliver playable HTML/visual reviews directly in ChatGPT with download links whenever feasible.
- **Qwen3-TTS narrator identity owner-approved on 23 November 2026 after A/B listening.** Owner prefers deep professional delivery; an Indian accent is not required. Self-host with no paid TTS subscription, credits, metered API or silent billing upgrades. Confirm free compute feasibility separately.
- Do not make unnecessary previews after explicit visual approval; make minor fixes in source and report the change.
- Preserve the approved badge, avatar and V6 visual baseline unless the owner explicitly requests changes.
- Keep storyline structure flexible and topic-appropriate. No fixed chapter count, title formula or compulsory length.
- Use reputable primary/public sources where possible; store references, source dates, publication-stage qualifiers and claims evidence in research metadata/descriptions. Never imply speculative illustrations are actual footage.
- **Store** code, docs, storyboard/research metadata, licensed asset references, and original music and SFX masters in GitHub.
- **Do not store** generated speech audio or rendered video files in GitHub. Those can be regenerated and provided to the owner as review/download artifacts.
- User's timezone: Asia/Kolkata. Use absolute dates in handoffs where needed.

## Read these files in this order in a new session
1. **This file**: `docs/PROJECT_STATUS.md` — current stage, approvals, next action.
2. [ROADMAP.md](ROADMAP.md) — project-wide sequence and acceptance milestones.
3. [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) — immutable approved design baseline.
4. [PRODUCTION.md](PRODUCTION.md) — existing production scripts and known limitations.
5. [BRAND.md](BRAND.md), [LOGO_DIRECTION.md](LOGO_DIRECTION.md) and relevant story files as needed.
6. [GitHub issue #5](https://github.com/Mythrow/BharatMode/issues/5) for remaining actionable work.

## Handoff convention after each significant change
Update this file and `docs/ROADMAP.md` with:
- **Done:** exactly what was completed and reviewed; link the source or commit.
- **Approved vs proposed:** explicit approval boundary.
- **Verification:** what actually ran/passed and what remains untested.
- **Next:** single immediate action, followed by optional subsequent tasks.
- **Blocked:** any missing tools, accounts, keys, licensing or data.
- Keep the most current status near the top; do not append contradictory “current draft” fragments endlessly.

## One-message prompt to resume anywhere

> Continue the Bharat Mode YouTube Shorts project from https://github.com/Mythrow/BharatMode. First read `docs/PROJECT_STATUS.md`, then `docs/ROADMAP.md` and `docs/APPROVED_SHORTS_TEMPLATE.md`. Respect the approved V6 design, do not ask me to run code locally, and carry out the next unfinished milestone. Update the GitHub status and documentation after completing work.

**Important:** A new chat does **not** automatically fetch or read this GitHub file just because it exists. The prompt above explicitly points it to the authoritative repository. In the Bharat Mode ChatGPT Project, prior context may help, but check this file for the current state rather than trusting a possibly stale summary.
