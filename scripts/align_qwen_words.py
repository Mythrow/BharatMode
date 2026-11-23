"""Align completed Qwen narration WAV to its approved transcript using local WhisperX.

No paid APIs. This script does *not* fabricate timings from text length: it invokes
an acoustic aligner on the actual waveform and rejects missing/misaligned words.
Install the open-source dependencies in a permitted execution environment.

Run one narration/scene at a time; output is an untracked alignment JSON.
A successful alignment is NOT proof the TTS correctly spoke the transcript;
pronunciation and audible transcript must still be reviewed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import wave
from pathlib import Path

_WORD_PATTERN = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*", re.UNICODE)


def canonical_words(text: str) -> list[str]:
    # The same tokenizer is used on approved text and aligner output. Unicode
    # normalization is deliberately conservative to catch skipped narration.
    return [m.group(0).casefold().replace('’', "'") for m in _WORD_PATTERN.finditer(text)]


def wav_metadata(audio_path: Path) -> dict:
    audio_path = Path(audio_path)
    with wave.open(str(audio_path), 'rb') as handle:
        if handle.getcomptype() != 'NONE':
            raise ValueError('Only uncompressed PCM WAV is supported')
        channels, rate, frames = handle.getnchannels(), handle.getframerate(), handle.getnframes()
        if channels != 1 or rate <= 0 or frames <= 0:
            raise ValueError('Expected a nonempty mono PCM WAV')
        duration = frames / rate
    return {
        'sha256': hashlib.sha256(audio_path.read_bytes()).hexdigest(),
        'durationSeconds': round(duration, 6),
        'sampleRateHz': rate,
        'channels': channels,
    }


def build_alignment(transcript: str, word_segments: list[dict], audio: dict,
                    *, aligner: str = 'whisperx') -> dict:
    expected = canonical_words(transcript)
    if not expected:
        raise ValueError('Empty approved transcript')
    if not isinstance(word_segments, list) or not word_segments:
        raise ValueError('No acoustic word segments found; do not estimate timestamps')
    actual = []
    words = []
    duration = float(audio['durationSeconds'])
    last_end = -1.0
    for i, segment in enumerate(word_segments):
        raw = str(segment.get('word', segment.get('text', ''))).strip()
        tokens = canonical_words(raw)
        if len(tokens) != 1:
            raise ValueError(f'Word {i} is absent or ambiguously split: {raw!r}')
        if segment.get('start') is None or segment.get('end') is None:
            raise ValueError(f'Missing acoustic timing for word {i}: {raw!r}')
        start, end = float(segment['start']), float(segment['end'])
        if not all(math.isfinite(x) for x in (start, end)):
            raise ValueError(f'Non-finite time for word {i}')
        if start < 0 or end <= start or end > duration + 0.025:
            raise ValueError(f'Word {i} falls outside the final audio')
        if start + 0.025 < last_end:
            raise ValueError(f'Word {i} overlaps a previous acoustic word')
        last_end = end
        actual.append(tokens[0])
        item = {'text': raw, 'start': round(start, 3), 'end': round(end, 3)}
        if segment.get('score') is not None:
            score = float(segment['score'])
            if not math.isfinite(score):
                raise ValueError('Non-finite aligner confidence')
            item['score'] = round(score, 4)
        words.append(item)
    if actual != expected:
        first_bad = next((i for i in range(min(len(expected), len(actual)))
                          if actual[i] != expected[i]), min(len(expected), len(actual)))
        raise ValueError(f'Alignment text mismatch at word {first_bad}: '
                         f'expected {expected[first_bad:first_bad+2]}, '
                         f'got {actual[first_bad:first_bad+2]}')
    if words[0]['start'] > min(duration * 0.6, 2.0):
        raise ValueError('Unusually large leading gap; manual review required')
    return {
        'schemaVersion': 1,
        'source': 'final-audio-acoustic-alignment',
        'aligner': aligner,
        'transcript': transcript,
        'audio': audio,
        'words': words,
        'qa': {
            'approvedTextWords': len(expected),
            'alignedWords': len(words),
            'exactWordMatch': True,
            'humanPronunciationReview': 'PENDING',
            'asrTranscriptReview': 'PENDING',
            'publishReady': False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audio', required=True, help='Final untracked narration PCM WAV')
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument('--text', help='Exact final spoken transcript')
    src.add_argument('--text-file', type=Path, help='UTF-8 file with exact final transcript')
    parser.add_argument('--output', type=Path, required=True, help='Untracked alignment JSON')
    parser.add_argument('--device', choices=['cpu', 'cuda'], default='cpu')
    args = parser.parse_args()

    audio_path = Path(args.audio)
    transcript = args.text if args.text is not None else args.text_file.read_text(encoding='utf-8').strip()
    metadata = wav_metadata(audio_path)
    # Lazy heavy imports preserve --help and unit tests without downloads.
    import whisperx
    waveform = whisperx.load_audio(str(audio_path))
    model, meta = whisperx.load_align_model(language_code='en', device=args.device)
    aligned = whisperx.align(
        [{'start': 0.0, 'end': metadata['durationSeconds'], 'text': transcript}],
        model, meta, waveform, args.device, return_char_alignments=False,
    )
    output = build_alignment(transcript, aligned.get('word_segments', []), metadata)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({
        'output': str(args.output), 'words': len(output['words']),
        'audioSha256': metadata['sha256'], 'humanReviewRequired': True,
    }))


if __name__ == '__main__':
    main()