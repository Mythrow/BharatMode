#!/usr/bin/env python3
"""Bharat Mode MUSIC-06 narrator-ducking *test only* (not episode audio).
Uses the owner-approved Option B faders from config/music.json.

This uses existing user-supplied/private media; does not synthesize a voice or pay APIs.
Requires ffmpeg, numpy, scipy and soundfile. Audio previews remain outside Git.

Usage:
  python scripts/preview_signature_mix.py --music /path/to/private/music.mp3 \
      --voice /path/to/private/approved.wav --out out/music-mix
"""
import argparse, hashlib, json, subprocess, wave
from pathlib import Path
import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

MUSIC_SHA='adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9'
VOICE_SHA='0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c'
SR=44100
DEMO_DURATION=20.0
VOICE_START=2.0

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as file:
        for block in iter(lambda:file.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def mp3_stereo_float(path,seconds):
    data=subprocess.check_output(['ffmpeg','-hide_banner','-loglevel','error','-i',str(path),'-t',str(seconds),'-vn','-ac','2','-ar',str(SR),'-f','f32le','pipe:1'])
    samples=np.frombuffer(data,dtype='<f4').reshape(-1,2).copy()
    needed=round(seconds*SR)
    if len(samples)<needed:raise ValueError('Music must last at least the preview duration')
    return samples[:needed]

def voice_float(path):
    with wave.open(str(path),'rb') as w:
        if (w.getnchannels(),w.getsampwidth(),w.getframerate())!=(1,2,24000):raise ValueError('Expected verified mono 24 kHz PCM16 narrator')
        raw=w.readframes(w.getnframes())
    mono=np.frombuffer(raw,dtype='<i2').astype(np.float32)/32768.0
    return resample_poly(mono,147,80).astype(np.float32)

def smooth_duck(activity):
    # Speech-aware envelope with fast duck and 280ms release, no audible pumping.
    out=np.empty_like(activity,dtype=np.float32)
    pos=0.0
    attack=np.exp(-1.0/(SR*0.024))
    release=np.exp(-1.0/(SR*0.28))
    for i,v in enumerate(activity):
        decay=attack if v>pos else release
        pos=pos*decay+float(v)*(1-decay)
        out[i]=pos
    return out

def render(music,voice,outdir):
    for name,expected in [(music,MUSIC_SHA),(voice,VOICE_SHA)]:
        got=digest(name)
        if got!=expected:raise ValueError(f'Source SHA mismatch {name}: {got}')
    # Standard reference balance selected by the channel owner: Option B.
    settings=json.loads((Path(__file__).resolve().parents[1]/'config/music.json').read_text(encoding='utf-8')).get('approvedMix')
    if not settings or settings.get('preset')!='B':
        raise ValueError('Owner-approved MUSIC-06 mixer preset B is required')
    v_gain=float(settings['voice'])/100.0
    base_gain=float(settings['musicBetweenSpeech'])/100.0
    ducked_gain=float(settings['musicDuringSpeech'])/100.0
    if not (0 < ducked_gain <= base_gain <= 1 and 0 < v_gain <= 1):
        raise ValueError('Approved mixer gains must satisfy 0 < ducked <= base <= 1 and 0 < voice <= 1')
    outdir.mkdir(parents=True,exist_ok=True)
    bed=mp3_stereo_float(music,DEMO_DURATION)
    speech=voice_float(voice)
    count=len(bed)
    start=round(VOICE_START*SR)
    if start+len(speech)>count:raise ValueError('Voice too long for demo')
    voice_track=np.zeros((count,2),dtype=np.float32)
    voice_track[start:start+len(speech),:]=speech[:,None]*v_gain
    # RMS activity gate over short periods. 24ms attack, 280ms release.
    activity=np.zeros(count,dtype=np.float32)
    # Keep activity during the authenticated vocal clip, not its silent tails.
    absvoice=np.abs(speech)
    window=round(.035*SR)
    smoothed=np.convolve(absvoice,np.ones(window,dtype=np.float32)/window,'same') if len(speech)<SR*12 else absvoice
    activity[start:start+len(speech)]=(smoothed>0.013).astype(np.float32)
    envelope=smooth_duck(activity)
    ramp=np.minimum(1,np.arange(count,dtype=np.float32)/(SR*.36))
    fade=np.minimum(1,(count-np.arange(count,dtype=np.float32))/(SR*.8))
    # Dynamically interpolate from approved normal music 55/100 to speech 32/100.
    # The music remains audible beneath the approved 88/100 narrator level.
    music_gain=(base_gain+(ducked_gain-base_gain)*envelope)*ramp*np.clip(fade,0,1)
    mixed=bed*music_gain[:,None]+voice_track
    peak=float(np.max(np.abs(mixed)))
    if peak>0.98:raise ValueError(f'Mix clips or has inadequate headroom: {peak}')
    if not np.isfinite(mixed).all():raise ValueError('Nonfinite waveform')
    wav=outdir/'BM-MUSIC-06-voice-mix-test.wav'
    mp3=outdir/'BM-MUSIC-06-voice-mix-test.mp3'
    sf.write(wav,mixed,SR,subtype='PCM_16')
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(wav),'-codec:a','libmp3lame','-b:a','192k',str(mp3)],check=True)
    summary={'status':'technical_music_voice_demo_NOT_BM0003_narration','purpose':'check selected music and approved narrator coexist before full story production','musicSha256':MUSIC_SHA,'voiceSha256':VOICE_SHA,'durationSeconds':DEMO_DURATION,'voiceStartSeconds':VOICE_START,'sampleRateHz':SR,'peakFloatBeforeEncode':peak,'ducking':'owner-approved option B: voice 88/100, music 55/100 between speech and 32/100 during active speech; 24ms attack/280ms release', 'approvedMixPreset':'B', 'stemGains':{'voice':v_gain,'musicNormal':base_gain,'musicDuringSpeech':ducked_gain},'wavSha256':digest(wav),'mp3Sha256':digest(mp3),'fullNarrationGenerated':False,'v6Rendered':False,'publicationApproved':False}
    (outdir/'preview-manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--music',required=True,type=Path)
    p.add_argument('--voice',required=True,type=Path)
    p.add_argument('--out',required=True,type=Path)
    args=p.parse_args()
    print(json.dumps(render(args.music,args.voice,args.out),indent=2))