# Bharat Mode — Qwen3-TTS Voice Direction

**Engine chosen by owner:** 23 November 2026.  
**Status:** Qwen3-TTS approved as preferred open-weight engine after owner listening comparison; **specific reusable narrator reference is not yet saved or technically validated.**

## Approved voice decision and constraints

- **Preferred TTS engine:** Qwen3-TTS, specifically `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` for voice creation.
- **Preferred voice quality:** professional, mature, deep/resonant, warm, clear and composed; confident without exaggerated broadcast hype.
- **Language:** English. **Indian accent is not required.**
- **No paid subscription, no usage-credit allowance, no metered speech API.** Downloadable Apache-2.0 model weights enable unlimited *model invocations* under our own computing resources; the owner does not want to run software locally. Free cloud computing **is not guaranteed** and requires separate feasibility verification.
- Owner evaluated an online Qwen3-TTS demo and preferred its sound to Kokoro; we do **not** have a saved copy of the exact voice/timbre chosen in that demo.
- **No voice cloning of Brian or another real-world person**. Use an original synthetic voice created via VoiceDesign.

### Starting voice prompt (draft, not frozen reference)

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

## Verified execution attempt (23 November 2026)

A real, CPU-only prototype was committed as [`scripts/qwen-voice-design-smoke.py`](../scripts/qwen-voice-design-smoke.py) and [`.github/workflows/qwen-voice-smoke.yml`](../.github/workflows/qwen-voice-smoke.yml). GitHub Actions [run 45105740993](https://github.com/Mythrow/BharatMode/actions/runs/45105740993) failed twice **before starting any step** (steps empty, logs not available). Hence neither model downloads nor inference started, and **no sample was generated**. This is an execution infrastructure blocker; the model/inference code remains untested. GitHub Actions was not charged through any metered TTS service. No user installation is needed to view the run.

The chat execution environment has no GPU, about 6 GiB RAM and no outbound model-download access. Thus no actual Qwen synthesis can run there today. Do not claim a completed narrator audition until an actual WAV exists.

## Integration and quality gates — not yet implemented

1. Confirm usable remotely provisioned compute (1.7B inference is heavier than Kokoro; GPU acceleration is normally desirable) that does not add unapproved payments, paid API calls or metered voice credits.
2. Integrate a Qwen3 voice synthesizer that reads `config/voice.json`, uses the approved reference voice, and produces untracked WAV files. The existing `npm run voice` script still invokes **OpenAI TTS** and must not be mistaken for the approved production provider.
3. Run local forced alignment on the **actual final rendered speech**, verify words and exact timing, and drive the approved V6 screen-centered, one-line caption animations.
4. Upgrade `src/short.jsx` to use the frozen V6 frame, measured scene timing, original music and SFX with ducking.
5. Confirm all license notices and commercial-usage obligations for code, model, any voice reference and media assets; fact-check and phone-review a complete voiced Short. Produce two differently structured pilots after the first is approved.
6. Do not commit generated narration or MP4s to Git. No requirement for the channel owner to install or run software.

## Historical decisions

- **Brian (vidIQ):** owner liked professional timbre; rejected as a production route because free credits can be exhausted. Preserve style preference only. No additional vidIQ narration generations.
- **Kokoro-82M:** Apache-2.0, lighter and unmetered when self-hosted; **fallback** if Qwen cannot run acceptably on available permitted compute.
- **Qwen3-TTS:** owner preferred its audible quality over Kokoro on 23 November 2026. **Engine is approved; actual reference audio and the production pipeline remain outstanding.**
