"""Qwen3-TTS Base consistency audition using Bharat Mode's private synthetic reference.

This is an **unmetered model-inference** experiment, not an API request.
Run on a Work/cloud machine with Qwen 1.7B Base weights and sufficient RAM/GPU.
The WAV is intentionally not stored in Git. Does not perform speech recognition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

from qwen_reference import validate_reference

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEXT = (
    "Across India, researchers are using advanced computing to study harder scientific problems. "
    "What happens when more laboratories gain access to this technology?"
)


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", required=True, help="Local PRIVATE WAV from the approved VoiceDesign audition")
    parser.add_argument("--manifest", default=str(ROOT / "config" / "narrator-reference.json"))
    parser.add_argument("--profile", default=str(ROOT / "config" / "voice.json"))
    parser.add_argument("--model", default=None, help="Local Base checkpoint path, or official model ID for an initial download")
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--output", default=str(ROOT / "out" / "qwen-base" / "narrator-consistency.wav"))
    parser.add_argument("--text", default=DEFAULT_TEXT)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    args = parser.parse_args()

    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("engine") != "qwen3-tts":
        raise ValueError("The approved engine must be qwen3-tts")
    if any(profile.get(key) is not False for key in (
        "paidVoiceSubscriptionAllowed", "paidVoiceAPICallsAllowed", "expiringCreditServicesAllowed"
    )):
        raise ValueError("Paid/credit-limited TTS must remain disabled")
    reference = validate_reference(args.reference, args.manifest)
    if len(args.text.strip()) < 12:
        raise ValueError("Audition script is too short")
    if args.max_new_tokens < 32 or args.max_new_tokens > 2048:
        raise ValueError("max-new-tokens must be within 32..2048")

    # Delay expensive imports until after verifying the original reference.
    import numpy as np
    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    torch.set_num_threads(min(4, max(1, os.cpu_count() or 1)))
    model_id = args.model or profile["repeatableVoiceModel"]
    dtype = torch.float32 if args.device == "cpu" else torch.bfloat16
    print(f"Valid reference: {reference['sha256']}", flush=True)
    print(f"Loading {model_id} on {args.device}; dtype {dtype}; no paid voice service", flush=True)
    start = time.monotonic()
    model = Qwen3TTSModel.from_pretrained(
        model_id,
        device_map="cpu" if args.device == "cpu" else "cuda:0",
        dtype=dtype,
        attn_implementation="eager" if args.device == "cpu" else "sdpa",
    )
    print(f"Base model loaded in {time.monotonic()-start:.1f}s", flush=True)
    prompt_items = model.create_voice_clone_prompt(
        ref_audio=str(Path(args.reference).resolve()),
        ref_text=reference["referenceText"],
        x_vector_only_mode=False,
    )
    waves, rate = model.generate_voice_clone(
        text=args.text,
        language="English",
        voice_clone_prompt=prompt_items,
        max_new_tokens=args.max_new_tokens,
    )
    if not waves:
        raise RuntimeError("Base model returned no audio")
    audio = np.asarray(waves[0], dtype=np.float32).reshape(-1)
    if audio.size == 0 or not np.isfinite(audio).all():
        raise RuntimeError("Base model returned an empty or invalid waveform")
    if float(np.max(np.abs(audio))) < 0.005:
        raise RuntimeError("Base model output was silent")
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    sf.write(target, audio, int(rate), subtype="PCM_16")
    result = {
        "status": "generated_unreviewed",
        "model": model_id,
        "referenceSha256": reference["sha256"],
        "text": args.text,
        "audioSha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "durationSeconds": round(audio.size / rate, 3),
        "sampleRateHz": int(rate),
        "elapsedSeconds": round(time.monotonic()-start, 1),
        "pronunciationAndVoiceConsistency": "NOT VERIFIED — listen and compare to the reference",
        "published": False,
    }
    target.with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    run()