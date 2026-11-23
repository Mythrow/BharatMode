"""Offline tests for the Qwen Base generated-WAV QA gate."""
from __future__ import annotations

import hashlib
import json
import math
import struct
import tempfile
import unittest
import wave
from pathlib import Path

from validate_qwen_base_output import validate_generated_audio


class TestBaseQa(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        d = Path(self.temp.name)
        self.wav = d / "audition.wav"
        self.man = d / "audition.json"
        self.ref = d / "reference.json"
        sr = 24000
        data = [int(8000 * math.sin(2 * math.pi * 150 * i / sr)) for i in range(sr * 2)]
        with wave.open(str(self.wav), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sr)
            f.writeframes(struct.pack("<" + "h" * len(data), *data))
        self.sha = hashlib.sha256(self.wav.read_bytes()).hexdigest()
        self.ref.write_text(json.dumps({"sha256": "a" * 64}))
        self.manifest = {
            "status": "generated_unreviewed", "published": False,
            "referenceSha256": "a" * 64, "audioSha256": self.sha,
            "durationSeconds": 2.0, "sampleRateHz": sr,
            "text": "A new narration line for Bharat Mode.",
        }
        self.store()

    def store(self):
        self.man.write_text(json.dumps(self.manifest))

    def validate(self):
        return validate_generated_audio(self.wav, self.man, self.ref)

    def test_good_file(self):
        obj = self.validate()
        self.assertEqual(obj["status"], "acoustic_file_qa_passed_human_review_pending")
        self.assertFalse(obj["voiceIdentityConfirmed"])

    def test_wrong_reference(self):
        self.manifest["referenceSha256"] = "b" * 64
        self.store()
        with self.assertRaisesRegex(ValueError, "reference"):
            self.validate()

    def test_wrong_audio_hash(self):
        self.manifest["audioSha256"] = "b" * 64
        self.store()
        with self.assertRaisesRegex(ValueError, "hash"):
            self.validate()

    def test_wrong_transcript_record(self):
        self.manifest["text"] = "  "
        self.store()
        with self.assertRaisesRegex(ValueError, "text"):
            self.validate()

    def test_wrong_duration(self):
        self.manifest["durationSeconds"] = 3.0
        self.store()
        with self.assertRaisesRegex(ValueError, "duration"):
            self.validate()

    def test_missing_audio(self):
        self.wav.unlink()
        with self.assertRaises(FileNotFoundError):
            self.validate()

    def test_no_publication_override(self):
        self.manifest["published"] = True
        self.store()
        with self.assertRaisesRegex(ValueError, "unpublished"):
            self.validate()

    def test_silence_detected(self):
        with wave.open(str(self.wav), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(24000)
            f.writeframes(b"\x00\x00" * 48000)
        self.manifest["audioSha256"] = hashlib.sha256(self.wav.read_bytes()).hexdigest()
        self.store()
        with self.assertRaisesRegex(ValueError, "silent"):
            self.validate()


if __name__ == "__main__":
    unittest.main()