# BM-007 audio handoff — approved narration V2

Audio-only Work Mode task requested by owner on 28 November 2026. Read config/voice.json, config/narrator-reference.json, docs/AUDIO_ALIGNMENT.md, docs/PRODUCTION.md and production/source/BM-007/storyboard-v5/script.json. Use the exact original approved private narrator reference (SHA-256 0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c) with Qwen/Qwen3-TTS-12Hz-1.7B-Base pinned revision fd4b254389122332181a7c3db7f27e918eec64e3. Retrieve and verify privately before synthesis; no substitute voice, paid voice API, new VoiceDesign or fabricated timing. Clear international English, mature deep warm resonant documentary narrator, calm confidence, subtle enthusiasm and natural medium pace. Indian accent optional; correct Indian pronunciation mandatory. Pay attention to Vindhyagiri, Mazagon, Mumbai, Kolkata, Project Seventeen A, frigates and indigenous. Verify Indian names against reliable native pronunciation evidence where available. Do not paraphrase or add tagline. Record pronunciation-only synthesis input separately from canonical transcript. Provisional visual duration 55s is not a hard audio constraint; natural pacing and full words take precedence.

## Exact script

### Scene 1
The Indian Navy has received Vindhyagiri, completing the delivery of all seven homegrown stealth frigates under Project Seventeen A.

### Scene 2
Designed by the Indian Navy, these advanced stealth warships are a hundred and forty-nine metres long and weigh nearly six thousand seven hundred tonnes when fully loaded.

### Scene 3
Four were built at Mazagon Dock in Mumbai, and three at Garden Reach Shipbuilders in Kolkata.

### Scene 4
All seven were delivered over a span of about twenty-three months. The final ship took sixty-eight months to build, sixteen months less than the first.

### Scene 5
The programme achieved seventy-five percent indigenous content, involving more than two hundred micro, small and medium enterprises across India.

### Scene 6
From design to construction, the programme marks a major milestone in India's ability to build advanced warships at home.

## Acceptance

Six final individual 24 kHz mono PCM16 WAVs, actual measured durations, exact transcript offline ASR comparison and independent audible pronunciation review. Use real WhisperX acoustic alignment on each final WAV and strict transcript with scripts/align_qwen_words.py; every word has valid nonoverlapping in-range start/end and source final-audio-acoustic-alignment with final WAV SHA-256. No estimated timings. Regenerate alignment/hashes after any audio modification. Report unmet checks honestly. Keep private reference and generated audio outside Git. Deliver BM-007-narration.zip with scene-01.wav through scene-06.wav, matching alignment JSONs, script.json, checksums.sha256, transcript-qa.jsonl, alignment-qa.log, QA-notes.txt, generation manifest (model revision, reference checksum, synthesis settings and any phonetic input changes), durations per scene and total. Provide private self-contained HTML narration review player with six individual takes and full sequence plus usable audio fallback. No visuals, music mixing or video. No publication authorization implied.
