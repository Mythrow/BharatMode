# Work Mode: Qwen3-TTS Base narrator-consistency test

**Stage:** execution handoff, not evidence that Qwen Base has run. Last updated: 23 November 2026.

## Goal

Generate a **real new-line WAV** using `Qwen/Qwen3-TTS-12Hz-1.7B-Base` conditioned on the channel's **original Qwen3 VoiceDesign synthetic reference**. Check whether the audible voice stays consistent, its pronunciation is intelligible, and the workflow remains usable without TTS API charges, credits, paid subscriptions, or requiring the owner to install anything.

The original VoiceDesign 7.6-second audition **did run successfully** in Work Mode on CPU. That does **not** establish that this Base test has run or that it will meet the same resource limits. The existing `.github/workflows/qwen-voice-smoke.yml` had a runner-startup failure; don't assume GitHub Actions solves this.

## Inputs and guardrails

- Repo: `https://github.com/Mythrow/BharatMode`, `main` branch.
- First read `docs/PROJECT_STATUS.md`, `docs/VOICE_DIRECTION.md`, `config/voice.json`, `config/narrator-reference.json`, and `scripts/qwen_base_voice_test.py`.
- **Private reference:** `bharat-mode-qwen-voice-audition.wav`, 7.600 s, 24,000 Hz, mono PCM16, SHA-256 `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`. Find the already-generated artifact in the owner's personal ChatGPT Library/Work conversation; don't ask them to install an app or run code. If the file isn't accessible from the Work task, report that blocker rather than substituting a different recording.
- Reference transcript, exactly: `India is building more of its own supercomputing infrastructure. Meet PARAM Rudra. Here's what the evidence shows.`
- Base model: official `Qwen/Qwen3-TTS-12Hz-1.7B-Base`; use its Apache-2.0 model weights, and record the exact model revision and local dependency versions. Do **not** use a hosted TTS API or a lookalike voice model.
- New-line audition passage: `Across India, researchers are using advanced computing to study harder scientific problems. What happens when more laboratories gain access to this technology?`
- Work Model's previous working VoiceDesign inference required staged float32 execution and about 7.3 GiB peak RSS on a ~9.7 GiB CPU workspace. **Plain float32 Base inference may exceed that memory.** First check memory and use safe CPU strategies or staged inference if required, rather than exhaustively retrying an OOM process. Do not buy compute without explicit permission.
- **No third-party voice cloning:** the reference was synthetic/original for Bharat Mode. Never use vidIQ/ElevenLabs Brian's audio as the clone source.
- **No public Git media:** voice WAVs, output JSON and raw model weights remain outside the repo; preserve only code, license/model revision/measurement notes and links to private artifacts.
- **V6 visuals are locked**; no template redesign.

## Execute on a permitted Work Mode cloud computer

1. Ensure `main` is current. Provision only already-available free compute. Check RAM, CPU/GPU and remaining disk before downloading the model. Prefer cached official weights and refuse unapproved fees.
2. Retrieve the private reference into an ignored location, e.g. `out/private/bharat-mode-qwen-voice-audition.wav`. Confirm it matches the SHA and metadata through:

   ```bash
   python scripts/qwen_reference.py --audio out/private/bharat-mode-qwen-voice-audition.wav
   ```

3. Prepare official `qwen-tts` with CPU PyTorch if no GPU is available, then download/cache `Qwen/Qwen3-TTS-12Hz-1.7B-Base` and record model revision. The checked-in test uses `create_voice_clone_prompt(ref_audio=..., ref_text=..., x_vector_only_mode=False)` followed by `generate_voice_clone` on the *different* audition text.
4. Execute `scripts/qwen_base_voice_test.py` on the verified private WAV. This existing test uses ordinary float32 on CPU, so monitor memory closely. If it cannot run within the available RAM, optimize/stage inference and **test the actual revised code**; don't claim success based on a smoke test or an unrelated VoiceDesign run.

   ```bash
   python scripts/qwen_base_voice_test.py \
     --reference out/private/bharat-mode-qwen-voice-audition.wav \
     --model Qwen/Qwen3-TTS-12Hz-1.7B-Base \
     --device cpu \
     --output out/qwen-base/narrator-consistency.wav
   ```

5. On real generated output, run the separate standard-library WAV/manifest integrity gate:

   ```bash
   python scripts/validate_qwen_base_output.py \
     --audio out/qwen-base/narrator-consistency.wav \
     --manifest out/qwen-base/narrator-consistency.json \
     --reference-manifest config/narrator-reference.json
   ```

   A pass means **only that a non-silent, sufficiently long, checksum-linked PCM WAV was generated**. It does not certify voice identity, word transcript, factual claims or publication readiness.
6. Separately listen to the actual new WAV versus the original reference. If a local offline ASR model is feasible, compare the decoded words with the new script (pay special attention to skipped words and `PARAM` in the reference), but do not confuse a forced aligner with transcript verification. If quality is inadequate, report what failed.
7. Return a **playable/downloadable** newly generated WAV in the Work conversation, ideally paired with the original for A/B review. Provide output SHA, audio duration, model revision, CPU/RAM usage, generation time after model load, and any errors/retries. If run fails, show the real blocker and do not fabricate a sound sample.
8. Update `docs/PROJECT_STATUS.md`, `docs/ROADMAP.md`, `docs/VOICE_DIRECTION.md`, and Issue #5 in the same checkpoint with evidence. Do not mark final narrator approval until the owner actually reviews the Base sample.

## After Base is accepted

Only after successful Base voice consistency and audio QA: generate a complete story WAV, verify the spoken transcript, run actual `scripts/align_qwen_words.py` acoustic alignment, consume its timestamps in `src/aligned-captions.jsx` under the approved V6 frame, and migrate `src/short.jsx` without altering the approved look. Then produce one complete, rights-cleared, fact-checked pilot for phone review.

## Failure is an acceptable result

If Work Mode lacks sufficient memory/disk, model downloads are blocked, the Base voice differs materially, or audio is unintelligible, report that honestly. None of these cases permits paid voice subscriptions, credits, API substitution, pretending code-only tests are real acoustic tests, or installing tools on the owner's PC.