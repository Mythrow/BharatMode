# BM-006 V2 narrated review — 27 November 2026

Owner feedback: scene 4 text crowded graphics; check scene 6; remove internal reference annotations; remaining storyboard acceptable subject to these corrections. V2 review is not final owner approval.

- Original source SHA-256 801c4fe8874bc12bf1dd0cc9db6db946a568a70bdb161e363a40ed43b75e7609 verified. Revised editable source: [preview-v2](source/BM-006/preview-v2/), commit a94c1ec0bb936c6eb0580901d4ae3c2912179d68.
- Private V2 source ZIP: libfile_0309e35ba6188191955121d6d6616375, SHA-256 95ef78296fbf0276f0f81a05d278242d8da333bf9e4a93d6a1eeee8fd70ab41c.
- Recovered Work narration: libfile_01a2dcaf77348191bcc33631776e10c8, SHA-256 457110c824f7a3592c382ab1bc806a16f4568de13ffee89b080dfc9348431576. All package checksums, six WAV formats and final-audio alignment hashes, exact scripts and timestamp bounds verified. Work reports reference verification, independent ASR and WhisperX; listening pronunciation QA remains outstanding.
- Narration durations: 9.2, 8.4, 9.92, 7.52, 8.48, 8.24 seconds; total 51.76. MUSIC-06 hash verified, Option B mix, 0.8s resolve and planned 1.0067s silent hold. Decoded last 0.918s peak zero.
- Full V2 private review MP4: libfile_f596b1a51c08819198b524dc2eb8e716, SHA-256 15cf79a27b6e24f7ea1aaf8bc1f7281a4d9c1cfbcdfeb69445c9911162a0da13. Native 1080x1920 60fps, 3214 frames, 53.566667s; all six segments completed with expected frame counts, consecutive video PTS, full decode passed. Checked decoded affected scenes. Five targeted label/clearance regression tests passed. Inter/Noto fallback as in V1; full font/rights, motion and phone QA, listening review, owner final render/thumbnail and release authorization remain pending.
- Excerpt Scenes 4–6: libfile_90ada0ca784881919028dcbeb6b8892f, SHA-256 927644dbc5c714fa2e5d64165a9a63c61970266311754cc9386a0eaf8d866535.
- Root cause: explicit Scene 5 helper label in hero source, not captions. Removed and added full-string guard before typewriter slicing; authoritative visual standard updated 9a51678734728a3048730d21ba02084cd2bb6c03. Preserve factual qualifiers. Do not treat review as release manifest; registry stays in_progress.
