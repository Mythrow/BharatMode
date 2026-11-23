# Bharat Mode — Assistant / Coding Agent Instructions

**Start by reading [docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md).**
Then read [docs/ROADMAP.md](docs/ROADMAP.md) and [docs/APPROVED_SHORTS_TEMPLATE.md](docs/APPROVED_SHORTS_TEMPLATE.md) *before editing any visual or production sources*.

- **ALWAYS inspect [content/CONTENT_LOG.md](content/CONTENT_LOG.md) and [content/registry.json](content/registry.json) before pitching, selecting or drafting any story.** Search all stages including Published, use the unique `BM-####` ID, and obey [docs/CONTENT_PIPELINE.md](docs/CONTENT_PIPELINE.md). Never register the same news event twice; a genuine new development on the same topic must link its earlier ID and explain the difference. After any intake/edit run `npm run content:check` and `npm run content:test`.
- New story files in `stories/` **MUST include** `story.contentId` matching a registry record and a dedicated research sheet. The legacy `publishing/queue.json` is creative planning, **not** identity/publication history.
- **MUSIC-06 ACTIVE:** owner chose the private 54.99s techno-thriller MP3 and confirmed a paid ElevenLabs Music plan. Current Music Terms allow ordinary monetized YouTube audio synchronization without required paid-tier attribution; precise tier/creation receipt not independently examined. Track remains private, SHA in `config/music.json`; earlier MUSIC-01–05 are superseded. A 20s approved-reference mix demo was generated; actual full BM-0003 narration/mix/V6 QA is pending. Never publish stand-alone music to Git or substitute paid TTS.
- The channel owner approved the V6 Shorts visual system on 23 November 2026, with perfectly centered segmented chapter progress (84px left and right on 1080px canvas).
- The official logo badge and avatar SVG masters in `public/brand/` must not be redrawn or recolored.
- **CURRENT FIRST CONTENT PILOT:** BM-0003 L&T Chennai 23 Nov new order, draft in `stories/lt-chennai-ai-cluster-order.json` and exact [Work Mode runbook](docs/WORK_MODE_BM0003_RUNBOOK.md). Actual scene audio/WhisperX/video do NOT exist yet; user must not be asked to install apps.
- The `BharatShort` generic renderer is older than the approved motion system. Its remaining integration work is tracked in [GitHub issue #5](https://github.com/Mythrow/BharatMode/issues/5).
- Do not assume a new chat has read GitHub or remembered every previous choice. Fetch/read the current status file first.
- The owner prefers interactive HTML or finished artifact previews **in the chat**; do not ask the owner to run scripts on their own device.
- **Audio review delivery preference (owner, 23 November 2026):** Do NOT send standalone downloadable MP3/WAV links as the primary audition experience. Build a **single self-contained, browser-playable HTML review page** with native audio players and embedded user-private sound bytes; link that HTML directly in the conversation. Users should be able to click Play, compare voice/music/ducked/unducked variants and not install/download media files. Use `scripts/build_audio_review_html.py` (agent-run only), keep HTML output in ignored `out/` or private artifact storage, **never commit HTML containing licensed music or private voice**. For music QA include exact fader gains and measured source-separated loudness/RMS, not ambiguous percentages.

- Store source, docs, story metadata, original music and SFX in Git. Do not commit rendered video or generated narration.
- Story-driven, flexible chapter structures; do not impose an identical five-part arc on every Short.
- Keep source fidelity, licensing and status qualifiers explicit. The final visual template AND consistent synthetic Qwen narrator identity are approved; **full-story word-level timestamps, actual production renderer and full MP4 phone QA are not**.
- After completing a meaningful milestone, update `docs/PROJECT_STATUS.md`, `docs/ROADMAP.md`, relevant specifications/tests, and the active GitHub issue as part of the same work.
