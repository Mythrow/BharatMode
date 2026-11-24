# Bharat Mode — Project Status / New-Chat Handoff

> **MANDATORY — independent graphic and text motion; owner correction 24 November 2026:** Never flatten the main artwork, labels and statistics into one animated rectangle or move a complete static hero as a substitute for motion design. Build meaningful separate layers: every story text element (headline, kicker, value, callout, label, supporting text) has its own eased entrance/reveal; fixed brand avatar/topic pill are intentional chrome exceptions. Chart bars/lines grow progressively, numeric quantities count toward verified end values, modules/tiles assemble or stagger in, paths draw/connect sequentially and nodes appear with appropriate timing. Continue subtle contextual motion with travelling light pulses, illuminated LEDs, circuit traces or other relevant effects after reveal; avoid flashing, unnecessary ornament or obscuring text. Keep distinct contextual backgrounds, 60fps motion, V6 captions and quiet transitions. Before owner review inspect native decoded frames during reveal, after reveal and near transitions for each scene, including full glyph bounds, artwork/text clipping, safe margins, actual within-hero movement (not merely background or progress bars) and settled end values. Fix clipping at source; do not mask over pixels or defer a known visible defect to the next review.

> **MANDATORY — distinct scene backgrounds, owner correction 24 November 2026:** Each narrative scene must have a visibly different story-specific background composition and contextual motion, not a common decorative base with a changed color, gradient, glow or repeated curve. Theme colors may repeat; the artwork, geometry, depth and movement must change to support the content. A continued beat inside the same scene may retain its environment for continuity. V6 locks the branding/chrome (logo, topic pill, typography, captions and centered chapter progress), not background artwork. Before storyboard delivery, assign a unique scene-level background design ID and show actual native-resolution frames; audit the contact sheet for repeated geometry, not just palette, and verify distinct scene background layers in editable source. Before draft delivery, inspect representative rendered frames and within-scene background motion at native 60fps. If this gate fails, correct the source and regenerate before review. Do not reintroduce the prototype V6 radial glow + ellipse as a universal background. Do not include editorial reference labels.

> **MANDATORY on-screen text rule — owner instruction, 24 November 2026:** Do not add source/reference/editorial meta labels in video frames, storyboards, title cards or hero graphics. Remove phrases such as “Illustrative server architecture,” “Government-reported snapshot,” “Mission-wide figures,” “Source: ...,” report citations, internal evidence labels and production notes. Keep references, provenance, explanatory context and asset-rights notes in the research record and YouTube description. Preserve material factual qualifiers directly in normal story content (e.g. date of measured data, ordered versus deployed, under manufacture, National Supercomputing Mission versus PARAM Rudra) whenever omitting them would mislead. Use clearly schematic artwork rather than simulated real facility footage; where an illustration or synthetic media disclosure is necessary to avoid misleading the audience, use appropriate disclosure, not a generic on-screen reference line. Apply this during storyboard generation and visual QA before rendering. No change to approved V6 chrome, captions or progress bars.

> **MANDATORY storyboard review format — owner instruction, 24 November 2026:** Stage 03 means actual rendered native 1080×1920 still compositions from the proposed production visual source, not prose, text-only tables, generic imagery or approximate mood boards. Show a chronological filmstrip/contact sheet of full frames approximately every five seconds, plus any materially different visual state or scene otherwise missed; label time/scene outside the image. Provide a clickable expandable frame viewer with horizontal thumbnails and previous/next navigation (in-chat when supported, self-contained HTML and direct full-resolution PNG links as fallback). Show actual headline, hero, theme, artwork, labels, logo, caption backing/current-word treatment and progress; mark provisional word timing and any font/asset fallbacks. Retain editable frame/scene sources for the subsequent video and revise those compositions based on owner feedback. Only after storyboard approval animate the same visual layers, add V6 transitions, real acoustic alignment/captions and approved audio, and produce a draft MP4. Do not substitute a written plan for this gate or claim a final video has already been rendered. No spoken Bharat Mode closing for BM-001; visual branding remains.

> **LATEST — dual numbering, owner decision 24 Nov 2026:** All ideas receive a permanent sequential `ID-###` first. Assign a separate `BM-###` production code only on owner selection, using the lowest unused positive number; never recycle an assigned number. Keep a single registry record with both codes, use idea ID for research and production code for new video deliverables. ID-001 / BM-001 PARAM Rudra is selected, at Stage 01 story review. ID-002 ICMR and ID-004 IIT Madras are unselected ideas. ID-003 / BM-003 L&T is owner-confirmed published, URL/date pending; preserve historical BM-0003 files and references without re-rendering. BM-002 is next, then skip BM-003 to BM-004; ID-005 is next idea. Earlier BM-#### identifiers below are legacy references, not new allocations. The story → script → visual storyboard → draft render approval order remains mandatory. `content/registry.json` schema v2 is authoritative; `id` is idea identity, `productionCode` is null until selected, and `legacyId` is read-only historical alias. Use `npm run content:move -- ID-005 in_progress --note "Owner selected story"` for a real selected ID; the allocator assigns its code automatically. No automatic publication.


> **MANDATORY — owner workflow, 24 November 2026:** Every new Short starts with the actual verified news/story content and original sources → owner review → complete narration script → owner review → visual scene-by-scene storyboard preview → owner review → actual draft MP4 render for feedback. Do not skip or combine these stages unless explicitly requested by the owner. Final QA, publishing dashboard, publication authorization and calendar reconciliation follow draft approval. Work remains audio-only; V6 and 24px caption corrections remain approved. The next owner-facing action is the news/story itself, not renderer implementation. See [mandatory owner review sequence](CONTENT_PIPELINE.md#mandatory-owner-review-sequence--24-november-2026).


> **Owner update — 24 November 2026:** Caption backing corner radius is **24px** (supersedes 32px); all no-shadow/no-blur, native resolution and direct-alignment requirements remain. The owner requests a refreshed HTML content calendar whenever asked; see [CONTENT_CALENDAR.md](CONTENT_CALENDAR.md). Calendar reflects real publication history, current production, future ideas and explicit schedules only. BM-0003 appears as owner-confirmed published with URL/date pending; no fictitious release dates.


> **LATEST — owner-confirmed publication and next-video refinements (24 November 2026):** Owner says BM-0003 is published and looks good; actual public URL and exact publication date still need to be supplied, so formal registry promotion awaits the real link (no invented ID). Do not re-render/reupload this episode or put it back into production. Owner explicitly approved the in-chat dashboard format for every final render. [Caption and native-resolution QA](POST_LAUNCH_VISUAL_QA.md) is mandatory for future videos: draw fresh captions from real alignment over new scenes, neutral translucent 24px rounded backing, no box/text shadow or backdrop blur; native 1080×1920 minimum for every layer at 60fps, higher-quality encode and real 100% pixel/phone QA. No legacy crop-copy bridge or 540×960 upscaling. V6 layout/motion, narrator, music, thumbnail and naming remain approved. Next: finish native all-layer production pipeline and test on the next distinct story. Historical unpublished/pending-review notes below are superseded by owner publication confirmation, subject to URL reconciliation.


> **CURRENT — owner-approved chat-first publishing delivery (24 Nov 2026):** The standalone HTML file opens as source text in the ChatGPT attachment preview on the owner's client. Deliver the publishing dashboard directly in the chat as the primary interface: actual thumbnail preview; plain direct downloadable approved MP4 and PNG links; exact per-field copy controls for title, full description including hashtags, hashtags, tags, playlist, upload settings, and sources; interactive local checklist initialized from verified release state. Do not depend on HTML execution, video playback or embedded media download buttons. If preview/copy controls are unsupported, provide plain text and direct file links. Checklist interaction is local UI state, not proof of publication or a registry update. Keep self-contained HTML and ZIP as optional offline backups only; no external hosting or paid services needed. Reuse the per-story release-page JSON as canonical publishing metadata. BM-0003 remains creatively approved, metadata proposed, and unpublished pending owner authorization and final checks. Frozen V6 and audio-only Work scope unchanged.


> **CURRENT — channel setup / publishing page (24 Nov 2026):** Owner confirmed all ten playlists created; [channel description, playlist descriptions, setup and later growth plan](CHANNEL_SETUP.md) are saved. Home tab arrangement explicitly deferred until sufficient published content; review after first ten published Shorts as a suggested checkpoint. [HTML publishing page standard](PUBLISHING_PAGE.md) replaces ZIP-first delivery. BM-0003 self-contained page generated and privately saved, media checksums verified; title/settings still proposed, no upload. Banner crop issue identified; two image-edit drafts saved privately, latest lowered branding not yet confirmed in Studio. Original approved artwork preserved. **Next:** finish BM-0003 device/rights and metadata checks, owner-authorized private upload and publication decision. In parallel implement reusable all-layer native 60fps main-chat audio-to-video pipeline and two varied pilots, with Work audio-only, approved narrator/MUSIC-06 and frozen V6. No needless new branding rounds.


> **Owner approval / release bundle (24 November 2026):** The owner accepted the BM-0003 custom thumbnail style and agreed that programmatic thumbnail composition is the default. Generate precise layouts, typography, brand and map/verified logos with code; optionally incorporate rights-cleared generated imagery when appropriate. The accepted cover and V5 final MP4 were independently re-materialized and SHA-256 verified, and a seven-file release ZIP (video, thumbnail, title, description, sources, upload checklist, checksum manifest) was created and archive-tested. Private Library: `/BharatMode/BM-0003-lt-chennai-ai-cluster-order-release.zip`, ID `libfile_ac72d80e1a408191bd6ae782fa0f6231`, SHA-256 `40cec26e7643c4ed34f92d8d8ac7ce58ca31393c3a51c97f4e1eafdc3b4d7f3e`, 6,447,203 bytes. No video re-encode. Creative video/cover approval complete; proposed metadata, physical phone/platform crop check and rights evidence remain distinct from explicit upload authorization. BM-0003 is In Progress, not published. Next: complete release gates; no unnecessary creative revisions. Work remains audio-only.


> **Approved thumbnail and filenames (24 Nov 2026):** [THUMBNAIL_AND_EXPORT_DIRECTION.md](THUMBNAIL_AND_EXPORT_DIRECTION.md) defines custom story-summary thumbnails and canonical `BM-####-<slug>.mp4` filenames. BM-0003 final MP4 now saved as `BM-0003-lt-chennai-ai-cluster-order.mp4` (byte-identical approved V5) and a custom matching PNG cover prepared for review. Old single-frame thumbnail superseded as default. No upload; remaining device/rights and publication gates unchanged.


> **Release preparation — 24 November 2026:** [BM-0003 release package](../publishing/BM-0003-release.md) now contains proposed title, description, thumbnail, settings and independently repeated technical/source QA. Actual approved MP4 SHA matched; 60fps / 2490 frames / 41.5s; full decode passed; −18.6 LUFS and −2.3 dBTP measured. Thumbnail extracted at 25.90s and saved privately. No video changes or upload. **Next:** owner review of metadata/thumbnail, device playback and remaining individual asset rights checks, then separate upload authorization. BM-0003 remains In Progress. Work audio-only.


> **CURRENT — 24 November 2026:** Owner approved the actual BM-0003 Revision 5 video and the open-canvas 60fps direction. **V6 + approved episode Revision 5** is the reference; [visual rules](OPEN_MOTION_DIRECTION.md) and [template](APPROVED_SHORTS_TEMPLATE.md) are authoritative. Creative review complete; phone QA and explicit publication approval remain separate. Always deliver a direct downloadable MP4. Work stays audio-only. No new render or audio regeneration needed for this approval.

**Historical checkpoints below record what was true at the time; earlier pending review statements are superseded by this approval.**

## BM-0003 Revision 5 — 60fps review delivered (24 November 2026)

- Owner approved V4's open-canvas format; V5 removes redundant labels, fixes the ascending contract-value range, separates India/Tamil Nadu label timings and positions finale labels outside their connections. Quantitative values count up with eased monotonic animation. Dates and model names remain identifiers. Essential fact qualifiers retained.
- Main-chat renderer `scripts/render_bm0003_open_motion_60fps.py` evaluates story art at each 60fps timestamp with subpixel drawing. Existing V6 chrome/title/caption/progress pixels are inherited from the original 30fps base; this is an explicit pilot limitation, not a complete native-60fps Remotion rebuild. Future production should render all layers at 60fps from verified audio/alignment assets.
- **Actual private output:** `BM-0003-v5-60fps.mp4` — 1080×1920, H.264/AAC, 60fps, 2490 frames, 41.5s, 6,330,450 bytes. SHA-256 `77367478e2a761661ece4068e400a589a4b2e75739dec2497eb60185e2fee634`. Decoded all 2490 frames at 270×480 for MD5 checks: zero identical adjacent frames. Four counter monotonicity/final-value checks passed. Representative still contact sheet inspected. Audio ADTS SHA-256 `a5a7966dfee87cf5f5482206ee10af254c270cc7a7600b3c0b2c3800e7632aa0` exactly matches V4. No audio changes.
- MP4 saved privately in ChatGPT Library `/BharatMode/` (library file ID `libfile_e0c9f9e7889c819188faa7916f611d99`). Direct MP4 delivery rather than a redundant HTML download. V4 embedded video HTML valid, but owner's in-chat preview cannot play it; exact preview failure unconfirmed. No claim that client can play a given MP4 inline until owner tests.
- **Next:** owner visual/playback review of V5, phone QA and publication sign-off. Nothing published. Work remains audio-only.

> **Owner approval / refinements (24 Nov 2026):** V4 open-canvas format approved. Revision 5 requested: true 60fps story animation, quantitative count-ups, minimal meaningful labels, ascending value range and non-overlapping map/network labels. Direct MP4 preferred because embedded-video HTML does not play in owner's chat preview. [Permanent rules](OPEN_MOTION_DIRECTION.md). V5 validation/review pending; do not publish.

> **Latest visual direction (24 Nov 2026):** BM-0003 V4 open-canvas motion review rendered here, replacing static boxed heroes with independently animated graphics and moving backgrounds. Original voice/music unchanged; owner review pending. [Details and permanent visual rules](OPEN_MOTION_DIRECTION.md).

### Revision 3 review delivery recovered — 24 November 2026

- The previous V3 encoded file was unavailable, so the main chat **reproduced** the V3 map/identity/camera revision from checksum-verified V2 (SHA-256 `6e4018988a67254b3db2273309c69dea5830c40be992489e37176b3a81448290`), committed Natural Earth geometry and the V3 rendering logic, including the documented L&T/NVIDIA marks. No Work video task and no new narration.
- New private output: `BM-0003-naturalearth-v3-rebuilt.mp4`. SHA-256 `60048b3db32c6e239d7dbbd4e1c32c8329088d662f835a2ff92c8865076f93a4`; **this is a fresh encode, not byte-identical to the earlier V3 video**. H.264/AAC, 1080×1920, 30fps, 1245 frames, 41.5s. Full decode passed. Natural Earth Chennai point lies within the stored Tamil Nadu polygon; inspected representative map frames.
- Audio codec-stream SHA-256 `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` matches the original/V2/V3 record. Qwen voice and MUSIC-06 Option B unchanged.
- **Both actual review files now saved privately in ChatGPT Library /BharatMode/**: the rebuilt MP4 and self-contained `BM-0003-naturalearth-v3-review.html` with embedded video and six scene controls. Verified embedded bytes equal the rebuilt MP4. Delivered in chat. Neither file is committed to Git.
- **Next: owner visual review, then phone QA.** Do not reopen audio or map-tool approval. No publishing.

> **Latest (23 Nov 2026):** Natural Earth + Remotion maps **APPROVED**; BM-0003 **Revision 3** physically rendered *here*, not in Work. Verified 41.5s 1080×1920/30fps private MP4 with India POV → true Tamil Nadu polygon → Chennai city pin and L&T/Vyoma.AI/LTN Compute/NVIDIA identifiers. Same AAC stream checksum `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` as V2, no narration/music changes. SHA new video `6aa5cb03e4448819dae65f04fa669fb1233c269a137d93d6bee1291f62224f9e`. [Map plan + sources](MAP_DIRECTION.md). Revision 3 remains private/unpublished and needs owner visual review and phone QA.

**THIS IS THE CANONICAL RESUME POINT.**

Last verified: **24 November 2026**. Owner approved the main-chat-produced BM-0003 Revision 5 creative result; older checkpoints are historical. Consult Git history for the latest commit. After a task is completed, update this file *in the same commit as the task*, revise the roadmap, and note the actual GitHub commit and any incomplete checks. GitHub is authoritative; old conversation snippets and historical V1–V5 examples are not.

## What the project is
**Bharat Mode** is a research-led, faceless YouTube Shorts channel highlighting verified Indian discoveries, inventions, builders, science, technology and meaningful national progress. Content should find underreported stories without sensationalizing or claiming unsupported "firsts". Voice, evidence and readable vertical animation are core to the product.

Repository: https://github.com/Mythrow/BharatMode

## Historical production checkpoints — earlier revisions (superseded)

### Corrected Work/video boundary and new BM-0003 visual cut — 23 November 2026

- Owner explicitly corrected the workflow: **Work Mode = AUDIO ONLY**, limited to offline Qwen narration/WAV exports, independent transcription QA and real word-level timing files. **Main ChatGPT chat = ALL video**: image/graphics, Remotion/V6 scenes, captions, soundtrack integration and final MP4. Old Work video-rendering instructions are wrong and must not be repeated. [Production Responsibilities](PRODUCTION_RESPONSIBILITIES.md) is canonical.
- Owner reviewed Work's 41.50s BM-0003 cut and found its repeated text/information cards **boring and visually insufficient**, despite technical voice/mix success.
- **Created a new full 41.50s review MP4 inside this chat** with a genuinely animated original schematic hero for each scene: 3D-perspective racks, Chennai chip/deployment visualization, contract band graphic, planned GPU grid, active-versus-planned clarification and connected compute-network finale. Audio stream is **byte-for-byte identical at codec level** to the previous cut; V6 frame/captions/brand/progress unchanged. The video SHA-256 is `6e4018988a67254b3db2273309c69dea5830c40be992489e37176b3a81448290`.
- Technical checks: **1080×1920**, **30 fps**, **1245 frames**, **41.5 s**; H.264/AAC; original and revised audio stream hashes both `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b`. In-chat screenshots/contact sheet inspected. Private MP4 and self-contained playable HTML review delivered; **no public upload**.
- This first visually upgraded bridge cut uses the historical Work MP4 as starting media; future Work jobs must deliver **only audio/alignments**, and the main conversation must render the base V6 video itself. Rendering source: `scripts/render_bm0003_visual_upgrade.py`. Original CGI is **illustrative**, not real site footage. **Owner feedback on revision 2 and device phone QA still pending**.

### MUSIC-06 soundtrack mix APPROVED — Option B, 23 November 2026

- **Owner explicitly chose B** after hearing the three actual ducked comparison mixes. The approved reference faders (simple 0–100 **linear source gains**, not perceived loudness) are **Qwen voice 88**, MUSIC-06 **55 between speech** and **32 while speaking**. As speech returns, music drops from 55→32; speech detector keeps the previously tested **24ms attack / 280ms release** envelope.
- The earlier mix A (voice 88/music 40 normal/16 under speech) was deemed too quiet. Mix C (88/66/44) is a rejected alternative, not approved.
- Approved under-speech music is **32/55 = 58.2% of its between-speech amplitude** (about **41.8% reduction** during narration). In the original 20-second MUSIC-06/old Qwen reference comparison, active speech average **voice/music separation ~13.8 dB**. This is a measured preview reference, **not a guarantee** on the ungenerated BM-0003 full narration.
- [config/music.json](../config/music.json) now holds `approvedMix` as the **single source of truth**; `scripts/preview_signature_mix.py` reads Option B directly so future technical review mixes do not accidentally fall back to old A. Final mobile-speaker and complete BM-0003 MP4 loudness QA still pending. **No need to re-ask for music-volume selection.**



### BM-0003 private review cut — 23 November 2026

- Generated and integrity-checked all six scenes with the official pinned Qwen3-TTS 1.7B Base checkpoint and the checksum-verified approved narrator. The initial CPU run was killed before synthesis. Disk-backed, unquantized float32 talker weights let the retry finish on permitted Work Mode CPU compute. Scene narration durations: 6.48, 6.8, 6.16, 5.6, 8.48, 6.32 seconds. Peak process RSS across scenes: 6.54 GiB.
- Independently checked speech with offline Whisper Tiny English and Whisper Base English. Verified dates, names, GPU model and count, and the order-value band. Real WhisperX English alignment produced 100 checksum-linked word timings from the final scene WAVs. Owner listening and pronunciation review remain open.
- Verified the private MUSIC-06 master hash and mixed the owner-approved Option B: voice 88, bed 55 between speech and 32 while ducked, with a 24 ms attack and 280 ms release. Measured mix peak: 0.770. The storyboard's nominal durations were replaced by the actual recordings plus scene-boundary spacing.
- Rendered a 41.50-second, 1080×1920, 30 fps H.264/AAC private MP4 using the approved V6 frame and real-alignment caption overlay. The frozen V6 template is unchanged. SHA-256: `537d2feeac41f15516a8e0d0f99ea3332495708db0254244e14aea7ee0080b89`. The cut is ready for owner phone review and has not been published.

### Music loudness review requested — 23 November 2026

- Owner found old negative dB readouts confusing and MUSIC-06 **too quiet relative to the narrator**. Future audio review should use an intuitive **moving 0–100 level meter** (where 100 = unchanged source amplitude; **not** perceived loudness) with an **inline HTML preview**. Do not presume the previous low bed is approved for production.
- Prepared one self-contained, privately delivered **20-second HTML comparison** containing three actual independently mixed MP3 options, all with the exact same approved old Qwen reference speech:
  - **A original:** voice 88/100; music normal 40/100, under speech 16/100; measured stem RMS voice/music separation ~19.7 dB.
  - **B suggested louder:** voice 88/100; music normal 55/100, under speech 32/100; voice/music separation ~13.8 dB.
  - **C stronger:** voice 88/100; music normal 66/100, under speech 44/100; voice/music separation ~11.0 dB.
- The same 24ms attack/280ms release speech detector controls the music. Three mixes generated and checked below clipping; the private master/voice SHA were verified, and a **portable script regenerated byte-identical HTML/MP3 output** locally. Source: `scripts/generate_music06_level_comparison.py` (private input arguments; HTML and private audio NOT Git-tracked).
- **Superseded:** owner chose **B** as the standard reference mix. Do not reopen A/B/C selection; full BM-0003 story narration and device loudness QA remain incomplete.



### Audio review format + measured MUSIC-06 levels — 23 November 2026

- **Owner preference for all upcoming audio checks:** present a **self-contained HTML preview with embedded playable audio** right in chat (no separate MP3/WAV downloads), allowing multiple comparison takes and simple listening; don't ask owner to run code. Generic script `scripts/build_audio_review_html.py` is committed; generated HTML embeds private bytes and must remain out of Git.
- Verified against the exact MUSIC-06 input MP3, original approved Qwen WAV, and existing 20-second mix preview: Qwen fader `0.88` (**−1.11 dB**), music baseline `0.40` (**−7.96 dB**), full speech duck `0.16` (**−15.92 dB**), an additional **−7.96 dB / 60% amplitude reduction**. Attack ~24 ms; release ~280 ms.
- In actively ducked portions, separated voice stem RMS **−20.17 dBFS**, music stem RMS **−39.90 dBFS**; voice−music overlap separation **19.74 dB**. These are mix-test measurements, not publication loudness targets or LUFS. HTML A/B preview generated locally with actual ducked mix, unducked counterpart, voice-only and music-only; **no BM-0003 narration yet**. Phone listening remains pending.



### BM-0003 Work Mode execution attempt — 23 November 2026

- Read the production runbook and located the canonical private MUSIC-06 master by its recorded path. Work Mode became unavailable before any commands could run. The current attempt did not retrieve or rehash the audio files, load Qwen, generate scene narration, check transcripts, align with WhisperX, mix, or render a pilot. No paid compute or publishing occurred.
- BM-0003 remains in progress. Resume from the private asset checksum checks and six-scene synthesis in [the runbook](WORK_MODE_BM0003_RUNBOOK.md) when permitted Work Mode compute is available.

### BM-0003 — story/audio preparation completed 23 November 2026

- **Owner-selected first new content:** `BM-0003`, L&T's **23 November 2026** additional Chennai NVIDIA B300 GPU order. Re-verified L&T's **23 November** release and separate **13 August** 10,000-GPU plan. [Six-scene script](../stories/lt-chennai-ai-cluster-order.json) drafted, **48 seconds provisional**, clearly distinguishes newly announced order from planned installed capacity. Linked into the permanent [content registry](../content/registry.json) and creative queue. No duplicate ID or published video.
- **MUSIC-06 licensing:** owner confirmed **paid ElevenLabs Music plan** at generation. Official [9 October 2026 Music Terms](https://elevenlabs.io/music-terms) allow ordinary monetized YouTube audiovisual synchronization without mandatory attribution on Starter-or-higher paid tiers. Exact individual tier/generation receipt not independently inspected; do not redistribute as a standalone music library.
- **Real preview mix created:** original private MUSIC-06 MP3 and existing approved Qwen voice reference were SHA-verified; 20-second stereo ducked music+voice preview generated, peak 0.821 before encoding, no clipping. It contains the **old approved narrator audition, NOT BM-0003 story narration**; phone and full-story mix QA pending.
- **Offline Qwen execution plan prepared:** `scripts/produce_story_audio.py` dry-run produces six exact scene commands using the official pinned Base model. Six Python contract tests passed. The **actual** full BM-0003 WAVs and WhisperX alignment have **not run**; 5.8 GiB chat RAM is below the previously measured 7.68 GiB Qwen Base peak.
- **NEXT:** run real scene narration/ASR/acoustic alignment on permitted free Work Mode compute; pair with MUSIC-06 and owner-approved V6 visual frame; deliver a first complete voiced MP4 for owner review. [Runbook](WORK_MODE_BM0003_RUNBOOK.md). No paid TTS credits/API/compute, no publishing without final sign-off.

### Previously selected music master — MUSIC-06 (archival checkpoint)

### MUSIC-06 signature master selected — 23 November 2026

- User approved their uploaded `techno-thriller-final.mp3` for Bharat Mode. Exact original MP3 stored privately at `BharatMode/music/techno-thriller-final.mp3` in ChatGPT Library, SHA-256 `adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9`, 54.99 seconds, stereo 44.1 kHz MP3 192 kbps. Original master is **not** public Git media. Details in [config/music.json](../config/music.json) and [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md).
- Use as the recognizable default for first ~5–10 Shorts with varied sections, levels, cuts and Qwen narration ducking. Later maintain 2–3 related textures to avoid repetitive identical soundtracks. MUSIC-01–05 are superseded; do not re-request selection.
- **Updated after this selection:** owner confirmed paid ElevenLabs Music plan; official current terms allow ordinary commercial YouTube video synchronization without attribution for paid tiers. The exact account tier/receipt was not independently inspected. Final mixed-video QA and publication permission still pending.
- The existing `public/music/ambient.wav`, original SFX and approved V6 visual template remain untouched. Next: mixed BM-0003 pilot with final voice alignment, licensed soundtrack verification and phone QA.



### Historical/superseded audition — MUSIC-05 melodic techno, 23 November 2026

- Owner rejected the MUSIC-04 hip-hop feel and wants **modern melodic techno**, with a **deeper low/mid synth melody and prominent bassline**, not high-key keyboard notes.
- Created **MUSIC-05 Deep Current**, an original 30.968-second, 124 BPM, four-on-the-floor F-minor techno candidate. Music-only and approved-Qwen-narrator-mixed WAVs/MP3s were generated, with stereo PCM16 WAV readback and no clipping; exact SHA hashes and code in [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md) and `scripts/generate_melodic_techno_audition.py`.
- **Superseded:** owner subsequently chose the separate paid ElevenLabs MUSIC-06 techno-thriller recording. V6 and approved narrator remain unchanged; MUSIC-05 was not adopted.


### Historical MUSIC-04 lo-fi audition — superseded by MUSIC-05

- Owner listening feedback on earlier scores: **MUSIC-01 too boring/simple**; likes MUSIC-03 rhythm and MUSIC-02 tune; wants a lo-fi beat with both traits. This is **directional feedback, not soundtrack approval**.
- Created a 31.304-second original **MUSIC-04 Lo-Fi Motion** audition at 92 BPM: swung hip-hop drums, warm Rhodes-style harmonic progression, brighter original melodic hook and subtle tape texture. Music-only and Qwen-narrator-mixed WAV/MP3 previews delivered in chat. Original reproducible source in `scripts/generate_lofi_audition.py`, details/checksums in [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md).
- Both 44.1 kHz stereo PCM16 WAVs passed readback, finite-sample and peak tests with no clipping; the mixed preview uses the exact owner-approved private reference. **Human listening is pending.** No soundtrack or SFX masters replaced and no V6 modifications.
- **Superseded:** owner rejected the hip-hop feel and requested MUSIC-05 instead. If it matches the desired groove, iterate to a real loopable, length-adaptable production music bed and matching minimal sonic stinger, then verify voice mixing and phone playback before locking music.



### New soundtrack selection checkpoint — 23 November 2026

- **Historical, pre-MUSIC-06 checkpoint:** old repository `public/music/ambient.wav` and `public/sfx/*.wav` were starter placeholders; the owner later selected MUSIC-06 as the new signature soundtrack, while production integration remains pending.
- Created three original, no-subscription procedural 20-second music candidates: `MUSIC-01 Quiet Momentum` (understated warm editorial), `MUSIC-02 Curious Discovery` (airy science-optimism), and `MUSIC-03 Built Forward` (restrained engineering momentum). Each has an instrumental-only WAV and an audition mix with the exact **approved private Qwen3 narrator**. Three narrated MP3 previews also generated for convenient listening in this chat.
- All six WAV previews were generated and checked as stereo 24 kHz PCM16, 20 seconds, below clipping; Python generator syntax and an instrumental-only run without a private voice passed. No preview has been **human auditioned/approved** yet; no long seamless looping/music loudness phone QA or final SFX identity has been verified.
- Composer source: [generate_music_auditions.py](../scripts/generate_music_auditions.py); editorial options and approval criteria: [MUSIC_DIRECTION.md](MUSIC_DIRECTION.md). Preview binaries remain untracked, and **all existing production music/SFX masters and the approved V6 frame are unchanged**.
- **Superseded:** owner completed music selection with MUSIC-06. No further MUSIC-01/02/03 auditions needed. Work on actual BM-0003 narration and V6 integration.



### Permanent content ID registry launched — 23 November 2026

- **Single source of truth:** [Content Log](../content/CONTENT_LOG.md) (human-readable boards: Idea, In Progress, Published), [Canonical registry JSON](../content/registry.json), and [one research sheet per ID](../content/research/). Every candidate and completed Short retains a permanent, never-recycled `BM-####` ID. See [CONTENT_PIPELINE.md](CONTENT_PIPELINE.md).
- **Imported existing work:** `BM-0001` PARAM Rudra (In Progress); `BM-0002` ICMR 100 tech-transfer deals (Idea, despite having an unvoiced storyboard); `BM-0003` L&T's **23 Nov 2026 new NVIDIA B300 Chennai order** (**In Progress**, owner chose to trial; **not published**); `BM-0004` IIT Madras 22 Nov sleep/autism labs (Idea).
- Story briefs `param-rudra`, `icmr-tech-transfer` and now `lt-chennai-ai-cluster-order` match their permanent content IDs; the selected [BM-0003 dated research](../content/research/BM-0003.md) and 48-second provisional storyboard exist. No full Qwen story narration or video upload yet. Keep the legacy `publishing/queue.json` for already-written story slugs only, not as the content registry.
- `scripts/content-registry.mjs` allocates IDs, searches all stages, enforces duplicate event/source/title and same-topic follow-up checks, validates stage transitions, and generates the content log. **Fourteen local automated tests passed**, including no deletion/reuse, duplicate intake, transition/published gates, cross-link requirements and stale-log detection. CI now checks the registry (note: unrelated GitHub Actions runner startup issues remain possible).
- **Editorial rule:** every daily candidate is compared against **all IDs including Published**. New developments in previously covered topics need a distinct event, related ID and explicit reason. A topical or semantic overlap still requires human editorial assessment; mechanical dedupe isn't perfect.


### Permanent narrator approved — 23 November 2026

- **Owner reviewed both WAVs and explicitly approved their similar, consistent voice.** This finalizes the identity of Bharat Mode's original Qwen3 synthetic documentary narrator; **do not ask for another A/B approval**.
- Reference SHA: `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c` (7.6s, 24 kHz mono PCM16). Exact private reference transcript and VoiceDesign model revision are frozen in `config/narrator-reference.json`. Qwen3-TTS 1.7B **Base** revision `fd4b254389122332181a7c3db7f27e918eec64e3`, new-line test SHA `c2a323ced010a718a90e03bdd365fe9b15a2d8b5ff6446ab71302cf6b0d6688b` (8.8s; 22/22 ASR words; 0.724 embedding cosine).
- **Approved voice identity ≠ all future takes approved.** The original `PARAM` pronunciation remains unverified: offline ASR transcribed "Parum". Check proper names, all spoken words and loudness for each final story.
- **Active pilot is now BM-0003 L&T Chennai** using the approved voice reference; generate its full script on permitted Work Mode CPU, measure pronunciation and throughput, align real WAVs, and integrate locked V6. PARAM Rudra BM-0001 remains a separate in-progress earlier pilot, not the current daily-story production target.


### Verified Base narrator-consistency test — 23 November 2026

- Used the original private 7.600 s VoiceDesign WAV after re-verifying its SHA-256 and 24 kHz mono PCM16 format against [the reference manifest](../config/narrator-reference.json).
- Ran the official Qwen3-TTS 1.7B Base checkpoint offline on four CPU threads, with staged float32 processing and the exact private reference transcript. Generated 8.8 s of new speech. The real-file integrity gate passed with no clipped samples. Offline Whisper Tiny English recovered all 22 words of the new passage.
- Speaker-embedding cosine similarity was **0.724** between the reference and the new sample using SpeechBrain ECAPA-TDNN. The two halves of the reference scored 0.638 and the two halves of the new sample scored 0.793. This supports consistency for this pair. Owner A/B listening is now **approved**, while original `PARAM` pronunciation review remains open.
- **Measured:** 103.5 s from model loading through WAV write, including 101.8 s for the staged generation path. Peak process RSS **7.68 GiB** on a 9.7 GiB Work Mode workspace. Installation and weight downloads are excluded. No paid compute, speech APIs, subscriptions or credits.
- The private WAV was delivered in the Work Mode conversation. Model revision, checksums, timing breakdown and the tested command are in the [Base runbook](WORK_MODE_BASE_RUNBOOK.md).

### Verified Qwen3-TTS Work Mode audition — 23 November 2026

- Downloaded the official 1.7B VoiceDesign weights and speech tokenizer, verified their SHA-256 hashes, and ran inference from local files with Hugging Face offline mode on a CPU-only Work Mode workspace (9.7 GiB reported RAM). No paid compute, metered voice API, subscription, or voice credits were used.
- Fed the voice prompt from [config/voice.json](../config/voice.json) and the exact PARAM Rudra audition text from [the smoke script](../scripts/qwen-voice-design-smoke.py). Verified a 7.6-second, 24 kHz mono PCM WAV. The owner can play the sample in the Work Mode conversation. The WAV is kept outside Git.
- The audition now serves as the verified engineering reference. The owner can compare it with the new Base sample.
- Earlier GitHub Actions [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) still records a separate runner startup failure before any step. Work Mode testing used the repository smoke script with a pinned local snapshot, a fixed seed, and staged float32 processing. The all-float32 attempt was killed under memory pressure and an INT8 sample failed the transcript check. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) for settings and timings.

### Caption alignment engineering checkpoint — 23 November 2026

- Built `scripts/align_qwen_words.py` to use a locally installed open-source WhisperX forced aligner on **real finalized narration WAVs**, writing checksum-linked word starts and ends. It rejects missing words, invented words, overlapping/invalid times, and transcript mismatches rather than estimating word times.
- Built `src/aligned-caption-timing.js` and `src/aligned-captions.jsx` as an **optional** centered word-synced V6 caption overlay. Group timing comes exclusively from a `final-audio-acoustic-alignment` file, never the old simulated demo timings. The approved V6 frame, layout and legacy story renderer were **not changed**.
- **Tests actually executed here:** eight Python alignment-contract tests, thirteen JS assertions, real reference-WAV header/hash check. All passed. Tests do **not** exercise WhisperX inference or Qwen Base.
- **Still pending:** run WhisperX on finalized narration, verify actual word timing, and render with V6. See [AUDIO_ALIGNMENT.md](AUDIO_ALIGNMENT.md).

**Completed and approved by channel owner**
- Channel name: **Bharat Mode**; tagline: **Big Ideas. Real Progress.**
- Brand palette: Classic Saffron `#E8752E`, Warm Ivory `#FFF7EB`, Ocean Teal `#117A7A`, Graphite Navy `#283039`, Deep Charcoal `#0B1018`.
- Typography: **Sora** for headlines/display; **Manrope SemiBold** for reading and captions.
- Exact SVG **badge and avatar** are approved source artwork under `public/brand/`; do not redraw or recolor the logo's internal colors.
- YouTube channel-cover design approved; see [CHANNEL_BANNER.md](CHANNEL_BANNER.md). Verify actual YouTube device crops before relying on it.
- **Official Shorts V6 visual/motion template APPROVED on 23 November 2026** after the final bar-centering adjustment. The source of truth is [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md); reusable visual component is [`src/approved-shorts-template.jsx`](../src/approved-shorts-template.jsx).
- **Progress bar perfectly centered** on 1080px canvas: 84px left + 912px bar + 84px right. A regression checker exists at `scripts/test-approved-template.mjs`.
- Approved look: directional character-by-character headline typing **without cursor**; entrances for text, hero and diagrams; raised hero; 0.34s subtle scene dissolve; topic-only pill; flexible chapter segmentation rather than fixed five-step formula; one-line *centered* phrase-group captions with very light, content-sized translucent backing, ~0.2s word pop from 60% to slight overshoot, transient highlight on spoken word; old phrases disappear.
- Earlier browser HTML preview variants under `previews/html/` are retained as design history. **V6 with symmetric progress** is the only current approved visual baseline.
- **Narrator engine selected 23 November 2026:** owner auditioned Qwen3-TTS and prefers its audio to Kokoro. **Approved engine: self-hosted Qwen3-TTS 1.7B VoiceDesign** (Apache-2.0); **no paid TTS subscriptions, metered API charges or voice credits**, and no Indian-accent requirement. Brian is professional-tone inspiration only. The original synthetic reference has been verified and retained privately. Kokoro is a fallback. See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) and [`config/voice.json`](../config/voice.json).

**Not yet completed / not approved for publication**
- The `BharatShort` production renderer in `src/short.jsx` is **still a legacy renderer**, not yet fully upgraded to approved V6 motion and per-word aligned captions. Its bar alignment has been fixed.
- No end-to-end **voice-aligned, fully rendered, phone-tested** publishable Short has been verified.
- The **permanent narrator identity is owner-approved** following A/B listening. Full-script pronunciation and delivery, actual word-level alignment, and sound-mix QA remain pending. The old vidIQ Brian and OpenAI TTS production paths are ineligible under the zero-credit requirement.
- Word-level caption timestamps must come from real finalized narration audio (TTS word timestamps or forced alignment), not the manually estimated prototype timings.
- Evidence/rights pipeline, upload-ready sourcing, audio ducking/loudness QA, actual YouTube crop/safe-area QA, and three distinct finished pilots are outstanding.

## Exactly where to resume in the next chat

**NEXT TASK — Complete remaining release gates for the accepted BM-0003 video and thumbnail.**

The approved V5 video is already complete for creative review. Title, description, thumbnail and technical/source QA are prepared in `publishing/BM-0003-release.md`. Confirm device playback and individual rights evidence; obtain separate explicit publication approval before upload. Generalize the approved open-canvas treatment into a native-60fps all-layer video renderer starting from verified audio-only Work deliverables for future stories. PARAM Rudra remains a separate later pilot.

Current implementation tracker: [GitHub issue #5 — voice-synced V6 renderer and first pilot](https://github.com/Mythrow/BharatMode/issues/5).

## Non-negotiable workflow preferences
- **The owner does not want to run code or install tools on their device.** Always deliver a direct MP4 download link for video; HTML/Play/Open controls are not substitutes. Audio review may use verified playable HTML when supported.
- **Qwen3-TTS narrator identity owner-approved on 23 November 2026 after A/B listening.** Owner prefers deep professional delivery; an Indian accent is not required. Self-host with no paid TTS subscription, credits, metered API or silent billing upgrades. Confirm free compute feasibility separately.
- Do not make unnecessary previews after explicit visual approval; make minor fixes in source and report the change.
- Preserve the approved badge, avatar and V6 visual baseline unless the owner explicitly requests changes.
- Keep storyline structure flexible and topic-appropriate. No fixed chapter count, title formula or compulsory length.
- Use reputable primary/public sources where possible; store references, source dates, publication-stage qualifiers and claims evidence in research metadata/descriptions. Never imply speculative illustrations are actual footage.
- **Store** code, docs, storyboard/research metadata, licensed asset references, and original music and SFX masters in GitHub.
- **Do not store** generated speech audio or rendered video files in GitHub. Those can be regenerated and provided to the owner as review/download artifacts.
- User's timezone: Asia/Kolkata. Use absolute dates in handoffs where needed.

## Read these files in this order in a new session
1. **This file**: `docs/PROJECT_STATUS.md` — current stage, approvals, next action.
2. [ROADMAP.md](ROADMAP.md) — project-wide sequence and acceptance milestones.
3. [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) and [OPEN_MOTION_DIRECTION.md](OPEN_MOTION_DIRECTION.md) — locked V6 and approved episode Revision 5 production reference.
4. [PRODUCTION.md](PRODUCTION.md) — existing production scripts and known limitations.
5. [BRAND.md](BRAND.md), [LOGO_DIRECTION.md](LOGO_DIRECTION.md) and relevant story files as needed.
6. [GitHub issue #5](https://github.com/Mythrow/BharatMode/issues/5) for remaining actionable work.

## Handoff convention after each significant change
Update this file and `docs/ROADMAP.md` with:
- **Done:** exactly what was completed and reviewed; link the source or commit.
- **Approved vs proposed:** explicit approval boundary.
- **Verification:** what actually ran/passed and what remains untested.
- **Next:** single immediate action, followed by optional subsequent tasks.
- **Blocked:** any missing tools, accounts, keys, licensing or data.
- Keep the most current status near the top; do not append contradictory “current draft” fragments endlessly.

## One-message prompt to resume anywhere

> Continue the Bharat Mode YouTube Shorts project from https://github.com/Mythrow/BharatMode. First read `docs/PROJECT_STATUS.md`, then `docs/ROADMAP.md` and `docs/APPROVED_SHORTS_TEMPLATE.md`. Respect the approved V6 + BM-0003 Revision 5 open-canvas 60fps direction in `docs/OPEN_MOTION_DIRECTION.md`, keep Work audio-only, include direct MP4 downloads, do not ask me to run code locally, and carry out the next unfinished milestone. Update the GitHub status and documentation after completing work.

**Important:** A new chat does **not** automatically fetch or read this GitHub file just because it exists. The prompt above explicitly points it to the authoritative repository. In the Bharat Mode ChatGPT Project, prior context may help, but check this file for the current state rather than trusting a possibly stale summary.
