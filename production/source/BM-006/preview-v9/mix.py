from pathlib import Path
import subprocess,wave,math,json,hashlib
import numpy as np
from scipy.signal import resample_poly
B=Path(__file__).resolve().parent.parent
assert hashlib.sha256((B/'techno-thriller-final.mp3').read_bytes()).hexdigest()=='adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9'
sr=48000
voice=[]
for i in range(1,7):
 with wave.open(str(B/'audio'/f'scene-{i:02d}.wav')) as w: voice.append(np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.float32)/32768)
v=resample_poly(np.concatenate(voice),2,1).astype(np.float32);nv=len(v);end=nv+round(.8*sr);total=math.ceil((len(v)/sr+1.8)*60)*800
m=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(B/'techno-thriller-final.mp3'),'-f','f32le','-ar',str(sr),'-ac','2','-']),dtype='<f4').reshape(-1,2)
assert len(m)>=end
# Exact approved B gains. Envelope speech gate derived from 20-ms RMS and true sample durations.
# Smooth attack/release between gains; no tempo changes.
block=480;g=np.empty(end,np.float32);level=.55;voice_pad=np.pad(v,(0,total-nv));
for j in range(0,end,block):
 stop=min(j+block,end);lo=max(0,j-480);hi=min(nv,stop+480);rms=float(np.sqrt(np.mean(v[lo:hi]**2))) if hi>lo else 0;target=.32 if rms>.012 else .55;tc=.024 if target<level else .28
 x=np.arange(1,stop-j+1)/sr;g[j:stop]=target+(level-target)*np.exp(-x/tc);level=float(g[stop-1])
# Music starts from the approved master; fade naturally after the final narration.
fade=np.ones(end,np.float32);fade[:int(.08*sr)]=np.linspace(0,1,int(.08*sr));fade[nv:end]=np.cos(np.linspace(0,np.pi/2,end-nv))**2
mix=np.zeros((total,2),np.float32);mix[:end]=m[:end]*g[:,None]*fade[:,None];mix+=voice_pad[:,None]*.88
peak=float(np.max(np.abs(mix)));assert peak<1.0,peak
with wave.open(str(B/'mix.wav'),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes(np.round(mix*32767).astype('<i2').tobytes())
print(json.dumps({'narration_seconds':nv/sr,'music_resolve_seconds':.8,'silent_hold_seconds':(total-end)/sr,'planned_frames':total//800,'mix_peak':peak,'music_last_half_second_pre_fade_rms':float(np.sqrt(np.mean(m[nv-24000:nv]**2))),'music_sha256':hashlib.sha256((B/'techno-thriller-final.mp3').read_bytes()).hexdigest()},indent=2))
