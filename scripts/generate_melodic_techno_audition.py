#!/usr/bin/env python3
"""Bharat Mode MUSIC-05: original modern melodic techno soundtrack audition.

Procedurally written notes, drums and synths; no copyrighted samples, loops,
third-party source recordings, external music generators, subscriptions or APIs.
Owner has NOT yet approved the soundtrack. V6 visual files are untouched.

Optional environment variables:
  BHARAT_MUSIC05_OUTPUT: output directory (default out/music-05/ under repo root)
  BHARAT_APPROVED_REFERENCE: approved private synthetic Qwen WAV (SHA validated)
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, resample_poly, sosfilt

SR=44100
BPM=124
BEAT=60.0/BPM
BAR=4*BEAT
BARS=16
DURATION=BARS*BAR
N=int(round(SR*DURATION))
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(os.environ.get('BHARAT_MUSIC05_OUTPUT', str(ROOT/'out'/'music-05'))).expanduser()
VOICE=Path(os.environ.get('BHARAT_APPROVED_REFERENCE',str(ROOT/'out'/'private'/'bharat-mode-qwen-voice-audition.wav'))).expanduser()
VOICE_SHA='0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c'
RNG=np.random.default_rng(20261123+5)


def hz(m):return 440*2**((m-69)/12)

def put(buf,start,sig,pan=0):
    i=max(0,round(start*SR)); skip=max(0,-round(start*SR))
    sig=np.asarray(sig,dtype=np.float32)
    n=min(len(buf)-i,len(sig)-skip)
    if n<=0:return
    l=math.cos(math.pi*(float(pan)+1)/4)*math.sqrt(2)
    r=math.sin(math.pi*(float(pan)+1)/4)*math.sqrt(2)
    buf[i:i+n,0]+=sig[skip:skip+n]*l
    buf[i:i+n,1]+=sig[skip:skip+n]*r


def signal(length):return np.arange(round(length*SR),dtype=np.float32)/SR


def hp(y,cut):return sosfilt(butter(2,cut,fs=SR,btype='highpass',output='sos'),y).astype(np.float32)

def lp(y,cut):return sosfilt(butter(2,cut,fs=SR,btype='lowpass',output='sos'),y).astype(np.float32)


def kick(v=1):
    t=signal(.43)
    f=47+139*np.exp(-37*t) # tight low techno floor kick: 47-65 Hz tail
    phase=2*np.pi*np.cumsum(f)/SR
    click=hp(RNG.standard_normal(len(t)).astype(np.float32),1800)*np.exp(-130*t)*.018
    body=np.sin(phase)*np.exp(-9.2*t)*(1-np.exp(-650*t))
    return (np.tanh(body*1.6)*.72+click)*v


def clap(v=1):
    t=signal(.27)
    white=RNG.standard_normal(len(t)).astype(np.float32)
    brush=hp(white,1250)
    env=np.exp(-24*t)*(1+.50*np.exp(-((t-.026)/.008)**2)+.37*np.exp(-((t-.047)/.009)**2))
    tone=np.sin(2*np.pi*185*t)*np.exp(-38*t)
    return (brush*env*.18+tone*.06*np.exp(-2*t))*v


def hat(open_=False,v=1):
    length=.28 if open_ else .11
    t=signal(length)
    white=RNG.standard_normal(len(t)).astype(np.float32)
    metal=hp(white,3100)
    noise=lp(metal,10000)
    return (noise*np.exp(-(14 if open_ else 43)*t)*v*.14).astype(np.float32)


def shaker(v=1):
    t=signal(.09);white=hp(RNG.standard_normal(len(t)).astype(np.float32),1700)
    return (white*np.exp(-40*t)*v*.065).astype(np.float32)


def deep_bass(midi,length=.29,v=1):
    t=signal(length)
    f=hz(midi)
    ph=2*np.pi*f*t
    # Controlled, harmonically rich mono bass: audible on phone without pure sub reliance.
    body=np.sin(ph)+.44*np.sin(2*ph+.08)+.23*np.sin(3*ph+.22)+.11*np.sin(4*ph+.1)
    env=(1-np.exp(-t/.008))*np.exp(-1.75*t)*np.minimum(1,np.maximum(0,(length-t)/.048))
    return (np.tanh(body*1.23)*env*.54*v).astype(np.float32)


def low_analog_lead(midi,length=.44,v=1):
    t=signal(length);f=hz(midi)
    # Detuned analog synth with finite harmonics and a round cutoff envelope.
    ph=2*np.pi*f*t
    x=np.zeros_like(t)
    for n in range(1,10):
        x+=(np.sin(ph*n)/n)*np.exp(-.18*n)
    x+=.22*np.sin(ph*1.004+.14)
    x=lp(x,1450)
    attack=(1-np.exp(-t/.016))
    decay=np.exp(-1.45*t)
    release=np.minimum(1,np.maximum(0,(length-t)/.10))
    x=np.tanh(x*1.7)*attack*decay*release*v
    return x.astype(np.float32)


def warm_pad(midi,length,v=1):
    t=signal(length);f=hz(midi)
    p=2*np.pi*f*t
    x=.53*np.sin(p)+.31*np.sin(p*1.003+.4)+.11*np.sin(p*2+.15)
    e=(1-np.exp(-t/.33))*np.minimum(1,np.maximum(0,(length-t)/.45))
    return (x*e*v).astype(np.float32)


def delayed_stereo(a,delay_seconds=.375,feedback=.22):
    n=round(delay_seconds*SR)
    result=a.copy()
    for mul,offset in ((feedback,n),(.09,2*n),(.04,3*n)):
        if offset<len(a):
            result[offset:,0]+=a[:-offset,1]*mul
            result[offset:,1]+=a[:-offset,0]*mul
    return result


def compose():
    rhythm=np.zeros((N,2),dtype=np.float32)
    lows=np.zeros_like(rhythm)
    melodics=np.zeros_like(rhythm)
    air=np.zeros_like(rhythm)

    # Fully original four-bar F minor / Dbmaj7 / Ab / Eb progression.
    # All main melody notes sit in the lower/middle register (Fm ~ F3–Eb4).
    roots=[29,25,32,27] # F1, Db1, Ab1, Eb1
    chordnotes=[[53,56,60,63],[49,53,56,60],[51,56,60,63],[51,55,58,62]]
    phrases=[
        [(0.0,53,.67,.92),(1.0,60,.42,.89),(1.75,56,.62,.95),(3.05,51,.54,.80)],
        [(0.0,53,.65,.89),(.98,56,.51,.85),(1.82,60,.58,.91),(3.08,56,.54,.82)],
        [(0.0,51,.62,.88),(.95,56,.52,.92),(1.82,60,.63,.93),(3.05,63,.44,.67)],
        [(0.0,55,.61,.90),(1.03,58,.49,.93),(1.90,55,.67,.82),(3.07,51,.54,.80)],
    ]
    for bar in range(BARS):
        ci=bar%4;bs=bar*BAR
        # Progressive, understated arrangement: groove immediately, then motif grows.
        level=1.0 if bar<8 else (1.13 if bar<12 else 1.04)
        if bar==12: level=.82
        for beat in range(4):
            put(rhythm,bs+beat*BEAT,kick(.41 if beat==0 else .37),pan=0)
            if beat%2:
                put(rhythm,bs+beat*BEAT+.006,clap(.31*level),pan=.04)
            if not(bar==12 and beat>=2):
                put(rhythm,bs+(beat+.5)*BEAT,hat(open_=True,v=.30*level),pan=.12 if beat%2==0 else -.12)
        # Quiet 16th motion without hip-hop swing or rattly hi-key percussion.
        for step in range(16):
            if step%2==0:continue
            if bar==12 and step>6:continue
            put(rhythm,bs+step*BEAT/4,shaker(.17*(1+.25*(step%4==3))*level),pan=.28 if step%4==1 else -.28)
        # 1/8 offbeats and sixteenth pickups, sitting between the 4/4 kicks.
        positions=[(.50,0,.55),(1.48,0,.63),(2.46,0,.70),(2.86,7,.35),(3.47,0,.68)]
        if bar>=8 and bar!=12:positions.append((3.74,12,.27))
        for pos,shift,v in positions:
            put(lows,bs+pos*BEAT,deep_bass(roots[ci]+shift+12,.30,v*.76*level),pan=0)
        # Airy but low, mostly sustained chord voices to give a dark melodic sense.
        for j,n in enumerate(chordnotes[ci][:3]):
            put(air,bs+.05,warm_pad(n,2.45,v=.038*level),pan=-.47 if j%2==0 else .44)
        # Mid-register melodic hook. Begins on first bar and changes in bar 9.
        for k,(pos,n,dynlen,vel) in enumerate(phrases[ci]):
            if bar>=8 and k==3 and bar%4!=3:n+=2 if ci==0 else 0
            if bar==12 and k>1:continue
            put(melodics,bs+pos*BEAT,low_analog_lead(n,BEAT*dynlen+.10,.126*vel*level),pan=(-.21 if k%2==0 else .24))
        # A tiny spaced analogue accent in the second half; never a high-key sparkly line.
        if 8<=bar<12:
            put(melodics,bs+3.46*BEAT,low_analog_lead(chordnotes[ci][1],.27,.043),pan=.31)
    melodics=delayed_stereo(melodics,BEAT*.75,.16)
    # A gentle 4/4 sidechain swell after each kick, releases before each offbeat bass note.
    envelope=np.ones(N,dtype=np.float32)
    for i in range(BARS*4):
        at=round(i*BEAT*SR)
        finish=min(N,at+round(.30*SR));span=finish-at
        if span>0:
            t=np.arange(span)/SR
            duck=.33+.67*(1-np.exp(-t/.14))
            envelope[at:finish]=np.minimum(envelope[at:finish],duck)
    lows*=envelope[:,None]
    melodics*=envelope[:,None]
    air*=envelope[:,None]
    musical=lows+melodics+air
    # Short room diffusion and stereo space for the synths (dry, punchy drums).
    for delay,gain in ((.077,.06),(.131,.043),(.218,.035)):
        d=round(delay*SR)
        if d<N:
            musical[d:,0]+=melodics[:-d,1]*gain
            musical[d:,1]+=melodics[:-d,0]*gain
    raw=rhythm+musical
    for channel in range(2):
        raw[:,channel]=hp(raw[:,channel],27)
        raw[:,channel]=lp(raw[:,channel],9400)
    # Short entry, short fade as a review snippet. Proper seamless loop is NOT yet approved.
    ramp=round(.05*SR)
    raw[:ramp]*=np.linspace(.04,1,ramp,dtype=np.float32)[:,None]
    fade=round(.55*SR)
    raw[-fade:]*=np.linspace(1,0,fade,dtype=np.float32)[:,None]
    raw=np.tanh(raw*1.2)
    rms=float(np.sqrt(np.mean(raw**2)))
    raw*=.112/max(1e-6,rms)
    peak=float(np.max(np.abs(raw)))
    if peak>.89: raw*=.89/peak
    return raw.astype(np.float32)


def verify_music(data):
    if data.shape!=(N,2):raise RuntimeError('Not stereo or wrong duration')
    if not np.isfinite(data).all():raise RuntimeError('Invalid generated samples')
    if float(np.max(np.abs(data)))>.93:raise RuntimeError('Music preview clipped')


def make_narrator_mix(music):
    if not VOICE.exists():return None
    sha=hashlib.sha256(VOICE.read_bytes()).hexdigest()
    if sha!=VOICE_SHA:raise RuntimeError('Approved narrator checksum mismatch: refuse to mix')
    wav,sr=sf.read(VOICE,dtype='float32')
    if wav.ndim!=1 or sr!=24000:raise RuntimeError('Narrator format unexpected')
    voice=resample_poly(wav,147,80).astype(np.float32)
    start=round(2.75*SR);end=start+len(voice)
    if end>N:raise RuntimeError('Voice too long for preview')
    env=np.ones(N,dtype=np.float32)
    advance=round(.36*SR);release=round(.52*SR)
    env[start-advance:start]=np.linspace(1,.24,advance,dtype=np.float32)
    env[start:end]=.24
    env[end:end+release]=np.linspace(.24,1,release,dtype=np.float32)
    out=music.copy()*env[:,None]*.63
    out[start:end,:]+=voice[:,None]*.87
    peak=float(np.max(np.abs(out)))
    if peak>.94:out*=.94/peak
    return out


def render():
    OUT.mkdir(parents=True,exist_ok=True)
    music=compose();verify_music(music)
    wav=OUT/'05-deep-current-techno-music-only.wav'
    sf.write(wav,music,SR,subtype='PCM_16')
    result={'id':'MUSIC-05','name':'Deep Current','status':'audition_owner_review_pending','genre':'modern melodic techno (not hip-hop)',
      'style':'124 BPM four-on-the-floor pulse; F minor deep analogue synth melody; rolling harmonically rich bass and dark warm pad; restrained highs',
      'rights':'Original procedural composition, no third-party musical loops/samples; no paid API',
      'bpm':BPM,'bars':BARS,'durationSeconds':round(DURATION,3),'sampleRateHz':SR,'channels':2,'wavSubtype':'PCM_16',
      'musicSha256':hashlib.sha256(wav.read_bytes()).hexdigest(),
      'musicPeak':round(float(np.max(abs(music))),5),'musicRMS':round(float(np.sqrt(np.mean(music**2))),5),
      'note':'Short candidate only: no owner approval, seamless loop or mastering QA.'}
    mx=make_narrator_mix(music)
    if mx is not None:
        out=OUT/'05-deep-current-techno-with-approved-narrator.wav'
        sf.write(out,mx,SR,subtype='PCM_16')
        result['narratorMixedSha256']=hashlib.sha256(out.read_bytes()).hexdigest()
        result['referenceSha256']=VOICE_SHA
        result['narratorMixedPeak']=round(float(np.max(np.abs(mx))),5)
    (OUT/'05-audition-manifest.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':render()