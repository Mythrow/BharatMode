# Bharat Mode — Launch milestones

**Latest checkpoint and new-chat resumption:** [PROJECT_STATUS.md](PROJECT_STATUS.md) is the authoritative current-status/handoff file. **Next active milestone:** the owner approved the Qwen3-TTS Base narrator's audible consistency on 23 November 2026; generate full PARAM Rudra narration, verify actual word timing and pronunciation, integrate with locked V6. See [issue #5](https://github.com/Mythrow/BharatMode/issues/5) and [VOICE_DIRECTION.md](VOICE_DIRECTION.md). The V6 visual design is approved, but publishable voiced video production remains unfinished.

**Official palette frozen:** 22 November 2026. See [BRAND.md](BRAND.md). This is the execution sequence, not a promise of unattended publishing.

## Milestone 1 — Brand assets (COMPLETE); actual YouTube crop review remains
- [x] Owner provided final vector badge and avatar; exact source files checked into `public/brand/`.
- [x] Vector avatar supplied in 320×320 viewBox; test actual final upload crop on YouTube.
- [x] Sora for display and Manrope SemiBold for body/captions; brand logo uses owner-outlined SVG artwork.
- [x] Approved icon/avatar and horizontal badge stored in repo; [x] banner approved; [x] source and recommended-size export in Git with SHA verification; [ ] test YouTube mobile/desktop crop; [ ] create motion signature.
- **Acceptance:** logo badge/avatar approved by owner; actual YouTube upload and motion graphics export still to test.

## Milestone 2 — Approved visual template (COMPLETE); three polished pilot Shorts (NEXT)
- [x] Owner approved the V6 visual/motion design with symmetrical chapter progress (84px both sides). Reusable frame in `src/approved-shorts-template.jsx`.
- [x] Owner clarified non-negotiable voice constraint: **free/open-weight, offline-capable, no paid TTS subscription or expiring/renewable voice credits**. Indian accent not required; owner prefers a deep, professional Brian-like tone.
- [x] **Qwen3-TTS selected by owner** after hearing Qwen and Kokoro demos. Use 1.7B VoiceDesign (Apache-2.0); Kokoro is the lightweight fallback, not the active choice.
- [x] Verify official 1.7B VoiceDesign download and offline CPU inference in Work Mode without paid compute or voice credits. Generated the 7.6-second PARAM Rudra WAV with the repository audition inputs and staged float32 inference. A local transcript check recovered all three sentences, with `PARAM` spelled phonetically. The earlier GitHub Actions runner startup failure remains recorded in [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993).
- [x] Independently verify and preserve the **private VoiceDesign WAV reference by checksum and manifest** (`config/narrator-reference.json`); match 7.6 s, 24 kHz, mono PCM16 and SHA-256. Implement `scripts/qwen_reference.py`; five unit tests pass. The WAV is not stored in Git.
- [x] Execute the [Qwen3-TTS 1.7B Base test](WORK_MODE_BASE_RUNBOOK.md) offline in Work Mode using the verified private VoiceDesign reference. Generated an 8.8 s PCM16 WAV. Integrity passed, offline ASR matched all 22 script words, and the reference-to-sample speaker embedding cosine was 0.724.
- [x] **Owner APPROVED narrator identity after comparing both clips by ear** on 23 November 2026. The private original synthetic reference is locked by SHA in `config/narrator-reference.json`; publication-specific audio QA remains open.
- [ ] Verify recurring compute access and full-script synthesis throughput. The short Base test measured 103.5 s total and 7.68 GiB peak process RSS.
- [ ] **NEXT:** generate full PARAM Rudra story WAV(s) from the approved private Qwen Base reference. Check transcript, proper-name pronunciation, runtime and resource usage; only then perform real forced word alignment and V6 integration.
- [x] Implement the free local **WhisperX acoustic-alignment data contract** and V6 real-timestamp caption overlay, with 8 Python + 13 JS assertions passing. [AUDIO_ALIGNMENT.md](AUDIO_ALIGNMENT.md) explains integration. This is code-level validation only, **not successful WhisperX inference**.
- [ ] Execute genuine word alignment on an actual finalized Base-generated WAV, verify transcript/"PARAM" pronunciation and word timing, then wire the overlay into general-story production rendering.
- [ ] Integrate V6 movement, grouped captions and actual word-aligned narration into the general story renderer.
- [ ] Three **distinct narratives**: an invention/how-it-works; an underreported measurable achievement; a person-led or community story.
- At least one ivory, one charcoal and one (short) saffron-feature scene across pilots.
- Dynamic subject-appropriate Remotion composition, captions synchronized to narration, voice generated per production run.
- Only original/rights-cleared music and graphics; do not store voice or rendered video files in Git.
- **Acceptance:** full renders reviewed on mobile, no claim errors, clear sources, readable captions, natural voice mix.

## Milestone 3 — Research-to-production workflow
- Source registry (ISRO, labs, science agencies, research papers, statistical reports, regional reporting).
- Script and source review checklist, accurate stage labels, fact review trail.
- Queue/editorial slate with story scores, human approval and explicit confidence.
- Publishing title/thumbnail rotation checks expanded to actual completed uploads.
- **Acceptance:** at least 10 vetted candidate stories, enough for a first publishable week.

## Milestone 4 — Channel setup and publication
- Verify YouTube handle and trademark situation outside this repo.
- Upload channel avatar/banner, add About description and links.
- Generate upload package: title, first-frame or thumbnail, description with source links, captions and disclosure as relevant.
- **Acceptance:** three polished pilot Shorts approved and ready for scheduling; human controls publication.

## Milestone 5 — Feedback and repeatable cadence
- Review retention curves, swipe/stay, replay and share patterns.
- Review a grid of thumbnails and 5 consecutive videos for visual sameness.
- Refine hook templates and evidence visualizations; don't make rigid repetitive content.
- **Acceptance:** a measured, evidence-led weekly editorial cadence.

## Cross-cutting constraints
- Keep repository source/docs/story briefs/audio masters; **exclude generated voice and video outputs**.
- Protect API keys; no generic slideshows that simply paraphrase public news.
- No unsupported factual claims, generated images passed off as documentary footage, or exaggerated "world first" claims.

## Immediate next production milestone
The Qwen narrator is approved. Next generate full PARAM Rudra story WAV(s), check pronunciation and transcript, run actual word alignment, and integrate the approved V6 renderer. Review one complete evidence-backed Short on a phone, then produce two differently structured pilots. Generated narration and MP4s stay outside Git.
