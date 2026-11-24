> **Latest visual direction (24 Nov 2026):** BM-0003 V4 open-canvas motion review rendered here, replacing static boxed heroes with independently animated graphics and moving backgrounds. Original voice/music unchanged; owner review pending. [Details and permanent visual rules](OPEN_MOTION_DIRECTION.md).

### Revision 3 review delivery recovered — 24 November 2026

- The previous V3 encoded file was unavailable, so the main chat **reproduced** the V3 map/identity/camera revision from checksum-verified V2 (SHA-256 `6e4018988a67254b3db2273309c69dea5830c40be992489e37176b3a81448290`), committed Natural Earth geometry and the V3 rendering logic, including the documented L&T/NVIDIA marks. No Work video task and no new narration.
- New private output: `BM-0003-naturalearth-v3-rebuilt.mp4`. SHA-256 `60048b3db32c6e239d7dbbd4e1c32c8329088d662f835a2ff92c8865076f93a4`; **this is a fresh encode, not byte-identical to the earlier V3 video**. H.264/AAC, 1080×1920, 30fps, 1245 frames, 41.5s. Full decode passed. Natural Earth Chennai point lies within the stored Tamil Nadu polygon; inspected representative map frames.
- Audio codec-stream SHA-256 `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` matches the original/V2/V3 record. Qwen voice and MUSIC-06 Option B unchanged.
- **Both actual review files now saved privately in ChatGPT Library /BharatMode/**: the rebuilt MP4 and self-contained `BM-0003-naturalearth-v3-review.html` with embedded video and six scene controls. Verified embedded bytes equal the rebuilt MP4. Delivered in chat. Neither file is committed to Git.
- **Next: owner visual review, then phone QA.** Do not reopen audio or map-tool approval. No publishing.

> **NEW MAP APPROVAL / VIDEO CHECKPOINT (23 Nov 2026):** Natural Earth 10m + Remotion selected for repeatable cinematic map geography (India POV, Tamil Nadu states, Chennai city center). [Map specification](MAP_DIRECTION.md) · [geo data](../data/maps/naturalearth-bm0003.json) · [Remotion reusable map](../src/natural-earth-map.jsx). In this chat, Python/FFmpeg produced V3 full 41.5s MP4 (same original audio). **Owner visual review pending, not published.** Work remains AUDIO ONLY.
# Bharat Mode — Launch milestones

**BM-0003 review checkpoint:** Six Qwen Base scenes, independent ASR, real WhisperX captions, and the MUSIC-06 Option B mix are in the private 41.50-second V6 pilot. Owner phone review and publication sign-off remain open.

**Latest checkpoint and new-chat resumption:** [PROJECT_STATUS.md](PROJECT_STATUS.md) is the authoritative current-status/handoff file. **Owner clarified: Work may ONLY produce Qwen WAVs, audio verification and true alignment; this ChatGPT conversation must make all videos**. See [Production Responsibilities](PRODUCTION_RESPONSIBILITIES.md). Earlier Work rendering was an error. BM-0003 CGI-enhanced 41.5-second in-chat video revision is ready for owner review, not published.  **Next active milestone:** BM-0003 L&T script drafted and owner-selected paid-tier MUSIC-06 mix demo created; generate and validate actual BM-0003 Qwen Base narration, real word alignment and locked V6 review MP4. See [issue #5](https://github.com/Mythrow/BharatMode/issues/5) and [VOICE_DIRECTION.md](VOICE_DIRECTION.md). The V6 visual design is approved, but publishable voiced video production remains unfinished.

**Official palette frozen:** 22 November 2026. See [BRAND.md](BRAND.md). This is the execution sequence, not a promise of unattended publishing.

## Milestone 1 — Brand assets (COMPLETE); actual YouTube crop review remains
- [x] Owner provided final vector badge and avatar; exact source files checked into `public/brand/`.
- [x] Vector avatar supplied in 320×320 viewBox; test actual final upload crop on YouTube.
- [x] Sora for display and Manrope SemiBold for body/captions; brand logo uses owner-outlined SVG artwork.
- [x] Approved icon/avatar and horizontal badge stored in repo; [x] banner approved; [x] source and recommended-size export in Git with SHA verification; [ ] test YouTube mobile/desktop crop; [ ] create motion signature.
- **Acceptance:** logo badge/avatar approved by owner; actual YouTube upload and motion graphics export still to test.

## Milestone 2 — V6 visuals and narrator approved; BM-0003 animated visual revision 2 produced here, approval pending

- [x] **Fix production ownership:** Work Mode **audio-only**; main chat owns visual creation, film editing and final MP4. Updated [production responsibilities](PRODUCTION_RESPONSIBILITIES.md) and Work audio runbook; do not delegate video rendering to Work again.
- [x] Review the first BM-0003 video and identify the core weakness: repeated static evidence cards and too much typography; the owner wants significantly more compelling visual storytelling.
- [x] **Create full in-chat revision 2** with six original animated story-specific CGI schematic hero sequences, unchanged locked V6 headline/captions/logo/centered progress and unchanged audio stream. 41.5sec 1080×1920, H.264/AAC; verified frame count and matching audio SHA-256; self-contained video HTML review in chat.
- [ ] **NEXT:** owner reviews revision 2 for visual engagement, then iterate if needed. Confirm on actual phone, check licensing/documentation and approve final pilot before any upload. CGI illustrates the concept, **not real L&T facility footage**.


- [x] Respond to owner audio-level feedback with **MUSIC-06 20s A/B/C louder mix test** in one privately linked self-contained HTML file with embedded playback and moving 0–100 fader meters. Reproducible generator in `scripts/generate_music06_level_comparison.py`; verified source SHAs, tested no clipping and exact regeneration.
- [x] **OWNER APPROVED Option B, 23 November 2026:** Qwen narrator **88/100**, MUSIC-06 **55/100 between speech**, **32/100 beneath speech**, with 24ms attack / 280ms release. Reference faders frozen in [config/music.json](../config/music.json) and reused by demo mixer. No need for further mix-selection auditions; actual BM-0003 story/full video mixing and phone QA remain open.



- [x] Owner confirmed MUSIC-06 was generated on a **paid ElevenLabs Music plan**; confirmed [9 Oct 2026 Music Terms](https://elevenlabs.io/music-terms) allow ordinary commercial YouTube-video music synchronization without paid-tier attribution. Exact account tier/receipt not independently inspected.
- [x] Actually created 20s **MUSIC-06 + approved synthetic Qwen voice** mix with automated ducking and verified source SHA checks; no clipping. Historical reference speech only, not BM-0003 narration.
- [x] Drafted source-checked **BM-0003 six-scene story** (~48s provisional), linked research, permanent content registry, editorial queue, and separate Qwen generation plan. **Six offline production tests passed**.
- [ ] **NEXT:** execute genuine full BM-0003 Qwen Base narration on free Work Mode CPU, independently validate spoken words, run actual WhisperX forced alignment, integrate owner-approved V6 with licensed music and create first phone-testable MP4. [Runbook](WORK_MODE_BM0003_RUNBOOK.md).


- [x] Owner selected supplied **MUSIC-06 Techno Thriller** as the signature background track. Private original MP3 is in ChatGPT Library with SHA-256 recorded in [config/music.json](../config/music.json); no public Git media upload.
- [x] Define reuse rule: same main sound for first 5–10 videos with varied cue excerpts/edits and narration ducking; later related variants to avoid identical repeated playback.
- [x] Owner reported a paid ElevenLabs Music plan and ordinary YouTube audiovisual media rights/no paid-tier attribution were verified against current terms; 20s music-and-approved-Qwen narrator mix test generated. **Story narration, complete video and phone/rights final QA remain pending.**


- [x] Generate **three original music auditions** and 20-second narrator-mixed comparisons without paid services or third-party music samples. [Music & sonic identity decisions](MUSIC_DIRECTION.md): MUSIC-01 Quiet Momentum, MUSIC-02 Curious Discovery, MUSIC-03 Built Forward. Procedural generator committed; audio demos remain outside Git.
- [x] Record owner feedback: MUSIC-01 rejected as boring/simple; MUSIC-03 beat and MUSIC-02 melody preferred; new requirement is **lo-fi beats** combining both.
- [x] Create **MUSIC-04 Lo-Fi Motion**, an original 92 BPM / 31.3-second swung beat with Rhodes melody and a Qwen-narrator-mixed audition, plus reproduction source and checksums. Both WAVs pass audio integrity checks; no paid services or samples.
- [x] Owner rejected MUSIC-04's hip-hop rhythm; new brief: **modern melodic techno with deep basslines and low/mid melody, not high keys**.
- [x] Created original **MUSIC-05 Deep Current** (30.968 s, 124 BPM, F-minor four-on-the-floor, rolling bass) and a ducked comparison with the approved Qwen narrator. Both WAVs generated without paid services, clip checks passed; [music direction + source](MUSIC_DIRECTION.md).
- [x] **Superseded:** owner instead selected the separate MUSIC-06 dark techno-thriller master. Do not ask for another MUSIC-05 review.
- [ ] Arrange the selected music into complete script-length/loop-ready variants; finalize subtle transitions/`Mode: ON` identity sound and mix narrator-first. Test levels and mobile playback; only then replace starter `public/music/ambient.wav` and provisional SFX, preserving source and rights.

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

- [x] **Permanent content tracker live**: [Content Log](../content/CONTENT_LOG.md) + source registry + four linked research sheets. Unique `BM-####` IDs; strict **Idea → In Progress → Published**, never recycle or delete IDs.
- [x] Intake and duplicate guard CLI, stage-history validation, published YouTube URL/date/owner approval gates, 14 passing local tests and CI integration. Daily discovery must search the registry before proposing another story.
- [x] **23 Nov L&T Chennai AI/B300 additional order selected as `BM-0003` / In Progress** for trial video; factual event/source context in [BM-0003 research](../content/research/BM-0003.md).
- [x] **BM-0003 storyboard drafted and sources reconfirmed**, six scenes/~48s provisional. Order's value is a **company-defined band** and 10,000 GPUs are a **previously planned cluster**, not verified live equipment. [Script](../stories/lt-chennai-ai-cluster-order.json).
- [ ] Generate actual Qwen Base narration per scene, run independent ASR/WhisperX, add V6 word captions/music and phone-review a full Short.

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
The Qwen narrator and MUSIC-06 signature score are approved selections. First complete **BM-0003** L&T story WAVs, check words and source qualifications, run real alignment, and integrate the locked V6 renderer. PARAM Rudra remains a separate later pilot. Review one complete evidence-backed Short on a phone, then produce two differently structured pilots. Generated narration and MP4s stay outside Git.
