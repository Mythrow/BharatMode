# Bharat Mode — Qwen3-TTS Voice Direction

**Engine chosen by owner:** 23 November 2026.  
**Status:** Qwen3-TTS is the approved open-weight engine. Work Mode generated a PARAM Rudra audition for owner review. Reusable voice consistency with Qwen3-TTS Base is pending.

## Approved voice decision and constraints

- **Preferred TTS engine:** Qwen3-TTS, specifically `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` for voice creation.
- **Preferred voice quality:** professional, mature, deep/resonant, warm, clear and composed; confident without exaggerated broadcast hype.
- **Language:** English. **Indian accent is not required.**
- **No paid subscription, no usage-credit allowance, no metered speech API.** Downloadable Apache-2.0 model weights enable unlimited *model invocations* under our own computing resources; the owner does not want to run software locally. Free cloud computing **is not guaranteed** and requires separate feasibility verification.
- Owner evaluated an online Qwen3-TTS demo and preferred its sound to Kokoro; we do **not** have a saved copy of the exact voice/timbre chosen in that demo.
- **No voice cloning of Brian or another real-world person**. Use an original synthetic voice created via VoiceDesign.

### Voice prompt used for the PARAM Rudra audition

> A mature male documentary narrator with a deep, warm, resonant voice. Clear international English, natural conversational rhythm, calm confidence and subtle enthusiasm. Professional and engaging without sounding theatrical, robotic or like a news announcer.

If the owner generated a particularly good VoiceDesign sample in the browser, ask for that generated sample **only when needed to preserve the exact audible identity**. A text prompt alone does not guarantee identical timbre on every regeneration.

## Correct model and reference workflow

Official sources:
- [QwenLM/Qwen3-TTS — official repository](https://github.com/QwenLM/Qwen3-TTS)
- [Qwen3-TTS-12Hz-1.7B-VoiceDesign — Hugging Face, Apache-2.0](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign)
- [Qwen3-TTS-12Hz-1.7B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base)

The official Qwen README documents a consistent-designed-narrator path:
1. Generate and approve a **short ORIGINAL synthetic voice reference** using `generate_voice_design` from the 1.7B VoiceDesign model.
2. Preserve the approved reference audio and exact transcript privately (outside Git); optionally record a cryptographic digest, model revision and prompt in production metadata.
3. Use `Qwen/Qwen3-TTS-12Hz-1.7B-Base`, `create_voice_clone_prompt` and `generate_voice_clone` with that original synthetic reference for **repeatable future audio**. This is a technical voice-consistency workflow, not cloning a third-party narrator.
4. Validate actual speech, pronunciation, pace and consistency on a complete script. Regenerate/refine if necessary.

## Verified Work Mode execution — 23 November 2026

- **Inputs:** exact English text from [the repository smoke script](../scripts/qwen-voice-design-smoke.py) and the voice prompt above from [config/voice.json](../config/voice.json). The script ran through a temporary wrapper with a local model directory, Hugging Face offline mode, PyTorch seed 42, and a 240-frame cap. The model stopped after 95 frames.
- **Model:** [Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign/tree/5ecdb67327fd37bb2e042aab12ff7391903235d3) revision `5ecdb67327fd37bb2e042aab12ff7391903235d3`. Verified the SHA-256 checksums of the model and speech tokenizer (4.52 GB combined).
- **Runtime:** CPU only, four PyTorch threads, staged float32, eager attention, Python 3.12, `qwen-tts==0.1.1`, `torch==2.8.0+cpu`, and `transformers==4.57.3`. 10.7 seconds to load and 96.1 seconds to load and generate, excluding installation and downloads. Peak process RSS was about 7.28 GiB on this Work Mode workspace.
- **CPU memory staging:** loaded the checkpoint in its native bfloat16 format. The talker ran in float32 with the original bfloat16 text embedding table retained in memory and its lookups widened to float32. Released the talker before loading the original float32 speech tokenizer for decoding. The run used the unquantized official weights.
- **Artifact:** `bharat-mode-qwen-voice-audition.wav`, 7.6 seconds, 24 kHz mono, PCM 16-bit. SHA-256 `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`. The sample is available in the Work Mode conversation for listening review and stays outside Git.
- **Transcript check:** local Whisper Tiny English recovered all three sentences and transcribed `PARAM` phonetically as `Parum`. Review the audible delivery and pronunciation before selecting the narrator.
- **Earlier CPU attempts:** the all-float32 process exited 137 during synthesis under memory pressure. The native bfloat16 run and an INT8 run with bfloat16 decoding were stopped after extended runtimes. An INT8 talker with float32 decoding wrote a 15.92-second WAV, but the offline transcript failed to match the script. The staged, unquantized run supplied the audition.
- **Limits:** a single short audition on the available Work Mode CPU, with no new paid compute, paid API, subscription, or voice credits. Voice selection, recurring hosting, the 1.7B Base consistency workflow, and full-script production performance still need verification.

Earlier GitHub Actions [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) failed twice before setup began. The Actions workflow itself still requires an independent runner check.

## Integration and quality gates — not yet implemented

1. Review the Work Mode audition. On approval, retain it privately with its transcript and verify the Qwen3-TTS Base consistency workflow. Check full-script throughput and recurring compute access without unapproved charges.
2. Integrate a Qwen3 voice synthesizer that reads `config/voice.json`, uses the approved reference voice, and produces untracked WAV files. The existing `npm run voice` script still invokes **OpenAI TTS** and must not be mistaken for the approved production provider.
3. Run local forced alignment on the **actual final rendered speech**, verify words and exact timing, and drive the approved V6 screen-centered, one-line caption animations.
4. Upgrade `src/short.jsx` to use the frozen V6 frame, measured scene timing, original music and SFX with ducking.
5. Confirm all license notices and commercial-usage obligations for code, model, any voice reference and media assets; fact-check and phone-review a complete voiced Short. Produce two differently structured pilots after the first is approved.
6. Do not commit generated narration or MP4s to Git. No requirement for the channel owner to install or run software.

## Historical decisions

- **Brian (vidIQ):** owner liked professional timbre; rejected as a production route because free credits can be exhausted. Preserve style preference only. No additional vidIQ narration generations.
- **Kokoro-82M:** Apache-2.0, lighter and unmetered when self-hosted; **fallback** if Qwen cannot run acceptably on available permitted compute.
- **Qwen3-TTS:** owner preferred its audible quality over Kokoro on 23 November 2026. **Engine is approved; actual reference audio and the production pipeline remain outstanding.**
