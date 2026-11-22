# Bharat Mode — Launch milestones

**Latest checkpoint and new-chat resumption:** [PROJECT_STATUS.md](PROJECT_STATUS.md) is the authoritative current-status/handoff file. **Next active milestone:** narrator **Brian approved** via vidIQ (no Indian accent required; no paid voice subscription). Implement final-audio ingestion, real word-level caption alignment and the approved V6 full story renderer; see [issue #5](https://github.com/Mythrow/BharatMode/issues/5) and [VOICE_DIRECTION.md](VOICE_DIRECTION.md). The V6 visual design is approved, but publishable voiced video production remains unfinished.

**Official palette frozen:** 22 November 2026. See [BRAND.md](BRAND.md). This is the execution sequence, not a promise of unattended publishing.

## Milestone 1 — Brand assets (COMPLETE); actual YouTube crop review remains
- [x] Owner provided final vector badge and avatar; exact source files checked into `public/brand/`.
- [x] Vector avatar supplied in 320×320 viewBox; test actual final upload crop on YouTube.
- [x] Sora for display and Manrope SemiBold for body/captions; brand logo uses owner-outlined SVG artwork.
- [x] Approved icon/avatar and horizontal badge stored in repo; [x] banner approved; [x] source and recommended-size export in Git with SHA verification; [ ] test YouTube mobile/desktop crop; [ ] create motion signature.
- **Acceptance:** logo badge/avatar approved by owner; actual YouTube upload and motion graphics export still to test.

## Milestone 2 — Approved visual template (COMPLETE); three polished pilot Shorts (NEXT)
- [x] Owner approved the V6 visual/motion design with symmetrical chapter progress (84px both sides). Reusable frame in `src/approved-shorts-template.jsx`.
- [x] Narrator identity approved: **Brian** via vidIQ voiceover, voice ID `nPczCjzI2devNBz1zQrb`; no Indian accent requirement and no paid voice subscription at present. Audition generated; voice direction documented in `docs/VOICE_DIRECTION.md` and `config/voice.json`.
- [ ] Confirm commercial rights of the chosen vidIQ-generated audio before publication and check credit limits before any additional generations.
- [ ] Build an audio-import plus final-audio word alignment system for Brian; the current vidIQ integration does **not** return word-level timestamps.
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
V6 visuals and the Brian narrator are now approved. Next: build **Brian audio ingestion + precise word timing + full V6 story renderer** without a paid voice subscription, followed by one complete evidence-backed vertical Short for end-to-end audio/visual review. After the first pilot passes phone QA, create two distinctly structured pilot Shorts. Generated narration and MP4s remain outside Git.
