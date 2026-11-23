"""Check authenticity and basic acoustic integrity of a Qwen Base audition WAV.

No speech recognition or speaker-identity proof is claimed: a human must listen to
both reference and output, and a separate ASR/forced alignment pass is needed.
Standard library only; this is a QA guard for the Work Mode Base test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import struct
import wave
from pathlib import Path


def validate_generated_audio(audio_path: str | Path, manifest_path: str | Path,
                             reference_manifest_path: str | Path) -> dict:
    audio_path = Path(audio_path)
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    reference = json.loads(Path(reference_manifest_path).read_text(encoding="utf-8"))
    if manifest.get("status") != "generated_unreviewed":
        raise ValueError("Unexpected output status; do not claim a reviewed narrator")
    if manifest.get("published") is not False:
        raise ValueError("Base audition must remain unpublished pending review")
    if manifest.get("referenceSha256") != reference.get("sha256"):
        raise ValueError("The Base output was not linked to our verified reference WAV")
    text = manifest.get("text")
    if not isinstance(text, str) or len(text.strip()) < 12:
        raise ValueError("Missing or implausibly short generated-text record")
    if not audio_path.is_file():
        raise FileNotFoundError(f"No actual WAV generated: {audio_path}")
    audio_sha = hashlib.sha256(audio_path.read_bytes()).hexdigest()
    if manifest.get("audioSha256") != audio_sha:
        raise ValueError("Generated WAV hash does not match the output manifest")
    with wave.open(str(audio_path), "rb") as handle:
        channels, framerate, width, frames = (
            handle.getnchannels(), handle.getframerate(), handle.getsampwidth(),
            handle.getnframes()
        )
        if handle.getcomptype() != "NONE" or width != 2 or channels != 1:
            raise ValueError("Expected mono uncompressed PCM16 WAV")
        if framerate != 24000 or frames <= 0:
            raise ValueError("Expected nonempty 24 kHz output")
        duration = frames / framerate
        pcm = handle.readframes(frames)
    if duration < 1.5 or not math.isfinite(duration):
        raise ValueError("Generated speech output too short or invalid")
    if abs(float(manifest.get("durationSeconds", 0)) - duration) > 0.015:
        raise ValueError("Generated waveform duration differs from manifest")
    if manifest.get("sampleRateHz") != framerate:
        raise ValueError("Sample rate does not match manifest")
    # Stream unpacking is fine for the deliberately short audition. No NumPy needed.
    values = struct.unpack("<" + "h" * frames, pcm)
    rms = math.sqrt(sum(v * v for v in values) / frames) / 32768
    peak = max(abs(v) for v in values) / 32768
    if peak < 0.005 or rms < 0.001:
        raise ValueError("Generated audio is effectively silent")
    clipping = sum(abs(v) >= 32760 for v in values) / frames
    if clipping > 0.025:
        raise ValueError("Audio has excessive clipping (over 2.5% of samples)")
    return {
        "status": "acoustic_file_qa_passed_human_review_pending",
        "audioSha256": audio_sha,
        "referenceSha256": reference["sha256"],
        "durationSeconds": round(duration, 3),
        "sampleRateHz": framerate,
        "rms": round(rms, 5),
        "peak": round(peak, 5),
        "clippedSampleFraction": round(clipping, 5),
        "text": text,
        "voiceIdentityConfirmed": False,
        "transcriptConfirmed": False,
        "pronunciationConfirmed": False,
        "safeForPublication": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audio", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--reference-manifest", type=Path,
                        default=Path(__file__).resolve().parents[1] / "config/narrator-reference.json")
    args = parser.parse_args()
    print(json.dumps(validate_generated_audio(args.audio, args.manifest, args.reference_manifest), indent=2))


if __name__ == "__main__":
    main()