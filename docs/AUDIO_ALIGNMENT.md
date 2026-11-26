# Bharat Mode — Qwen narration to approved V6 captions

**Current status:** approved Qwen Base reference and real acoustic alignment have been used in episode production. Verify fresh inputs per story; the reusable native renderer remains an engineering candidate until real-input render QA passes.

## Inputs and safety checks

1. Synthesize the final narration WAV using our original synthetic Qwen voice reference. Use the owner-approved Base reference and pinned model; verify SHA and listening QA each time.
2. Use **the final audio** and the exact approved spoken transcript, not a draft or a manually estimated timing file. Run the open-source WhisperX alignment engine on permitted compute. It needs its own downloaded aligner weights (and may require a separate compatible Python environment from Qwen3-TTS).
3. `scripts/align_qwen_words.py` obtains acoustic word starts and ends from the waveform and writes a JSON file with the final WAV's SHA-256, measured duration and strict word matches. If the aligner misses a word, returns no timestamp, overlaps words, invents a different word or yields out-of-audio positions, the script **fails** instead of manufacturing timestamps.
4. A passing alignment **does not prove that the voice actually pronounced the right words**; forced alignment is conditioned on the supplied transcript. Complete a listening/ASR pronunciation review separately, especially `PARAM Rudra`, before publication.
5. `src/aligned-caption-timing.js` only accepts the schema marked `source: "final-audio-acoustic-alignment"`. It creates natural short phrase groups from those *existing timestamps*. `src/aligned-captions.jsx` renders the owner-approved centered, translucent one-line caption box and 0.2s per-word pop. **Neither file changes the approved V6 frame geometry.**

## Work/cloud execution example (not for the channel owner to run locally)

```bash
# Inside a permitted Work/cloud environment that has WhisperX installed:
python scripts/align_qwen_words.py \
  --audio out/qwen-base/narrator-consistency.wav \
  --text "Across India, researchers are using advanced computing to study harder scientific problems. What happens when more laboratories gain access to this technology?" \
  --output out/alignments/narrator-consistency.json \
  --device cpu
```

**No output is committed to public GitHub**. Generated WAVs, aligned timestamps and videos stay in ignored `out/` or private storage. Copy the exact approved new-line narration from the actual Base generation manifest for consistency.

Integration API for the approved frame once a genuine alignment is generated:

```jsx
import {AlignedNarrationCaptions} from './aligned-captions.jsx';

<ApprovedShortsFrame
  theme={theme}
  topic={topic}
  chapters={chapters}
  timeSec={timeSec}
  caption={<AlignedNarrationCaptions alignment={alignment} timeSec={timeSec} theme={theme}/>}
>
  {visuals}
</ApprovedShortsFrame>
```

The `BharatShort` composition now uses the native production contract; `src/short.jsx` is legacy. See [renderer contract](RENDERER_CONTRACT.md). For a full multi-scene Short, use one verified alignment per generated audio segment or a complete final soundtrack with correct global timestamp offsets; do not silently reuse timestamps from a different recording.

## Historical test evidence (23 November; not the current audit CI result)

- `python -m unittest discover -s scripts -p 'test_align_qwen_words.py'`: 8 pure-code passing cases, including exact match and rejection paths.
- `node scripts/test-aligned-caption-timing.mjs`: passing phrase segmentation/timing validation checks.
- Real 7.6-second Qwen reference inspected separately: 24 kHz mono, SHA-256 `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c` (matches reference manifest). **No fake word timings were created for this WAV**.
- The WhisperX acoustic engine was **not downloaded/executed** in this chat. Qwen Base model inference and resulting narration are also not executed here.

## Acceptance before publishing

A genuine reference-consistent voice generation, a real acoustic alignment, all words present and reasonably timed, pronounced `PARAM` correctly, no clipped captions, V6 frame safe areas and progress centering preserved, audio ducking and evidence QA, review on an actual phone.