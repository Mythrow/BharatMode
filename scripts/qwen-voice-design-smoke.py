"""One-shot CPU Qwen3-TTS VoiceDesign test for Bharat Mode.

Run only with downloaded/open model weights; generates an original synthetic
reference audition and a small manifest into an ignored output folder.
No metered TTS services or third-party voice recordings are involved.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / "config/voice.json").read_text(encoding="utf-8"))
OUTPUT = ROOT / "out" / "qwen-voice-smoke"
MODEL = PROFILE["voiceDesignModel"]
TEXT = (
    "India is building more of its own supercomputing infrastructure. "
    "Meet PARAM Rudra. Here's what the evidence shows."
)

def main() -> None:
    if PROFILE.get("engine") != "qwen3-tts":
        raise RuntimeError("This test is for the approved Qwen3-TTS engine only.")
    if PROFILE.get("paidVoiceAPICallsAllowed") is not False:
        raise RuntimeError("Profile must explicitly prohibit paid speech APIs.")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(max(1, min(4, os.cpu_count() or 1)))
    torch.set_num_interop_threads(1)
    print(f"Loading {MODEL} on CPU, float32, eager attention", flush=True)
    start = time.monotonic()
    model = Qwen3TTSModel.from_pretrained(
        MODEL,
        device_map="cpu",
        dtype=torch.float32,
        attn_implementation="eager",
    )
    print(f"Model loaded in {time.monotonic() - start:.1f}s", flush=True)
    print(f"Synthesizing {len(TEXT)} characters; no external speech API", flush=True)
    wavs, sample_rate = model.generate_voice_design(
        text=TEXT,
        language="English",
        instruct=PROFILE["voicePrompt"],
        max_new_tokens=512,
    )
    if not wavs:
        raise RuntimeError("Model returned no waveforms.")
    wav = np.asarray(wavs[0], dtype=np.float32).reshape(-1)
    if not wav.size or not np.isfinite(wav).all():
        raise RuntimeError("Model returned an invalid waveform.")

    audio_file = OUTPUT / "bharat-mode-qwen-voice-audition.wav"
    sf.write(audio_file, wav, sample_rate, subtype="PCM_16")
    manifest = {
        "status": "generated_unreviewed",
        "model": MODEL,
        "language": "English",
        "referenceText": TEXT,
        "voicePrompt": PROFILE["voicePrompt"],
        "durationSeconds": round(float(len(wav) / sample_rate), 3),
        "sampleRate": int(sample_rate),
        "peakAmplitude": round(float(np.max(np.abs(wav))), 5),
        "sha256": hashlib.sha256(audio_file.read_bytes()).hexdigest(),
        "licenseNote": "Qwen3-TTS VoiceDesign Apache-2.0 model; original synthetic sample",
        "note": "Audition test only: not an approved permanent voice or upload-ready narration.",
    }
    (OUTPUT / "audition-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print("Generated: " + json.dumps(manifest, indent=2), flush=True)
    print(f"Total runtime: {time.monotonic() - start:.1f}s", flush=True)

if __name__ == "__main__":
    main()
