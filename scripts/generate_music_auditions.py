#!/usr/bin/env python3
"""Bharat Mode: three ORIGINAL synthesized score directions for owner audition.

No third-party samples, copyrighted melodies, paid APIs or voice synthesis.
Only source audio: owner-approved original synthetic narrator WAV for MIX demos.
DO NOT overwrite the repo's existing music; these are unapproved tests.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

RATE=24000
BPM=96
BEAT=60/BPM
NBEATS=32  # 8 bars, exactly 20 seconds
LENGTH=BEAT*NBEATS
N=int(round(RATE*LENGTH))
ROOT=Path(__file__).resolve().parents[1]
# Both paths can be overridden by a temporary Work Mode execution environment.
OUT=Path(os.environ.get('BHARAT_MUSIC_PREVIEW_OUT', str(ROOT/'out'/'music-auditions'))).expanduser()
VOICE=Path(os.environ.get('BHARAT_APPROVED_REFERENCE',str(ROOT/'out'/'private'/'bharat-mode-qwen-voice-audition.wav'))).expanduser()
OUT.mkdir(exist_ok=True,parents=True)
RNG=np.random.default_rng(12776)


def hz(midi):return 440*2**((midi-69)/12)

def synth(freq,t,dur,kind,vol=1):
    # unique non-looping, sample-by-sample deterministic original synthesis
    if kind=='pad':
        ph=2*np.pi*freq*t
        tone=(.66*np.sin(ph)+.19*np.sin(ph*2+.3)+.09*np.sin(ph*3+.6)+.18*np.sin(ph*1.003)+.10*np.sin(ph*.997))
        attack=np.minimum(1,t/.85)**1.3
        release=np.minimum(1,np.maximum(0,dur-t)/.8)**1.5
        return vol*tone*attack*release
    if kind=='rhodes':
        ph=2*np.pi*freq*t
        v=(np.sin(ph+1.6*np.exp(-4*t)*np.sin(2*ph))+.25*np.exp(-1.3*t)*np.sin(3*ph))
        env=(1-np.exp(-t/.013))*np.exp(-.8*t)*np.minimum(1,(dur-t)/.13)
        return vol*v*env
    if kind=='plucky':
        ph=2*np.pi*freq*t
        tone=np.sin(ph)+.24*np.sin(2*ph+1.1)+.11*np.sin(3*ph+.2)
        return vol*tone*(1-np.exp(-t/.005))*np.exp(-4.3*t)*np.clip((dur-t)/.07,0,1)
    if kind=='bell':
        ph=2*np.pi*freq*t
        tone=np.sin(ph)+.33*np.sin(2.003*ph)+.12*np.sin(3.99*ph)+.055*np.sin(5.49*ph)
        return vol*tone*(1-np.exp(-t/.008))*np.exp(-2.5*t)*np.clip((dur-t)/.16,0,1)
    if kind=='bass':
        ph=2*np.pi*freq*t
        tone=np.sin(ph)+.16*np.sin(2*ph+.9)+.07*np.sin(3*ph)
        return vol*tone*(1-np.exp(-t/.026))*np.exp(-1.1*t)*np.clip((dur-t)/.17,0,1)
    raise ValueError(kind)

def stereo_add(dest,start,dur,midi,kind,volume,pan=0):
    pos=int(round(start*RATE));n=min(int(round(dur*RATE)), N-pos)
    if pos<0 or n<=0:return
    t=np.arange(n,dtype=np.float32)/RATE
    sig=synth(hz(midi),t,dur,kind,volume)
    # energy-aware simple stereo panning
    theta=(np.clip(pan,-1,1)+1)*np.pi/4
    dest[pos:pos+n,0]+=sig*np.cos(theta)
    dest[pos:pos+n,1]+=sig*np.sin(theta)

def drum(dest,start,kind,volume):
    pos=int(round(start*RATE));
    if pos>=N:return
    dur={'kick':.52,'tick':.09,'shimmer':.11,'rim':.14,'snare':.15}[kind]
    n=min(int(dur*RATE),N-pos)
    t=np.arange(n,dtype=np.float32)/RATE
    if kind=='kick':
        freq=54+74*np.exp(-26*t)
        phase=2*np.pi*np.cumsum(freq)/RATE
        sig=(np.sin(phase)*np.exp(-15*t)+.045*np.exp(-75*t)*RNG.normal(size=n))*volume
    elif kind=='rim':
        sig=(.15*np.sin(2*np.pi*580*t)+RNG.normal(size=n)*.30)*np.exp(-32*t)*volume
    elif kind=='snare':
        white=RNG.normal(size=n).astype(np.float32)
        s=sosfilt(butter(2, [620,4900],fs=RATE,btype='bandpass',output='sos'),white)
        sig=(.32*s+.18*np.sin(2*np.pi*181*t))*np.exp(-31*t)*volume
    else:
        white=RNG.normal(size=n).astype(np.float32)
        band=sosfilt(butter(2,[2600,9800],fs=RATE,btype='bandpass',output='sos'),white)
        sig=band*volume*np.exp(-(41 if kind=='tick' else 26)*t)
    dest[pos:pos+n,0]+=sig*.68
    dest[pos:pos+n,1]+=sig*.72

def shimmer(sig,delay=.165,decay=.15):
    # very subtle short slap; adds space without burying words
    out=sig.copy()
    offset=int(delay*RATE)
    out[offset:,1]+=sig[:-offset,0]*decay
    offset2=int((delay*1.67)*RATE)
    out[offset2:,0]+=sig[:-offset2,1]*decay*.7
    return out

def polish(buf,mode):
    # Cut sub bass and upper harshness; airy pads, controlled centre
    out=np.empty_like(buf)
    for ch in range(2):
        x=sosfilt(butter(2,36,fs=RATE,btype='highpass',output='sos'),buf[:,ch])
        x=sosfilt(butter(2,6200,fs=RATE,btype='lowpass',output='sos'),x)
        out[:,ch]=x
    out=shimmer(out,decay=.16 if mode!=3 else .09)
    # Clip-safe gentle saturation, no aggressive compression
    out=np.tanh(out*.97)
    # Seam smoothing (generated phrase is continuous, taper preserves loop transition)
    fade=int(.24*RATE)
    out[:fade]*=np.linspace(.3,1,fade)[:,None]
    out[-fade:]*=np.linspace(1,.30,fade)[:,None]
    return out.astype(np.float32)

progressions={
  1:{'name':'Quiet Momentum','slug':'01-quiet-momentum','description':'Warm analog pad, gentle pulse, restrained piano tones. Editorial, modern, reassuring.',
    'chords':[[55,59,62,66],[50,57,62,64],[52,55,59,62],[48,55,59,62,64]],'bass':[43,38,40,36]},
  2:{'name':'Curious Discovery','slug':'02-curious-discovery','description':'Airy keys and glassy arpeggios; bright, intelligent and optimistic without hype.',
    'chords':[[48,52,55,59],[53,57,60,64],[45,52,55,59,60],[43,50,55,59,64]],'bass':[36,41,33,31]},
  3:{'name':'Built Forward','slug':'03-built-forward','description':'Firmer low-frequency groove and mechanical accents; confident and energetic.',
    'chords':[[50,53,57,60,64],[46,50,53,57],[53,57,60,67],[48,55,62,67]],'bass':[38,34,41,36]},
}


def compose(mode):
    cfg=progressions[mode];b=np.zeros((N,2),dtype=np.float32)
    chordLen=2*4*BEAT
    for ci,notes in enumerate(cfg['chords']):
        start=ci*chordLen
        if mode==1:
            # low-mid soft analog texture, anchored away from speech frequencies
            for i,note in enumerate(notes):stereo_add(b,start-.10 if ci else 0,chordLen+.27, note,'pad',.012,pan=(-.45 if i%2==0 else .42))
            for k in range(4):
                onset=start+k*2*BEAT
                stereo_add(b,onset,.72,notes[k%len(notes)]+12,'rhodes',.020,pan=.32 if k%2 else -.28)
                stereo_add(b,onset,.78,cfg['bass'][ci],'bass',.047)
            for k in range(4):drum(b,start+(k*2+.0)*BEAT,'tick',.020)
        elif mode==2:
            for i,note in enumerate(notes):stereo_add(b,start,chordLen+.20,note,'pad',.009,pan=(-.56 if i%2==0 else .55))
            for k in range(16):
                t=start+k*.5*BEAT
                note=notes[(k*3+ci)%len(notes)]+12+(12 if k%8==7 else 0)
                stereo_add(b,t,.70,note,'plucky',.010,pan=.40 if k%2 else -.40)
            for k in [0,2,4,6]:
                stereo_add(b,start+k*BEAT,.85,notes[(k//2)%len(notes)]+12,'bell',.011,pan=-.25)
            stereo_add(b,start,1.6,cfg['bass'][ci],'bass',.033)
            stereo_add(b,start+4*BEAT,1.5,cfg['bass'][ci],'bass',.029)
            for k in range(8):drum(b,start+k*BEAT,'shimmer',.012)
        else:
            for i,note in enumerate(notes):stereo_add(b,start,chordLen+.20,note,'pad',.0085,pan=(-.4 if i%2==0 else .40))
            for k in range(8):
                onset=start+k*BEAT
                bassNote=cfg['bass'][ci]+(7 if k==6 else 0)
                stereo_add(b,onset,.36,bassNote,'bass',.057)
                drum(b,onset,'kick',.050 if k%2==0 else .027)
                if k%2==1:drum(b,onset,'rim',.068)
                for j in range(2):drum(b,onset+j*.5*BEAT,'tick',.032 if j==0 else .021)
            for k in range(8):
                onset=start+(k+.5)*BEAT
                stereo_add(b,onset,.45,notes[(k*2+ci)%len(notes)]+12,'plucky',.016,pan=(-.28 if k%2==0 else .28))
    # hold enough space in narration band by preserving softer midrange
    return polish(b,mode)

voice = None
if VOICE.is_file():
    # The private, owner-approved synthetic reference is never included in Git.
    if hashlib.sha256(VOICE.read_bytes()).hexdigest()!='0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c':
        raise ValueError('Voice reference SHA mismatch: refusing to substitute another voice')
    voice,sr=sf.read(VOICE)
    if sr!=RATE or voice.ndim!=1:raise ValueError('Original reference must be 24 kHz mono WAV')
    voiceStart=int(1.2*RATE)
    voiceLength=len(voice)
    if voiceStart+voiceLength>=N:raise ValueError('Reference is too long for audition arrangement')
else:
    print('Private reference WAV not found; exporting ONLY original instrumental directions (no voice mix).')
manif=[]
for key,cfg in progressions.items():
    music=compose(key)
    # Norm integrated amplitude for similar audition levels, peak below -2dBFS
    musicRms=np.sqrt(np.mean(music**2))
    music=music*(0.046/max(musicRms,1e-8))
    music=np.tanh(music*.98).astype(np.float32)
    standalone=OUT/(cfg['slug']+'-music-only.wav')
    sf.write(standalone,music,RATE,subtype='PCM_16')
    track={ 'id':cfg['slug'], 'name':cfg['name'], 'description':cfg['description'], 'bpm':BPM,
      'durationSec':20.0, 'status':'audition_only_not_approved','originalMusic':True,
      'narratorSource':'owner-approved original synthetic Qwen3 reference; private WAV is optional',
      'musicFile':str(standalone),
      'rms':round(float(np.sqrt(np.mean(music**2))),5),
      'peakMusic':round(float(np.max(np.abs(music))),5),
      'musicSHA256':hashlib.sha256(standalone.read_bytes()).hexdigest()}
    if voice is not None:
        # 1.2s lead-in, same 7.6s approved narrator, then music continues solo.
        # Compare beds at equal voice level and modest music ducking.
        demo=music.copy()*0.78
        fade=int(.20*RATE)
        left=max(0,voiceStart-fade)
        right=min(N,voiceStart+voiceLength+fade)
        env=np.ones(N,dtype=np.float32)
        env[left:voiceStart]=np.linspace(1,.36,voiceStart-left)
        env[voiceStart:voiceStart+voiceLength]=.36
        env[voiceStart+voiceLength:right]=np.linspace(.36,1,right-(voiceStart+voiceLength))
        demo*=env[:,None]
        voiced=voice.astype(np.float32)*.85
        startFade=min(int(.045*RATE),len(voiced)//3)
        voiced[:startFade]*=np.linspace(0,1,startFade)
        voiced[-startFade:]*=np.linspace(1,0,startFade)
        demo[voiceStart:voiceStart+voiceLength,:]+=voiced[:,None]
        demo=np.tanh(demo*.95)
        mixed=OUT/(cfg['slug']+'-with-approved-narrator.wav')
        sf.write(mixed,demo,RATE,subtype='PCM_16')
        track.update(voiceMixFile=str(mixed),
          peakMix=round(float(np.max(np.abs(demo))),5),
          mixSHA256=hashlib.sha256(mixed.read_bytes()).hexdigest())
    manif.append(track)
    print(cfg['name'],track['peakMusic'],track.get('peakMix','no private narrator'),standalone.stat().st_size)
(OUT/'manifest.json').write_text(json.dumps({'project':'Bharat Mode','stage':'audition only, none approved','date':'2026-11-23','tracks':manif},indent=2)+'\n')
print('Generated:',len(manif),'tracks; voice mixes:', 'included' if voice is not None else 'not requested', OUT)