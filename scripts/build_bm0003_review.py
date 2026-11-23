"""Build the Option B mix and frame-accurate pilot props from checked scene media."""
import argparse
import json
import math
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

from align_qwen_words import wav_metadata
from preview_signature_mix import MUSIC_SHA, SR, digest, smooth_duck, voice_float
from validate_qwen_base_output import validate_generated_audio

ROOT = Path(__file__).resolve().parents[1]
FPS = 30


def build(voice_dir, music, output):
    if digest(music) != MUSIC_SHA:
        raise ValueError("MUSIC-06 hash mismatch")
    story = json.loads((ROOT / "stories/lt-chennai-ai-cluster-order.json").read_text())["story"]
    alignments, tracks = [], []
    frames = 0
    for i, scene in enumerate(story["scenes"]):
        wav = voice_dir / f"{i:02}.wav"
        meta = validate_generated_audio(wav, wav.with_suffix(".json"), ROOT / "config/narrator-reference.json")
        aligned = json.loads((voice_dir / f"{i:02}-alignment.json").read_text())
        if (aligned["audio"] != wav_metadata(wav) or aligned["transcript"] != scene["narration"]
                or meta["text"] != scene["narration"]):
            raise ValueError(f"Scene {i+1} audio or transcript does not match")
        alignments.append(aligned)
        speech = voice_float(wav)
        count = math.ceil(len(speech) * FPS / SR) + 8
        tracks.append(np.pad(speech, (0, count * (SR // FPS) - len(speech))))
        frames += count
        scene["duration"] = count / FPS

    voice = np.concatenate(tracks)
    elapsed = frames / FPS
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-stream_loop", "-1", "-i", str(music),
                                   "-t", f"{elapsed:.8f}", "-ar", str(SR), "-ac", "2",
                                   "-f", "f32le", "pipe:1"])
    bed = np.frombuffer(raw, dtype="<f4").reshape(-1, 2)
    if abs(len(bed)-len(voice)) > 1:
        raise ValueError("Music length differs from frame timeline")
    bed = np.pad(bed, ((0, max(0, len(voice)-len(bed))), (0,0)))[:len(voice)]
    activity = uniform_filter1d(np.abs(voice), size=round(.035*SR), mode="constant") > .013
    duck = smooth_duck(activity)
    clock = np.arange(len(voice)) / SR
    fade = np.minimum(1, clock/.36) * np.clip((elapsed-clock)/.7, 0, 1)
    preset = json.loads((ROOT / "config/music.json").read_text())["approvedMix"]
    normal = preset["musicBetweenSpeech"] / 100
    ducked = preset["musicDuringSpeech"] / 100
    gain = (normal - (normal - ducked) * duck) * fade
    mix = voice[:,None] * (preset["voice"] / 100) + bed * gain[:,None]
    peak = float(np.max(np.abs(mix)))
    if not np.isfinite(mix).all():
        raise ValueError("Mix is not finite")
    master_gain = min(1.0, .92/max(peak, .01))
    output.mkdir(parents=True, exist_ok=True)
    sf.write(output / "mix.wav", mix*master_gain, SR, subtype="PCM_16")
    (output / "props.json").write_text(json.dumps({"story":story,"alignments":alignments}))
    print(json.dumps({"frames":frames,"duration":elapsed,"peak":peak*master_gain,
                      "masterGain":master_gain,"words":sum(len(a["words"]) for a in alignments)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--voice-dir", type=Path, required=True)
    parser.add_argument("--music", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.voice_dir, args.music, args.output)
