# Production reproducibility and recovery

For every new Short, create a versioned structured story brief under stories/ and a per-story production manifest under production/ using [the example](../production/manifest.example.json). Record permanent ID and production code, approved script revision, per-scene measured WAV/alignment, original/adjusted cue map, source-rendered storyboard, unique backgrounds and editable visual source, all assets/provenance/rights/hashes, native render config (tool versions, fonts, encoder flags, fps, resolution, frame counts and silent hold), output hashes, and gate evidence. Commit non-sensitive source/metadata only. Private-only sources containing media must be packaged privately with a checksum and recoverable reference; never include audio, licensed media or MP4 in public Git.

## Recovery in a new chat

1. Read latest registry and matching research/release records. Locate private source bundle/asset by Library ID or exact filename/path recorded in manifest. Use authorized Library/file lookup; do not assume a prior sandbox path exists.
2. Recover the original file bytes to a private workspace, compare SHA-256 with manifest; verify archive paths before extracting (reject traversal). Recover approved narrator reference and MUSIC-06 using config hashes. Obtain exact final scene WAVs, alignments, licensed art and original/adjusted cue maps; verify each against manifest. Do not regenerate an already approved/published episode.
3. Inspect locked tool/font versions and render command, confirm story source and dimensions. Only main production conversation renders video; Work audio-only. Missing private source, hash mismatch, expired/unavailable access, rights gaps or missing fonts are blockers; ask owner to supply the exact asset rather than silently substitute it.
4. For new episodes save editable source bundle and QA report to private Library, record checksum and recovery metadata in manifest, preserve final delivered bytes. Never claim that a Library identifier has been recovered without materialization and hash validation.

## Historical recovery pointers (recorded, not freshly recovered)

- BM-001: ID-001 research records music-fixed source ZIP and exact release media.
- BM-002: ID-002 research and release-page identify private episode artifacts.
- BM-003: ID-003 research, legacy release record and private release ZIP; do not use the old bridge for new renders.
- BM-004: ID-005 research records V6 source bundle, QA and canonical video.
- BM-005: ID-006 research records V7 editable source, exact media, QA and unchanged audio payload.

Legacy structured briefs exist for BM-001–003; BM-004/005 have private source and research pointers but no structured story JSON in Git. Do not reconstruct or mark fully reproducible without recovering actual source/approved scripts and verifying bundle integrity. Never edit the existing rendered videos. The recovery index is evidence of recorded locations, not proof of access.
