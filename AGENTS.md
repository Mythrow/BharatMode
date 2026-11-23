# Bharat Mode — Assistant / Coding Agent Instructions

**Start by reading [docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md).**
Then read [docs/ROADMAP.md](docs/ROADMAP.md) and [docs/APPROVED_SHORTS_TEMPLATE.md](docs/APPROVED_SHORTS_TEMPLATE.md) *before editing any visual or production sources*.

- **ALWAYS inspect [content/CONTENT_LOG.md](content/CONTENT_LOG.md) and [content/registry.json](content/registry.json) before pitching, selecting or drafting any story.** Search all stages including Published, use the unique `BM-####` ID, and obey [docs/CONTENT_PIPELINE.md](docs/CONTENT_PIPELINE.md). Never register the same news event twice; a genuine new development on the same topic must link its earlier ID and explain the difference. After any intake/edit run `npm run content:check` and `npm run content:test`.
- New story files in `stories/` **MUST include** `story.contentId` matching a registry record and a dedicated research sheet. The legacy `publishing/queue.json` is creative planning, **not** identity/publication history.
- The channel owner approved the V6 Shorts visual system on 23 November 2026, with perfectly centered segmented chapter progress (84px left and right on 1080px canvas).
- The official logo badge and avatar SVG masters in `public/brand/` must not be redrawn or recolored.
- The `BharatShort` generic renderer is older than the approved motion system. Its remaining integration work is tracked in [GitHub issue #5](https://github.com/Mythrow/BharatMode/issues/5).
- Do not assume a new chat has read GitHub or remembered every previous choice. Fetch/read the current status file first.
- The owner prefers interactive HTML or finished artifact previews **in the chat**; do not ask the owner to run scripts on their own device.
- Store source, docs, story metadata, original music and SFX in Git. Do not commit rendered video or generated narration.
- Story-driven, flexible chapter structures; do not impose an identical five-part arc on every Short.
- Keep source fidelity, licensing and status qualifiers explicit. The final visual template AND consistent synthetic Qwen narrator identity are approved; **full-story word-level timestamps, actual production renderer and full MP4 phone QA are not**.
- After completing a meaningful milestone, update `docs/PROJECT_STATUS.md`, `docs/ROADMAP.md`, relevant specifications/tests, and the active GitHub issue as part of the same work.
