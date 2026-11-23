# Bharat Mode — Music & Sonic Identity

## MUSIC-05 — Deep Current (current audition, 23 November 2026)

**Latest owner feedback:** MUSIC-04's hip-hop groove was rejected. The user wants **modern techno with a deeper melody and basslines instead of high-key instruments**. MUSIC-01 remains rejected as too simple; MUSIC-02's melodic appeal and MUSIC-03's rhythmic strength informed this newer direction.

A newly synthesized, **original melodic-techno audition** uses a 124 BPM four-on-the-floor pulse, sustained F-minor warmth, low/mid-register analog-synth motif, rolling harmonically rich bass and restrained high-frequency percussion. **No hip-hop swing, bright piano lead or third-party samples**. Working name: MUSIC-05 Deep Current.

- Length **30.968 seconds**, 44,100 Hz stereo PCM16. Music-only WAV SHA-256: `50a7ab8280198bbfbab8323aae19c1aad2dce06a0c52ff2182ec10a1cf8db9fe`, peak 0.352.
- Mixed with approved private Qwen narrator, offset 2.75 s and ducking the music during speech. Narration-mixed WAV SHA-256: `d3a42db52ddd1970135881154082809ef28cebbbc6e7e265f3931daa05ff9e90`, peak 0.834. The narrator source was SHA-verified as `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`.
- Two MP3 audition previews delivered in chat; previews and WAVs **not tracked in Git**. Reproducible composition source is `scripts/generate_melodic_techno_audition.py`; uses numpy/scipy/soundfile and optional private Qwen reference. Generate with `python scripts/generate_melodic_techno_audition.py`, optionally setting `BHARAT_APPROVED_REFERENCE` and `BHARAT_MUSIC05_OUTPUT`.
- File generation, syntax, readback, duration and peak/clipping checks passed. **This is a candidate only. Owner listening, stereo/phone QA, loudness mastering, transition compatibility and seamless extended looping are NOT yet approved or tested.**
- The older `public/music/ambient.wav` and two SFX assets remain **provisional, unchanged**; approved V6 visuals and Qwen narrator identity remain unchanged. Do not select/replace final music until owner reacts to MUSIC-05.


## Previous owner direction — Lo-fi hip-hop MUSIC-04 (rejected after audition) (23 November 2026)

The owner **rejected MUSIC-01 Quiet Momentum** as too boring/simple, **liked the beats of MUSIC-03 Built Forward** and **liked the melody/tune of MUSIC-02 Curious Discovery**, and asked for a combination using **lo-fi beats**. This is preference feedback, **not final approval** of any track.

Produced **MUSIC-04 Lo-Fi Motion**: an original 92 BPM, 12-bar (31.304-second) stereo arrangement in an optimistic jazzy/chill lo-fi hip-hop style. It has a rhythmic, syncopated kick/snare pocket, swung hi-hats, warm Rhodes-style keyboard chords, a brighter recurring upper melody, subtle tape noise and a melodic bassline. The groove starts promptly; voice-mixed audition puts the **same approved synthetic Qwen reference** at ~2.25 seconds with a ducked score behind the speech. Nothing is copied from an existing artist or copyrighted song.

- **Music-only WAV SHA-256:** `81a6f75030d329c67193bf16da1d07a96561543627cff200c458377d8a26972c`.
- **Narrator-mixed WAV SHA-256:** `33bd302a9ca40d338bda98aa94347e6a5db873e774bc63c6b785d2a9f5b3cde1`; narrator source matches privately approved reference SHA `0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c`.
- **Audio:** 44.1 kHz stereo, PCM16, 31.304 sec, peak music ~0.521 FS, peak mixed ~0.755 FS; no clipping. MP3 narrated/instrumental preview copies also generated for listening. Final loudness, seamless looping, edit responsiveness, sound identity and phone-speaker mix are still unapproved/unverified.
- **Reproduce:** `python scripts/generate_lofi_audition.py`. With environment variable `BHARAT_APPROVED_REFERENCE` pointed to the exact approved private synthetic reference WAV, the generator also produces the voice comparison. `BHARAT_LOFI_OUT` changes the output directory. No voice or music-preview binaries are stored in Git.
- **Owner decision pending:** listen to MUSIC-04 with narration and music-only. Refine groove or melody as requested. **Do not** replace `public/music/ambient.wav` or existing SFX until owner approves and full-length, narration-first final masters have been mixed and checked.



**Status: THREE ORIGINAL AUDITIONS READY — NOT OWNER-APPROVED.**  
**Date:** 23 November 2026. Music approval now precedes BM-0003's first publishable voiced V6 render.  
**Approved and unchanged:** V6 visual design and the original Qwen3-TTS synthetic narrator.

## Why this gate exists

Bharat Mode needs an audible signature that feels informative, premium, optimistic and credible without overwhelming its mature documentary narrator. Background music should communicate curiosity and forward motion, **not** triumphalist marching-band, generic stock-tech EDM, patriotic anthem tropes or dramatic news stings. Scripts should begin immediately; no mandatory musical intro.

The tracked `public/music/ambient.wav` (9.6 sec) and existing `public/sfx/metric-rise.wav` and `public/sfx/mode-on.wav` were programmatically generated as **development placeholders**. Their presence in the repository does not mean their final sound is approved. **Do not replace these masters until the owner selects a direction.**

## Audition candidates (23 November 2026)

All are original synthesized compositions made with no third-party musical samples or paid generation services. The audition generator source is `scripts/generate_music_auditions.py`. No external music or artist recordings were used.

| ID | Working name | Emotional role | Typical editorial fit |
| --- | --- | --- | --- |
| MUSIC-01 | **Quiet Momentum** | Warm pads, light pulse and sparse keyboard, least intrusive | Narrative science, measured progress, policy context |
| MUSIC-02 | **Curious Discovery** | Airy keys and small glass-like motifs, positive and investigative | Inventions, research, lab breakthroughs |
| MUSIC-03 | **Built Forward** | More pronounced restrained rhythmic pulse and low bass | Engineering, infrastructure, applied technology |

**Audition arrangement:** each is a 20-second stereo, 24 kHz PCM16 preview at 96 BPM (32 beats), with a separate instrumental-only WAV and a narrated comparison WAV/MP3. Comparison places **the same exact owner-approved 7.6-second Qwen3 reference speech at 1.2 seconds** over music, then leaves the rest instrumental. Music is reduced during speech (audition prototype uses ~36% of instrumental level, after a separate mix-level factor), fades gently around speech and peaks below full scale. This is **not** a finished mix, loudness master, gapless loop, or proof that the dynamic range will work on every speaker.

Generated audio preview files are deliberately **outside Git**; available as attachments/links in the music audition chat. The code can reproduce WAVs in a permitted Work Mode environment. The optional narrator reference is private and validated by SHA-256; no voice files should be committed. Instrumental previews can be generated without private reference.

## Owner listening decision — PENDING

Before choosing, compare every option with the narrator **and** instrumental-only. Select one preferred core direction or a blended direction (for example, MUSIC-01 base with MUSIC-02's bright motif). Distinguish what makes a suitable common brand sound from what must change by episode. **Do not freeze a melody, claim approval, replace the existing audio, or publish a video without owner feedback.**

Suggested sound system to approve in the next iteration:

1. **One coherent sonic palette**, flexible in intensity for science/people/engineering videos rather than a different unrelated theme each Short.
2. **Narration-first mix:** use real voice to set ducking and EQ, then check phone speaker intelligibility. Set integrated loudness and true peak only after evaluation; avoid heavy sub-bass and frequencies that fight speech.
3. **Story-beat accents:** minimal transitions and data/SFX, not a hit every subtitle word. The existing two SFX are prototypes, not approved finals.
4. **Recognizable closing motif** (optional very brief `Mode: ON` sonic punctuation), no loud logo splash or mandatory long intro.
5. **Duration-aware, seamless arrangement:** create suitable 35–55-second or script-fit extended loops/variations after a direction is chosen. The 20-second audition loops are not validated as seamless.
6. **Rights:** preserve original source code and final selected original masters in Git; generated voice and full MP4s excluded. Review platform content/music policies before publication.

## Reproduce audition files (for agent/Work use; not a user-side setup task)

The generator uses Python `numpy`, `scipy`, and `soundfile`; it performs procedural composition and WAV writing. No music API, payment or external track download.

- `python scripts/generate_music_auditions.py` produces three **music-only** test WAVs in the ignored `out/music-auditions/` folder.
- Set `BHARAT_APPROVED_REFERENCE` to a private original synthetic Qwen WAV (matching `config/narrator-reference.json`) before running to get the three voice-mixed audition WAVs as well; set `BHARAT_MUSIC_PREVIEW_OUT` to change the output folder.
- Agent must check generated duration (20 seconds), two-channel 24 kHz PCM16 properties, audible quality, clipping and spectral space under narration. Do not present a procedural composition as professionally mastered or use the preview as the official episode score without owner approval.

**Tests completed 23 Nov:** all three standalone and three narrated 20-second WAVs generated successfully; audio readback verified shape (480,000 frames × two channels at 24 kHz), finite values and sub-clipping peaks. A separate run without the private reference produced **only** three instrumental files, as intended. Generator Python compilation passed. Human/phone music QA and final publishing soundtrack approval are pending.

## Relationship to content

The owner selected [BM-0003 — L&T Chennai AI infrastructure](../content/research/BM-0003.md) as the next video trial. That story remains **In Progress**, not published. Finish the sonic identity choice, then use the selected mix direction under our approved Qwen narrator in the rights-checked V6 video. `BM-0001` PARAM Rudra remains a separate in-progress production pilot.
