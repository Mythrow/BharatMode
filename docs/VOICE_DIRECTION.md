# Bharat Mode — Free, Unmetered Voice Direction

**Owner requirement updated:** 23 November 2026.  
**Status:** The *professional Brian-like delivery* is preferred, but the **Brian/vidIQ production voice was superseded** because the free-credit limit can be exhausted. **No final production voice is approved yet.**

## Non-negotiable constraint

No paid voice subscription, no paid-per-character speech API and **no limited or renewable voice-generation credits**. The selected speech model must be open-weight/open-source and runnable under our control, with no artificial character cap. Infrastructure compute is still required; do **not** promise that hosted compute is literally unlimited or permanently free.

The owner **does not require an Indian accent**. Preferred audio character: professional, mature, resonant, clear, trustworthy and composed. The earlier Brian recording is a *style reference only*, not an authorized voice clone or the production provider.

## Recommended solution: local Kokoro-82M

- Model: [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), with [upstream inference library](https://github.com/hexgrad/kokoro).
- Weight/license: **Apache-2.0**; commercial use is allowed under applicable license obligations.
- Usage: downloadable open weights, run locally/offline after setup, **no vendor credits, subscription or recurring per-script API charges**.
- Initial professional male voice audition candidates: **`am_michael`**, **`am_fenrir`**, **`bm_george`**. These are *names of Kokoro model voice presets*, not copies of vidIQ/ElevenLabs identities with similar names.
- Final voice preset must be selected by owner **after actual generated audio samples** using the same PARAM Rudra passage. No Kokoro sample has yet been generated or heard by the owner.
- Confirm license notices for the selected model and bundled voice/dependencies; do not infer unrestricted redistribution rights from a demo website.

## Computation / owner experience

- The owner does **not** want to install software or run commands on their own device.
- Prefer a usable remote development/render environment. GitHub Actions standard hosted runners currently allow free usage for *public repositories*, but still have job, storage, fair-use, and policy constraints; confirm feasibility and do not treat this as limitless hosting. Sources: [GitHub billing](https://docs.github.com/en/actions/concepts/billing-and-usage) and [GitHub Actions limits](https://docs.github.com/en/actions/reference/limits).
- Any infrastructure fees or runtime limitations must be identified and approved explicitly, never silently introduced.
- Do not commit generated speech files or MP4s to the repository, and avoid exposing unreleased material in public CI logs/artifacts.

## Engineering next steps

1. Generate three **actual** Kokoro narrator samples from exactly the same audition script, without a metered TTS provider, and provide listening artifacts directly in chat when possible. Record what was truly generated.
2. Select the voice preset based on pronunciation, naturalness and a Brian-like professional tone; lock preset, model revision and speaking speed in `config/voice.json`.
3. Implement local voice synthesis in the build pipeline, producing audio that can be regenerated without a subscription or expiring credit allowance.
4. Derive accurate word timestamps from the **final generated audio** using a local alignment tool, not estimated timing.
5. Update `src/short.jsx` to use the approved V6 visual frame, centered phrase captions, real narration, audio ducking and all existing source/rights gates.
6. Render/QA one evidence-backed pilot, then two different pilots. Final publication still needs owner approval.

## Rejected approaches / historical auditions

- **vidIQ Brian** (`nPczCjzI2devNBz1zQrb`): owner liked the generated professional sample (~12.28 seconds), but rejected as the production route when discovering its recurring credit limit. Do not spend additional vidIQ credits for Bharat Mode narration.
- **vidIQ Liam, Callum**: earlier explorations, superseded.
- Other free-tier or trial TTS APIs: **not eligible** if they cap usage or require ongoing credits.
- Open-source model with non-commercial license: **not eligible** for planned monetized YouTube content.
- Exact voice cloning of Brian is **not** planned or authorized.
