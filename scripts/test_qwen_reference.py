"""Standard-library regression checks for private narrator reference validation."""
import hashlib
import json
import struct
import sys
import tempfile
import unittest
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qwen_reference import validate_reference


class ReferenceChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.audio = base / "sample.wav"
        self.meta = base / "reference.json"
        with wave.open(str(self.audio), "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(24000)
            wav.writeframes(struct.pack("<" + "h" * 2400, *([500] * 2400)))
        self.record = {
            "sha256": hashlib.sha256(self.audio.read_bytes()).hexdigest(),
            "origin": "original-qwen3-tts-voice-design",
            "referenceText": "This is an original synthetic reference.",
            "audio": {"channels": 1, "sampleRateHz": 24000,
                      "sampleWidthBytes": 2, "durationSeconds": 0.1}
        }
        self.save()

    def save(self):
        self.meta.write_text(json.dumps(self.record), encoding="utf8")

    def test_valid(self):
        self.assertEqual(validate_reference(self.audio, self.meta)["sha256"], self.record["sha256"])

    def test_reject_changed_bytes(self):
        self.audio.write_bytes(self.audio.read_bytes() + b"x")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            validate_reference(self.audio, self.meta)

    def test_reject_voice_from_other_sources(self):
        self.record["origin"] = "other-source"
        self.save()
        with self.assertRaisesRegex(ValueError, "original synthetic"):
            validate_reference(self.audio, self.meta)

    def test_reject_wrong_transcript(self):
        self.record["referenceText"] = ""
        self.save()
        with self.assertRaisesRegex(ValueError, "transcript"):
            validate_reference(self.audio, self.meta)

    def test_reject_bad_format(self):
        self.record["audio"]["sampleRateHz"] = 44100
        self.save()
        with self.assertRaisesRegex(ValueError, "Unexpected WAV format"):
            validate_reference(self.audio, self.meta)

if __name__ == "__main__":
    unittest.main()