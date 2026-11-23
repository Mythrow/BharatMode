# Bharat Mode — Music & Sonic Identity

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
