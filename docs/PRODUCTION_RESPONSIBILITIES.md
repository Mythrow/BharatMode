> **Approved map pipeline:** Natural Earth 1:10m country/state/city geographic data + reusable Remotion map component, with actual in-chat video renders (OpenCV/FFmpeg acceptable for iterative bridges). [MAP_DIRECTION.md](MAP_DIRECTION.md). Work must not generate map animations or MP4s.
# Bharat Mode — Responsibility Boundary: AUDIO ONLY in Work, VIDEO HERE

**Owner instruction (23 November 2026):** Work Mode must **only generate and validate narration/audio assets**. All image sourcing/graphics, motion, editing, music placement, composition, video encoding and MP4 rendering must be performed **in the main ChatGPT production conversation**. Never delegate video production to Work, even when a runbook or old issue says otherwise. This owner instruction overrides earlier broad production handoffs.

## Work Mode — allowed (audio-only)

- Load the pinned official `Qwen3-TTS-12Hz-1.7B-Base` model and verify the approved private synthetic voice reference against its SHA-256.
- Generate each actual scene narration as its own private PCM WAV. Verify encoding, spoken transcript and proper names independently; correct/regenerate only incorrect speech with the same speaker reference.
- Align finalized speech with a real acoustic alignment pass (WhisperX); export **exact per-scene word timing JSON** with the voice WAV metadata/hash, scene ID and transcript. Optionally export an audio-only stitched narration WAV with boundary spacing and an audio integrity manifest.
- Provide **audio-only private files** (six scene WAVs, six alignment JSONs, transcript QA and checksums). Work must not touch V6 styling, design, video frames, captions rendering or music/video assembly. No MP4 or video output from Work.
- Update only voice/audio status in GitHub, and note that final visual publishing/review work happens elsewhere.

## Main ChatGPT production conversation — video owner

- Read the content registry, fact ledger, script, locked V6 layout and approved music configuration. Use licensed imagery and original dynamic visualizations; graphical illustration must be unmistakably illustrative rather than impersonating the real site or completed infrastructure.
- Retrieve Work's **audio-only** outputs/alignments. Render the V6 frame and actual timed captions **here** with a capable local CPU/container/browser renderer, or equivalent in-conversation tools. Music follows approved MUSIC-06 Option B: narrator **88/100**, score **55/100 between words** and **32/100 under narration**.
- Compose all animations, story diagrams, original/sourced footage, scene changes and final 1080×1920 H.264/AAC MP4 in the current chat's execution environment. Verify visual quality using extracted frame contact sheets and review on mobile before publication.
- Deliver the actual MP4 and an optional self-contained **browser-playable HTML review page** directly in the main conversation. Do not require the owner to install editing software. Do not publish automatically.
- Keep editable rendering source in Git; generated private narration, soundtrack, licensed-only media and MP4 binaries remain **outside public Git**.

## BM-0003 visual revision after owner review (23 Nov)

The first Work-made 41.50-second pilot was technically valid but visually **too text-heavy**: one reusable static evidence card for nearly every scene. The owner rejected that visual direction and corrected Work scope.

A new **in-conversation video revision** was rendered using `scripts/render_bm0003_visual_upgrade.py` and the existing private review MP4 as **temporary base media**. It replaces the card portion with six animated, **original CGI schematic** visuals: server-rack corridor perspective, Chennai NVIDIA B300 deployment visualization, large-order value range with server architecture, planned GPU matrix, planned-vs-unconfirmed operational status, and connected compute ecosystem. It **does not represent real Chennai footage**. The approved V6 headline/typewriter/captions/brand/centered progress were left intact by compositing only into the central visual region.

- **Original technical base:** `BM-0003-review.mp4` (Work's **historical** 41.50-second audio+frame cut, SHA-256 `537d2feeac41f15516a8e0d0f99ea3332495708db0254244e14aea7ee0080b89`).
- **Revised video produced here:** `BM-0003-visual-upgrade.mp4`, **41.50 s**, 1080×1920, 30 fps, H.264/AAC, **1245 frames**, SHA-256 `6e4018988a67254b3db2273309c69dea5830c40be992489e37176b3a81448290`.
- **Exact unchanged embedded audio stream:** SHA-256 `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` in both old and new MP4s. This includes approved narration + MUSIC-06 Option B. Voice audio was not regenerated.
- **Review:** a private, browser-playable HTML page with video embedded and six scene jump points was generated in chat. The licensed/private MP4 and HTML are not in Git.
- **Limitations:** The current revision is CGI rather than photographic b-roll, and it is a **review candidate**, not a final owner-approved visual or phone-QA/published Short. It uses the prior Work MP4 as a bridge because Work returned a finished file in this historical run; **future tasks must provide audio only**, and the main chat must build V6 videos directly from the scene WAVs/alignments. For future narratives, do not rely on Work-generated video as an input.

### Repeat the in-chat visual upgrade (agent-run, not user-side task)

```bash
python scripts/render_bm0003_visual_upgrade.py \
  --input out/BM-0003-review.mp4 \
  --out out/BM-0003-visual-upgrade.mp4
```

Uses Python, OpenCV, NumPy, Pillow and FFmpeg. `--check` writes six stills + a visual contact sheet for QA. The current bridge script changes only the selected evidence region and stream-copies audio; it does **not** generate a video from audio alone. Future complete video rendering from audio must also happen in this chat, adapting V6's `src/approved-shorts-template.jsx` and caption timing as necessary.

## Approval gates

**Narrator identity:** approved. **MUSIC-06 + Option B:** approved. **V6 visual template:** approved. **BM-0003 visual revision 2:** awaiting user review. **Public upload:** not approved. Do not mark BM-0003 Published.
