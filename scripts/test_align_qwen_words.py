"""Offline contract regression tests; no pretrained acoustic weights required."""
import copy
import unittest
from align_qwen_words import build_alignment, canonical_words

AUDIO = {'sha256': '0123456789abcdef', 'durationSeconds': 4.0,
         'sampleRateHz': 24000, 'channels': 1}
SEGMENTS = [
    {'word': 'India', 'start': .12, 'end': .6, 'score': .95},
    {'word': 'is', 'start': .62, 'end': .8},
    {'word': 'building', 'start': .88, 'end': 1.5},
    {'word': 'more', 'start': 1.6, 'end': 2.1},
]

class TestAlignment(unittest.TestCase):
    def test_exact_word_contract(self):
        data = build_alignment('India is building more.', SEGMENTS, AUDIO)
        self.assertEqual(data['qa']['alignedWords'], 4)
        self.assertEqual(data['qa']['humanPronunciationReview'], 'PENDING')
        self.assertFalse(data['qa']['publishReady'])
        self.assertEqual(data['words'][2]['start'], .88)
    def test_punctuation_normalization(self):
        self.assertEqual(canonical_words("It's PARAM Rudra!"), ["it's", 'param', 'rudra'])
    def test_reject_missing_word(self):
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            build_alignment('India is building more.', SEGMENTS[:3], AUDIO)
    def test_reject_missing_time(self):
        x = copy.deepcopy(SEGMENTS)
        x[1].pop('start')
        with self.assertRaisesRegex(ValueError, 'Missing acoustic timing'):
            build_alignment('India is building more.', x, AUDIO)
    def test_reject_faked_overlap(self):
        x = copy.deepcopy(SEGMENTS)
        x[1]['start'] = .3
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            build_alignment('India is building more.', x, AUDIO)
    def test_reject_off_audio(self):
        x = copy.deepcopy(SEGMENTS)
        x[-1]['end'] = 9
        with self.assertRaisesRegex(ValueError, 'outside'):
            build_alignment('India is building more.', x, AUDIO)
    def test_reject_hallucinated_word(self):
        x = copy.deepcopy(SEGMENTS)
        x[2]['word'] = 'imagining'
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            build_alignment('India is building more.', x, AUDIO)
    def test_reject_zero_timestamps(self):
        x = copy.deepcopy(SEGMENTS)
        x[0]['end'] = x[0]['start']
        with self.assertRaisesRegex(ValueError, 'outside'):
            build_alignment('India is building more.', x, AUDIO)

if __name__ == '__main__':
    unittest.main()