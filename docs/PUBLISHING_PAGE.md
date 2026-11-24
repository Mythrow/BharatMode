# Bharat Mode — Publishing page standard

Owner requirement, 24 November 2026: deliver every finished Short in one openable HTML publishing page, with copy controls for individual fields and the actual thumbnail and video downloads. This supersedes ZIP as primary delivery; archives may be kept as optional backup.

- Naming: `BM-####-<slug>-publish.html`. Preserve approved canonical MP4 and PNG names.
- Include title, full description including hashtags, separate hashtags, tags, playlist(s), category, language, audience, disclosure, license, visibility, comment settings, sources/caveats, and completion checklist. Individual Copy buttons must copy exact text, with selection/manual fallback when clipboard permission is unavailable.
- Thumbnail preview and PNG/MP4 download controls; embed exact final media for portable offline files, with no external services. Use Blob downloads; do not claim in-chat playback or downloads will necessarily work in sandboxed previews. Deliver plain direct MP4 and PNG links as fallback. Open saved HTML in Chrome/Edge.
- Verify media bytes against approved checksums; no re-encoding. Validate HTML, metadata, JS syntax and embedded media. Browser interaction test when available; distinguish syntax checks from actual browser/account tests.
- Keep page and private rendered media out of Git; save in private Library. Commit reusable generator and non-sensitive metadata, rights/source records and handoff. No automatic publication.

## Implementation

`scripts/create_release_page.py` reads per-episode JSON and approved local video/thumbnail. Example:

```sh
python scripts/create_release_page.py --metadata publishing/BM-0003-release-page.json --video BM-0003-lt-chennai-ai-cluster-order.mp4 --thumbnail BM-0003-lt-chennai-ai-cluster-order-thumbnail.png --output BM-0003-lt-chennai-ai-cluster-order-publish.html
```

BM-0003 page generated, 9,001,075 bytes, SHA-256 `2df1f344f19c9d1d32b96fc5650d71e462a12113a15d28e11401b5c94cc579d2`; private Library `/BharatMode/BM-0003-lt-chennai-ai-cluster-order-publish.html` ID `libfile_186985f055948191840880eb7130c845`. 14 copy controls and 2 media downloads; HTML parsed, JS passed node --check, decoded embedded bytes exactly matched approved PNG and MP4. Interactive browser clipboard/download behavior not independently tested. User may open downloaded page locally. Metadata remains proposed; video and thumbnail approved, no upload. Original ZIP retained as archive.
