# Work Mode production handoff — BM-0003 (L&T Chennai AI infrastructure)

**Prepared:** 23 November 2026. **Stage:** source-checked six-scene script drafted and original MUSIC-06 voice-ducking test generated; **full Qwen narration, real alignment and V6 video not generated yet.**

## Non-negotiable context

- Canonical content ID `BM-0003`, stage `in_progress`, story source: [`stories/lt-chennai-ai-cluster-order.json`](../stories/lt-chennai-ai-cluster-order.json). Do not create another content ID for the same 23 November L&T order.
- Narrator identity **approved**: original privately retained Qwen3-TTS VoiceDesign reference, SHA-256 `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`. Use **official Qwen3-TTS 1.7B Base** model revision `fd4b254389122332181a7c3db7f27e918eec64e3`, same staged CPU path tested in Work Mode. No paid compute or TTS subscription, API, or expiring speech credits.
- Owner selected **MUSIC-06** techno-thriller MP3; exact SHA-256 `adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9`, private copy in their ChatGPT Library (`BharatMode/music/techno-thriller-final.mp3`). Owner reports the file was generated on a **paid ElevenLabs Music plan**. Current Music Terms (9 October 2026) permit commercial online audiovisual media and require **no attribution on paid Starter-and-higher tiers**. Save evidence of the precise generated track/plan if available; the account itself has not been independently examined. See [`config/music.json`](../config/music.json).
- V6 visual layout and identity are **owner-approved and immutable**, especially centered chapter bars and caption behavior. `src/short.jsx` is still the legacy renderer: never call its output a completed V6 pilot without actual integration.
- **Never store the private reference, selected music master, generated WAVs, downloaded weights or rendered MP4 in GitHub.** Save those as private review attachments, including technical checksums.

## Fact-approved editorial boundaries

The **23 November 2026** original [L&T press release](https://www.larsentoubro.com/pressreleases/2026/2026-11-23-larsen-toubro-secures-large-order-for-deploying-ai-cluster) announces a new multi-year engagement through Vyoma.AI/LTN Compute for *additional* NVIDIA B300 GPUs at Chennai, with an unnamed infrastructure customer. L&T's **Large** order classification is the **₹2,500–5,000 crore band** — the exact value and number of added GPUs are **not disclosed**. The **10,000 GPU cluster and 250 MW Phase 1 design** appeared in L&T's [13 August announcement](https://www.larsentoubro.com/pressreleases/2026/2026-08-13-larsen-toubro-secures-mega-order-as-part-of-a-strategic-partnership-with-together-ai-to-build-india-s-largest-nvidia-b300-ai-factory), not as an already-operating result on 23 November. No claims that Nvidia chips were designed by L&T/India or all GPUs are active. See the [BM-0003 research sheet](../content/research/BM-0003.md).

## Exact order of production

1. **Dry-run speech plan:** `python scripts/produce_story_audio.py --story stories/lt-chennai-ai-cluster-order.json` prints the six scene-specific commands and text without loading a model or generating audio. **Six offline contract tests passed** with `python -m unittest discover -s scripts -p test_bm0003_production.py`.
2. In an authorized free Work Mode computer with enough memory and locally cached official Base model, privately retrieve the original narrator WAV, run `python scripts/qwen_reference.py --audio out/private/bharat-mode-qwen-voice-audition.wav`, and use **existing verified** Qwen Base model weights. The prior short test used ~7.68 GiB peak RSS on a 9.7 GiB workspace; a 5.8 GiB standard chat sandbox **cannot** execute it.
3. Actual per-scene narration, with six separate files and independent QA:

   ```bash
   HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_TELEMETRY=1 \
   OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 TOKENIZERS_PARALLELISM=false \
     python scripts/produce_story_audio.py \
       --story stories/lt-chennai-ai-cluster-order.json \
       --reference out/private/bharat-mode-qwen-voice-audition.wav \
       --model /absolute/path/to/verified/qwen-base-checkpoint \
       --output out/voice/BM-0003 --execute
   ```

   The runner calls `scripts/qwen_base_voice_test.py --text <exact scene text>` and `scripts/validate_qwen_base_output.py` for each file. A **pass only verifies audio/metadata integrity, not spoken accuracy**. Keep each WAV and manifest.
4. **Transcript check independent of WhisperX:** run local offline ASR on each real WAV and compare to its exact script; listen for names and numbers (`L and T`, `Nvidia B three hundred`, `twenty-five hundred`, `five thousand`, `ten thousand`). Regenerate problematic scenes *with the same approved voice reference*. Do not use forced alignment to prove words were actually said.
5. **Real timestamps:** once final audio is approved, execute `scripts/align_qwen_words.py --audio <final_scene.wav> --text <exact scene text> --output <private_alignment.json>` on capable compute, or run the story runner with `--align` if WhisperX is installed. Verify missing-word/misalignment edge cases manually. Update scene timings to match actual WAV durations and boundary breaths; the storyboard's **48 seconds are provisional**, not actual speech timestamps.
6. Retrieve MUSIC-06 private MP3 and validate against `config/music.json`; keep it outside Git. Use MUSIC-06 with **owner-approved Option B** reference faders from `config/music.json.approvedMix`: voice **88/100**, music **55/100** in gaps, **32/100** under narration, **24ms attack / 280ms release**. These are relative per-stem source gains; adjust only after measuring actual story intelligibility and device QA. Never revert to old Option A (40/16). For preliminary engineering review, `python scripts/preview_signature_mix.py --music <private_mp3> --voice <private_reference_wav> --out out/music-mix` creates a **20-second narrated music preview with historical reference speech, NOT the BM-0003 story**. In the full pilot, substitute the **actual per-scene story audio**, not that historical audition.
7. Migrate approved V6 frame/motion and `src/aligned-captions.jsx` to story-specific production. Caption words must be mapped to true audio timestamps. Choose original/licensed graphics — any drawn data-centre image must be visibly a schematic, not misleading documentary footage. Export 1080×1920/30 fps and check caption safety, music/voice intelligibility, peak levels and exact fact qualifiers on an actual phone.
8. Deliver the **actual BM-0003 narrated MP4 and audio for owner review**, but do not upload or publish. After all rights, speaking, evidence and audio tests pass, publication still needs owner sign-off. Update research/status/roadmap and issue #5 with *verified* results, never pretend a dry run is a generated pilot.

## Completed locally in the preparation session

- Official company release and earlier project announcement checked against script; script comprises six proposed scenes, 48 seconds total **nominal** duration.
- `scripts/produce_story_audio.py` dry-run validated six scene-specific Qwen Base commands using the pinned model revision; **6 Python contract tests passed**. The real Qwen model was **not** loaded and no new story narration was generated in the standard chat container.
- A **20-second** original MUSIC-06 plus **existing** approved narrator-reference mix test was created in a private sandbox. Source SHA checks matched both original recordings; 44.1 kHz stereo and output peak 0.821 before MP3 encoding. Preview is **not BM-0003 narration**, not a finalized master and not a phone QA pass.
- Music rights status updated from an unknown plan to **owner-confirmed paid plan**, with ordinary YouTube synchronization/monetization supported by current ElevenLabs Music Terms. Document the exact plan if a separate license compliance review later requires it.