"""Validate a private Qwen3-TTS narrator reference against tracked metadata.

The WAV stays outside Git. This module uses only the Python standard library,
and can be imported by the Qwen Base synthesis script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import wave
from array import array
from pathlib import Path
import sys


def validate_reference(audio_path: str | Path, manifest_path: str | Path) -> dict:
    audio_path = Path(audio_path).expanduser().resolve()
    manifest_path = Path(manifest_path).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not audio_path.is_file():
        raise FileNotFoundError(f"Private voice reference is missing: {audio_path}")
    data = audio_path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != manifest["sha256"]:
        raise ValueError(f"Voice reference checksum mismatch: {digest}; expected {manifest['sha256']}")
    with wave.open(str(audio_path), "rb") as wav:
        channels, rate, width, frames = (
            wav.getnchannels(), wav.getframerate(), wav.getsampwidth(), wav.getnframes()
        )
        if wav.getcomptype() != "NONE":
            raise ValueError("Voice reference must be uncompressed PCM WAV")
        pcm = wav.readframes(frames)
    expected = manifest["audio"]
    if (channels, rate, width) != (
        expected["channels"], expected["sampleRateHz"], expected["sampleWidthBytes"]
    ):
        raise ValueError(f"Unexpected WAV format: channels={channels}, rate={rate}, width={width}")
    duration = frames / rate
    if abs(duration - expected["durationSeconds"]) > 0.025:
        raise ValueError(f"Unexpected WAV duration: {duration:.3f}s")
    if width != 2:
        raise ValueError("Expected 16-bit signed PCM audio")
    samples = array("h")
    samples.frombytes(pcm)
    if sys.byteorder != "little":
        samples.byteswap()
    peak = max((abs(v) for v in samples), default=0)
    if peak < 100:
        raise ValueError("Reference is empty or silent")
    if not manifest.get("referenceText"):
        raise ValueError("Reference transcript is required for voice cloning")
    if manifest.get("origin") != "original-qwen3-tts-voice-design":
        raise ValueError("Only an original synthetic Qwen VoiceDesign reference is permitted")
    return {
        "status": "verified",
        "audio": str(audio_path),
        "sha256": digest,
        "durationSeconds": round(duration, 3),
        "sampleRateHz": rate,
        "peakPcm16": peak,
        "referenceText": manifest["referenceText"],
        "ownerFinalApproval": manifest.get("ownerFinalApproval", False),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audio", required=True, help="Private Qwen3 WAV; never commit it")
    parser.add_argument(
        "--manifest", default="config/narrator-reference.json", help="Tracked voice metadata"
    )
    args = parser.parse_args()
    print(json.dumps(validate_reference(args.audio, args.manifest), indent=2))


if __name__ == "__main__":
    main()