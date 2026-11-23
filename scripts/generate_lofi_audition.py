#!/usr/bin/env python3
"""Bharat Mode original lo-fi hip-hop audition, MUSIC-04.

Composition and every sound here are procedurally authored; no existing music,
commercial loops, third-party samples, paid API, or music generator is used.
Private approved synthetic reference optional, SHA-validated, never committed.
This creates ORIGINAL audition media, NOT approved production soundtrack.
"""
from __future__ import annotations
import hashlib, json, math, os
from pathlib import Path
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 44100
BPM = 92
BEAT = 60 / BPM
BAR = BEAT * 4
BARS = 12
DURATION = BAR * BARS
N = round(DURATION * SR)
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get('BHARAT_LOFI_OUT',str(ROOT/'out'/'music-lofi'))).expanduser()
VOICE = Path(os.environ.get('BHARAT_APPROVED_REFERENCE',str(ROOT/'out'/'private'/'bharat-mode-qwen-voice-audition.wav'))).expanduser()
REFERENCE_SHA='0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c'
RNG=np.random.default_rng(20261123)


def note(midi):return 440 * 2 ** ((midi-69)/12)

def append(buf, start, signal, pan=0.0):
    p=int(round(start*SR)); offset=max(0,-p); p=max(0,p)
    if p>=len(buf) or offset>=len(signal):return
    n=min(len(buf)-p, len(signal)-offset)
    sig=np.asarray(signal[offset:offset+n],dtype=np.float32)
    angle=np.pi/4*(1+np.clip(pan,-1,1))
    buf[p:p+n,0]+=sig * np.cos(angle)*1.41421356
    buf[p:p+n,1]+=sig * np.sin(angle)*1.41421356


def rhodes(midi, duration=1.3, velocity=1):
    t=np.arange(int(duration*SR),dtype=np.float32)/SR
    f=note(midi)
    ph=2*np.pi*f*t
    # FM transient -> mellow Rhodes-like sine body, slight detuning
    fm=.82*np.exp(-6*t)*np.sin(2*ph+0.33)
    a=np.sin(ph+fm)
    b=.32*np.sin(2.002*ph+.25)*np.exp(-1.9*t)
    c=.11*np.sin(3.004*ph+.9)*np.exp(-3.4*t)
    wobble=.993+.007*np.sin(2*np.pi*.38*t+.3)
    env=(1-np.exp(-t/.013))*np.exp(-1.3*t)*np.clip((duration-t)/.16,0,1)
    return (velocity*(a+b+c)*env*wobble).astype(np.float32)


def glass(midi, duration=.85, velocity=1):
    t=np.arange(int(duration*SR),dtype=np.float32)/SR
    ph=2*np.pi*note(midi)*t
    y=np.sin(ph)+.19*np.sin(ph*2.009)+.075*np.sin(ph*4.02)
    env=(1-np.exp(-t/.009))*np.exp(-3.4*t)*np.clip((duration-t)/.09,0,1)
    return (y*env*velocity).astype(np.float32)


def bass(midi,duration=.55,velocity=1):
    t=np.arange(int(duration*SR),dtype=np.float32)/SR
    ph=2*np.pi*note(midi)*t
    y=np.sin(ph)+.22*np.sin(ph*2-.1)+.09*np.sin(ph*3+.2)
    env=(1-np.exp(-t/.011))*np.exp(-1.55*t)*np.clip((duration-t)/.13,0,1)
    return (np.tanh(1.6*y)*.72*env*velocity).astype(np.float32)


def kick(velocity=1):
    d=.34;t=np.arange(round(d*SR))/SR
    f=51+112*np.exp(-33*t)
    ph=2*np.pi*np.cumsum(f)/SR
    tonal=np.sin(ph)*np.exp(-13*t)
    click=RNG.normal(size=len(t))*np.exp(-100*t)*.033
    return ((tonal+click)*velocity).astype(np.float32)


def snare(velocity=1,ghost=False):
    d=.24;t=np.arange(round(d*SR))/SR
    noise=RNG.normal(size=len(t))
    bp=sosfilt(butter(2,[850,9600],fs=SR,btype='bandpass',output='sos'),noise)
    body=np.sin(2*np.pi*171*t)*np.exp(-23*t)
    snap=bp*np.exp(-22*t)
    # loose two-layer clap with soft delayed breath
    tail=np.zeros_like(snap)
    delay=round(.013*SR);tail[delay:]=snap[:-delay]*.48
    return ((.38*snap+.25*body+.23*tail)*velocity*(.36 if ghost else 1)).astype(np.float32)


def hat(velocity=1,open_=False):
    d=.32 if open_ else .087;t=np.arange(round(d*SR))/SR
    noise=RNG.normal(size=len(t))
    bp=sosfilt(butter(2,[4500,15500],fs=SR,btype='bandpass',output='sos'),noise)
    decay=14 if open_ else 51
    return (bp*np.exp(-decay*t)*velocity).astype(np.float32)


def pad(midi,duration=3,velocity=1):
    t=np.arange(round(duration*SR),dtype=np.float32)/SR
    ph=2*np.pi*note(midi)*t
    x=.69*np.sin(ph)+.19*np.sin(ph*1.003+.17)+.10*np.sin(ph*2+.4)
    env=(1-np.exp(-t/.42))*np.clip((duration-t)/.55,0,1)
    return (x*env*velocity).astype(np.float32)


def soft_delay(b):
    y=b.copy()
    for delay,gain in ((.115,.09),(.245,.065),(.363,.044)):
        d=round(delay*SR)
        y[d:,0]+=b[:-d,1]*gain
        y[d:,1]+=b[:-d,0]*gain
    return y


def compose():
    melodic=np.zeros((N,2),dtype=np.float32)
    rhythm=np.zeros((N,2),dtype=np.float32)
    # Cmaj9 / Am9 / Fmaj9 / G6/9  = bright, warm jazzy progression
    chords=[
      [48,52,55,59,62], # C major 9
      [45,48,52,55,59], # A minor 9
      [41,45,48,52,55], # F major 9
      [43,47,50,52,57], # G6 add9
    ]
    roots=[36,33,41,43]
    # Expressive repeated 4-bar hook with rest placement, not a generic arpeggio.
    # Each entry=(beatWithinBar, MIDI note, holdInSeconds, dynamics)
    motifs=[
     [(0.0,76,.65,.83),(1.0,79,.45,.92),(1.75,81,.50,.78),(2.5,79,.50,.88),(3.35,76,.32,.65)],
     [(0.0,76,.70,.78),(1.0,74,.47,.84),(1.73,72,.40,.76),(2.6,76,.80,.78)],
     [(0.3,72,.52,.75),(1.0,76,.48,.88),(1.7,79,.62,.77),(2.75,76,.70,.90)],
     [(0.0,74,.46,.84),(0.8,76,.34,.75),(1.65,79,.55,.82),(2.55,81,.43,.92),(3.15,79,.72,.70)]
    ]
    for bar in range(BARS):
        ci=bar%4; bs=bar*BAR
        # chord voicings in close register, less muddy when narrated
        for j,n in enumerate(chords[ci][1:]):
            append(melodic,bs-.02,pad(n,2.88,velocity=.009),pan=-.40 if j%2==0 else .44)
        # syncopated Rhodes voicings with a touch of jazz articulation
        for pos,vel,duration in ((0,.042,.92),(2.0,.028,.62),(3.5,.022,.52)):
            for j,n in enumerate(chords[ci][1:]):
                append(melodic,bs+pos*BEAT+(j%2)*.003,rhodes(n+12,duration,vel*(.84+.12*j)),pan=(-.28+.16*j))
        for k,(pos,n,_,dyn) in enumerate(motifs[ci]):
            # hook is prominent in instrumental portions, airy over the narration
            lift=1 if bar%4==0 else .92
            append(melodic,bs+pos*BEAT,glass(n,.95,.046*dyn*lift),pan=.17 if k%2 else -.18)
        # bass: syncopated a few notes but restrained
        for pos,semitone,vel in ((0,0,.095),(1.5,0,.061),(2.75,7,.052),(3.5,0,.058)):
            append(melodic,bs+pos*BEAT,bass(roots[ci]+semitone,.43,vel),pan=0)
        # drums: halftime hip-hop pocket with 2-and-4 snare, eighth-hat swing
        # Each bar has a humanized kick arrangement.
        kpatterns=[[0,1.5,2.75],[0,1.75,2.75,3.5],[0,.75,2.5],[0,1.5,2.75,3.5]]
        for k,pos in enumerate(kpatterns[ci]):
            delta=[.0,.010,-.012,.007][k]
            append(rhythm,bs+pos*BEAT+delta,kick(.108 if k==0 else (.091 if pos>=2 else .077)))
        for pos in (1.,3.):
            append(rhythm,bs+pos*BEAT+.016,snare(.093),pan=.035)
        for pos in (2.75,3.75):
            append(rhythm,bs+pos*BEAT+.022,snare(.035,ghost=True),pan=-.08)
        for h in range(8):
            pos=h*.5*BEAT
            # lo-fi swing of off-beat eighths and quiet alternating accents
            sw=.078*BEAT if h%2 else 0
            jit=RNG.uniform(-.004,.006)
            open_=h==7 and bar%4==3
            vel=.069 if h%2==0 else .054
            vel*=RNG.uniform(.82,1.13)
            append(rhythm,bs+pos+sw+jit,hat(vel,open_),pan=(-.20 if h%2 else .20))
    # Gentle room delay on instruments only; drums stay present and dry.
    melodic=soft_delay(melodic)
    music=rhythm+melodic
    for channel in range(2):
        x=sosfilt(butter(2,31,fs=SR,btype='highpass',output='sos'),music[:,channel])
        # tame sharpness, tape-like top roll-off
        x=sosfilt(butter(2,10300,fs=SR,btype='lowpass',output='sos'),x)
        music[:,channel]=x
    # very quiet original procedurally generated tape noise, not a sampled record
    noise=RNG.normal(size=(N,2)).astype(np.float32)*.00057
    for channel in range(2):
        noise[:,channel]=sosfilt(butter(2,2800,fs=SR,btype='lowpass',output='sos'),noise[:,channel])
    music+=noise
    # music starts on the first beat, with gentle final fade for audition only
    fade=round(.45*SR)
    music[-fade:]*=np.linspace(1,0,fade)[:,None]
    music=np.tanh(music*1.26)*.92
    rms=float(np.sqrt(np.mean(music**2)))
    # music-only normalized to an audible moderate volume without hard limiting
    music*=.078/max(rms,1e-5)
    peak=float(np.max(np.abs(music)))
    if peak>.88: music*=.88/peak
    return music.astype(np.float32)


def render():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    music=compose()
    music_path=OUTPUT/'04-lofi-motion-music-only.wav'
    sf.write(music_path,music,SR,subtype='PCM_16')
    record={'id':'MUSIC-04','name':'Lo-Fi Motion','status':'audition_only_owner_review_pending',
            'style':'92 BPM swung lo-fi hip-hop groove / punchy kick-snare / airy jazzy Rhodes hook / warm sub-bass / subtle original tape texture',
            'license':'original code-generated composition; no third-party music or samples',
            'bpm':BPM,'durationSeconds':round(DURATION,3),'sampleRateHz':SR,
            'channels':2,'audioFormat':'WAV PCM16','musicSha256':hashlib.sha256(music_path.read_bytes()).hexdigest(),
            'musicPeak':round(float(np.max(np.abs(music))),5),'musicRMS':round(float(np.sqrt(np.mean(music**2))),5)}
    if VOICE.is_file():
        if hashlib.sha256(VOICE.read_bytes()).hexdigest()!=REFERENCE_SHA:
            raise ValueError('Private narrator reference does not match owner-approved SHA; refusing mix')
        voice,sr=sf.read(VOICE,dtype='float32')
        if sr!=24000 or voice.ndim!=1:raise ValueError('Unexpected voice format')
        from scipy.signal import resample_poly
        v=resample_poly(voice,147,80).astype(np.float32)
        start=round(2.25*SR);end=start+len(v)
        if end>N:raise ValueError('Reference too long')
        env=np.ones(N,dtype=np.float32)
        ramp=round(.30*SR)
        env[start-ramp:start]=np.linspace(1,.29,ramp)
        env[start:end]=.29
        env[end:end+ramp]=np.linspace(.29,1,ramp)
        demo=music*.78*env[:,None]
        # Narrator distinctly central, audible even over headphones.
        vv=v*.80
        head=min(round(.045*SR),len(vv)//3)
        vv[:head]*=np.linspace(0,1,head)
        vv[-head:]*=np.linspace(1,0,head)
        demo[start:end]+=vv[:,None]
        peak=float(np.max(np.abs(demo)))
        if peak>.95: demo*=.95/peak
        out=OUTPUT/'04-lofi-motion-with-approved-narrator.wav'
        sf.write(out,demo,SR,subtype='PCM_16')
        record.update(narratorAuditionSha256=hashlib.sha256(out.read_bytes()).hexdigest(),
                      narratorAudioOriginalSha256=REFERENCE_SHA,
                      narratorMixPeak=round(float(np.max(np.abs(demo))),5),
                      narratedStartSeconds=round(start/SR,3),narratorDurationSeconds=len(voice)/24000)
        print('Narrator-mixed audition:',out)
    else:
        print('Approved narrator file unavailable: instrumental-only preview exported')
    manifest=OUTPUT/'04-lofi-motion-manifest.json'
    manifest.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('Original lo-fi music audition:',music_path, '\nManifest:',manifest)
    print(json.dumps(record,indent=2))

if __name__=='__main__':render()