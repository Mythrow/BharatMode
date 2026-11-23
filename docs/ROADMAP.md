# Bharat Mode — Launch milestones

**Latest checkpoint and new-chat resumption:** [PROJECT_STATUS.md](PROJECT_STATUS.md) is the authoritative current-status/handoff file. **Next active milestone:** owner approved **Qwen3-TTS** after listening comparison; use open-weight `Qwen3-TTS-12Hz-1.7B-VoiceDesign` to create an original reusable synthetic voice reference, then self-host the narration + word alignment + V6 renderer with no paid subscriptions or voice credits. See [issue #5](https://github.com/Mythrow/BharatMode/issues/5) and [VOICE_DIRECTION.md](VOICE_DIRECTION.md). The V6 visual design is approved, but publishable voiced video production remains unfinished.

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
- [ ] Capture and approve an original **reusable Qwen3 voice reference**, then lock its prompt, reference transcript, private audio location and model revision. No exact sample is yet saved; do not clone Brian.
- [ ] Verify suitable permitted remote compute for Qwen 1.7B without introducing unapproved charges. The owner will not install or run software locally.
- [ ] **BLOCKED — GitHub runner/startup failed:** Qwen3-TTS VoiceDesign CPU smoke test was committed, but [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) failed twice **before any setup or inference steps**, with no logs/artifacts. Check Actions execution/runner availability or choose another permitted execution environment. No real Qwen audio was generated.
- [ ] Build self-hosted Qwen speech generation + genuine final-audio word alignment; avoid paid and metered speech APIs.
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
V6 visuals and **Qwen3-TTS engine** are approved; permanent narrator reference still requires capture and validation. Next: establish a reusable **Qwen-designed original voice**, then build **unmetered self-hosted speech generation + precise word timing + full V6 story renderer**, followed by one complete evidence-backed vertical Short for end-to-end audio/visual review. After the first pilot passes phone QA, create two distinctly structured pilot Shorts. Generated narration and MP4s remain outside Git.
