# Bharat Mode — current handoff

**Snapshot: 28 November 2026; latest owner release reports 27 November.** Release truth is [registry.json](../content/registry.json), not this dated summary. Refresh it on every new chat. [Generated content log](../content/CONTENT_LOG.md) lists all IDs.

- BM-001 PARAM Rudra, BM-002 ICMR and BM-003 L&T: owner-confirmed public; actual URLs and verified publication dates pending. Do not reopen.
- BM-004 GalaxEye/Bellatrix: owner confirmed live on 27 Nov; public URL and independently verified publication date pending. Historical figure-specific reuse clearance, exact final video approval, music evidence and phone/platform checks remain outstanding. Do not reopen published media.
- BM-005 construction equipment: owner-confirmed upload and 28 Nov 10 AM IST schedule; exact V7/thumbnail acceptance, music evidence and phone/platform checks outstanding. Do not equate schedule with publication.
- BM-006 / ID-009 Chariot-1: owner reports upload on 27 Nov and confirmed schedule for 29 Nov 10 AM IST. Corrected V9 upload draft and title recorded; eight regression tests, native 3214-frame decode and identical AAC verified. Exact-media approval, pronunciation listening, rights/font/phone checks, full validation and final manifest remain outstanding; do not infer QA from upload. [Release page](../publishing/BM-006-release-page.json), [draft evidence](../production/BM-006.draft.json). Registry scheduled (owner reported). Next free production code BM-008; next idea ID-017.
- BM-007 / ID-013: V2 script and V5 storyboard approved; final narration archive received, checksum/script and audio-bound alignments verified (47.52s). Narrated V1 preview complete: 2960 native 1080x1920 60fps frames, continuous PTS, 49.333s, MUSIC-06 ducking, real aligned captions, cue-retimed camera visuals and silent ending. [Preview source](../production/source/BM-007/narrated-v1/), [draft](../production/BM-007.draft.json). Owner preview/listening approval, replacement scene 3 ASR and low-confidence scene 6 word alignment, map/music/font rights, phone and release QA pending.
- **Next owner-facing step:** review BM-007 narrated V1 preview, resolve audio QA flags and outstanding release checks before final export/thumbnail.
- Approved brand, V6 + later refinements, Qwen original narrator and MUSIC-06 B stay unchanged. Home tab deferred until roughly ten published Shorts.
- First analytics snapshot is unequal-age and provisional. Collect comparable 24h/7d Studio data when provided; no sweeping creative changes.

**Technical backlog:** [roadmap](ROADMAP.md) and [issue #5](https://github.com/Mythrow/BharatMode/issues/5). No generic renderer is certified until real-audio native render, decoded motion/phone QA and owner review. Existing private source/review assets: [recovery standard](PRODUCTION_REPRODUCIBILITY.md).

**New-chat reading order:** this page → registry/log → relevant research → content pipeline → approved template/production guide as needed. Historical checkpoint details: [archive](archive/README.md). This summary is not a second status ledger; when stale regenerate it from current evidence.

**Audit record:** PR #6 was merged (previously verified); the repository-backed JavaScript contract tests passed in an isolated harness; GitHub Actions still reports failure with unavailable logs/empty steps. Do not call CI green or the production renderer certified. See [audit record](AUDIT_2026-11-27.md).
