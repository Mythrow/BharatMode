# Bharat Mode — Project Status / New-Chat Handoff

**THIS IS THE CANONICAL RESUME POINT.**

Last verified: **23 November 2026**. Work Mode generated the PARAM Rudra Qwen3-TTS audition. Consult Git history for the latest commit. After a task is completed, update this file *in the same commit as the task*, revise the roadmap, and note the actual GitHub commit and any incomplete checks. GitHub is authoritative; old conversation snippets and historical V1–V5 examples are not.

## What the project is
**Bharat Mode** is a research-led, faceless YouTube Shorts channel highlighting verified Indian discoveries, inventions, builders, science, technology and meaningful national progress. Content should find underreported stories without sensationalizing or claiming unsupported "firsts". Voice, evidence and readable vertical animation are core to the product.

Repository: https://github.com/Mythrow/BharatMode

## Current stage — V6 visuals and Qwen3-TTS engine approved; PARAM Rudra voice audition ready

### Verified working reference + Base test preparation — 23 November 2026

- Continuing with the real 7.6-second Qwen3-TTS audition as a **provisional engineering reference**, not a claim of final narrator listening approval. The owner asked to continue development; final audible voice quality and PARAM pronunciation remain to review before publishing.
- The original private Work Mode/Library WAV was materialized in the working environment and independently checked: **24 kHz mono PCM16, 7.600 seconds, SHA-256 `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`**, matching the Work record. The WAV remains **outside public Git**.
- Added `config/narrator-reference.json` with exact audition transcript, model revision and checksum; `scripts/qwen_reference.py` checks the actual private file against the manifest; `scripts/qwen_base_voice_test.py` implements Qwen3-TTS Base synthetic-reference reuse via official `create_voice_clone_prompt` / `generate_voice_clone` APIs, outputting an ignored new-line WAV for comparison.
- Verified the reference validator against the **real WAV**, and ran five synthetic unit tests (valid case and four rejection cases); `qwen_base_voice_test.py` was syntax/CLI checked but **the Base 1.7B model was not executed** in this session (no model weights or adequate available compute here).
- **Next engineering execution:** run Qwen3-TTS Base on a suitable Work Mode cloud computer using the private reference, review voice similarity and new-line pronunciation, then proceed with real word alignment and V6 production integration. No local user setup or paid TTS provider.


### Verified Qwen3-TTS Work Mode audition — 23 November 2026

- Downloaded the official 1.7B VoiceDesign weights and speech tokenizer, verified their SHA-256 hashes, and ran inference from local files with Hugging Face offline mode on a CPU-only Work Mode workspace (9.7 GiB reported RAM). No paid compute, metered voice API, subscription, or voice credits were used.
- Fed the voice prompt from [config/voice.json](../config/voice.json) and the exact PARAM Rudra audition text from [the smoke script](../scripts/qwen-voice-design-smoke.py). Verified a 7.6-second, 24 kHz mono PCM WAV. The owner can play the sample in the Work Mode conversation. The WAV is kept outside Git.
- **Next: owner listens to the audition.** If approved, retain the original synthetic reference and exact transcript privately, then verify Qwen3-TTS 1.7B Base can reproduce that voice on new lines. This test covers one short audition. Recurring compute access, full-script throughput, pronunciation review, reference consistency, and production integration are pending.
- Earlier GitHub Actions [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) still records a separate runner startup failure before any step. Work Mode testing used the repository smoke script with a pinned local snapshot, a fixed seed, and staged float32 processing. The all-float32 attempt was killed under memory pressure and an INT8 sample failed the transcript check. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) for settings and timings.

### Caption alignment engineering checkpoint — 23 November 2026

- Built `scripts/align_qwen_words.py` to use a locally installed open-source WhisperX forced aligner on **real finalized narration WAVs**, writing checksum-linked word starts and ends. It rejects missing words, invented words, overlapping/invalid times, and transcript mismatches rather than estimating word times.
- Built `src/aligned-caption-timing.js` and `src/aligned-captions.jsx` as an **optional** centered word-synced V6 caption overlay. Group timing comes exclusively from a `final-audio-acoustic-alignment` file, never the old simulated demo timings. The approved V6 frame, layout and legacy story renderer were **not changed**.
- **Tests actually executed here:** eight Python alignment-contract tests, thirteen JS assertions, real reference-WAV header/hash check. All passed. Tests do **not** exercise WhisperX inference or Qwen Base.
- **Still pending:** run Qwen3-TTS Base on eligible Work Mode compute to verify voice consistency; run WhisperX on the *newly generated Base WAV*; review actual word timing, narrator pronunciation, and render with V6; human publication QA remains required. See [AUDIO_ALIGNMENT.md](AUDIO_ALIGNMENT.md).

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
- **Narrator engine selected 23 November 2026:** owner auditioned Qwen3-TTS and prefers its audio to Kokoro. **Approved engine: self-hosted Qwen3-TTS 1.7B VoiceDesign** (Apache-2.0); **no paid TTS subscriptions, metered API charges or voice credits**, and no Indian-accent requirement. Brian is professional-tone inspiration only. **Exact reusable narrator reference audio is NOT saved yet**; Kokoro is a fallback. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) and [`config/voice.json`](../config/voice.json).

**Not yet completed / not approved for publication**
- The `BharatShort` production renderer in `src/short.jsx` is **still a legacy renderer**, not yet fully upgraded to approved V6 motion and per-word aligned captions. Its bar alignment has been fixed.
- No end-to-end **voice-aligned, fully rendered, phone-tested** publishable Short has been verified.
- The **PARAM Rudra synthetic-voice audition is ready for owner review**. A reusable final narrator reference, full-script pronunciation and delivery, word-level alignment, and sound-mix QA are pending. The old vidIQ Brian and OpenAI TTS production paths are ineligible under the zero-credit requirement.
- Word-level caption timestamps must come from real finalized narration audio (TTS word timestamps or forced alignment), not the manually estimated prototype timings.
- Evidence/rights pipeline, upload-ready sourcing, audio ducking/loudness QA, actual YouTube crop/safe-area QA, and three distinct finished pilots are outstanding.

## Exactly where to resume in the next chat

**NEXT TASK — Execute and review Qwen3-TTS Base voice-consistency audition using the verified reference WAV.**

1. Original Qwen VoiceDesign reference is **verified** and tracked by hash/metadata in `config/narrator-reference.json`; the WAV itself is private and outside Git. **Final audible narrator approval and PARAM pronunciation check remain pending.**
2. On a capable Work Mode cloud computer, use `scripts/qwen_reference.py` to verify the private WAV, then `scripts/qwen_base_voice_test.py` with official Qwen 1.7B Base weights to generate **new, different lines** using that exact reference. Review whether voice quality/identity carries over and capture timing/memory usage. Base inference is not yet verified.
3. If the Base voice is consistent, implement repeatable narration from actual story text, phonetic pronunciation QA and **forced word-level alignment** into the locked V6 caption system. Do not treat synthetic or estimated word timestamps as real speech timing.
4. Integrate with `src/short.jsx` (currently legacy), original music/SFX and phone-safe layout; fact-check and phone-review one publishable Short before two other pilots. Never use paid voice APIs, credits or unapproved computing fees.

**Completed this checkpoint:** verified the actual privately stored VoiceDesign WAV, committed immutable reference metadata, implemented SHA/audio verification and a Qwen Base generation experiment. **Verified tests:** five reference unit tests and sample/manifest match. **Not completed:** Qwen Base inference, final narrator approval, alignment, V6 story integration, MP4 or phone QA.

Current implementation tracker: [GitHub issue #5 — voice-synced V6 renderer and first pilot](https://github.com/Mythrow/BharatMode/issues/5).

## Non-negotiable workflow preferences
- **The owner does not want to run code or install tools on their device.** Deliver playable HTML/visual reviews directly in ChatGPT with download links whenever feasible.
- **Qwen3-TTS engine approved, exact narrator reference pending.** Owner prefers deep professional delivery; an Indian accent is not required. Self-host with no paid TTS subscription, credits, metered API or silent billing upgrades. Confirm free compute feasibility separately.
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
