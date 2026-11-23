from pathlib import Path
import numpy as np, soundfile as sf, hashlib, json, subprocess, base64, html, argparse
from scipy.signal import resample_poly, fftconvolve
# Invoke from the repository root with private files. No generated audio/HTML goes to Git.
parser=argparse.ArgumentParser(description='Generate MUSIC-06 original/louder/stronger HTML listening tests')
parser.add_argument('--music',required=True,type=Path,help='Privately stored MUSIC-06 MP3')
parser.add_argument('--voice',required=True,type=Path,help='Approved private 24kHz mono Qwen reference WAV')
parser.add_argument('--out',required=True,type=Path,help='Private ignored output folder')
args=parser.parse_args()
OUT=args.out;OUT.mkdir(exist_ok=True,parents=True)
MUSIC=args.music;VOICE=args.voice
assert hashlib.sha256(MUSIC.read_bytes()).hexdigest()=='adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9'
assert hashlib.sha256(VOICE.read_bytes()).hexdigest()=='0e7f4d17e9d16f3ddb5ded7dbde68a6b774af19cb04a479debedb8811355f94c'
SR=44100;N=20*SR;START=2*SR
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(MUSIC),'-t','20','-ar','44100','-ac','2','-f','f32le','-'])
bed=np.frombuffer(raw,dtype='<f4').reshape((-1,2)).copy()[:N]
speech,sr=sf.read(VOICE,dtype='float32');assert sr==24000 and speech.ndim==1
speech=resample_poly(speech,147,80).astype('float32')
end=START+len(speech)
vt=np.zeros((N,2),dtype='float32');vt[START:end,:]=speech[:,None]*.88
activity=np.zeros(N,dtype='float32');k=round(.035*SR)
active=(fftconvolve(np.abs(speech),np.ones(k,dtype='float32')/k,'same')>.013).astype('float32')
activity[START:end]=active
# replicate short-run envelope as existing preview
attack=np.exp(-1.0/(SR*.024));release=np.exp(-1.0/(SR*.28))
bounds=np.r_[0,np.flatnonzero(np.diff(activity)!=0)+1,N]
env=np.empty(N,dtype='float32');last=0.
for st,en in zip(bounds[:-1],bounds[1:]):
    target=float(activity[st]);coef=attack if target>last else release
    z=np.arange(1,en-st+1)
    env[st:en]=target+(last-target)*np.power(coef,z)
    last=float(env[en-1])
ramp=np.minimum(1.,np.arange(N,dtype='float32')/(SR*.36))
fade=np.minimum(1.,(N-np.arange(N,dtype='float32'))/(SR*.8))
fades=ramp*np.clip(fade,0,1)
idx=np.flatnonzero((env>.95)&(np.arange(N)>=START)&(np.arange(N)<end))
def rms(x):return float(np.sqrt(np.mean(np.asarray(x,dtype=np.float64)**2)))
def db(x):return 20*np.log10(max(x,1e-12))
settings=[
 {'id':'a','title':'A · Current mix','desc':'The existing quieter soundtrack','normal':.40,'speaking':.16},
 {'id':'b','title':'B · Owner-approved','desc':'Owner-approved soundtrack balance for Bharat Mode','normal':.55,'speaking':.32},
 {'id':'c','title':'C · Music forward','desc':'Strongest cinematic score, less room for narration','normal':.66,'speaking':.44},
]
for row in settings:
    base=row['normal'];under=row['speaking'];duck=1-under/base
    gain=base*(1-duck*env)*fades
    music=bed*gain[:,None]
    mix=vt+music
    peak=float(np.max(np.abs(mix)))
    row['peak']=peak
    print(row['title'], 'peak',peak,'music RMS',db(rms(music[idx])),'voice rms',db(rms(vt[idx])))
    # apply common stereo peak safety cap if necessary; no clipping, preserve stem balance
    safety=min(1.,0.94/peak)
    row['safety']=safety
    row['peakPost']=peak*safety
    mix=mix*safety
    filepath=OUT/f'MUSIC06_Mix_{row["id"]}.mp3'
    pcm=np.clip(mix,-1,1).astype('<f4')
    # piping float PCM through FFmpeg avoids redundant WAV file
    proc=subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar','44100','-ac','2','-i','-','-codec:a','libmp3lame','-b:a','160k',str(filepath)],input=pcm.tobytes(),capture_output=True)
    if proc.returncode:raise RuntimeError(proc.stderr.decode())
    row['path']=str(filepath)
    row['sha256']=hashlib.sha256(filepath.read_bytes()).hexdigest()
    row['duringVoiceMusicRms']=round(db(rms(music[idx])) +db(safety),1)
    row['voiceRms']=round(db(rms(vt[idx]))+db(safety),1)
    row['voiceMusicGapDb']=round(db(rms(vt[idx]))-db(rms(music[idx])),1)
    row['musicIncreaseVsAWhileVoiceDb']=round(db(under/.16),1)
    row['musicIncreaseVsAInBreaksDb']=round(db(base/.4),1)
    row['gainCurveSamples']=[round(float(env[i])*1.,3) for i in range(0,N,SR//10)]
# Generate HTML as single portable embedded mp3 file
for row in settings:row['url']='data:audio/mpeg;base64,'+base64.b64encode(Path(row['path']).read_bytes()).decode('ascii')
client=[{k:v for k,v in row.items() if k in ['id','title','desc','normal','speaking','safety','gainCurveSamples','url','voiceMusicGapDb','peakPost']} for row in settings]
htmltext=r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bharat Mode | MUSIC-06 Loudness Review</title>
<style>
:root{--bg:#0b1018;--surface:#16212a;--border:#30404b;--ink:#fff7eb;--muted:#aebfc7;--accent:#e8752e;--teal:#70d3cc;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;color-scheme:dark;background:var(--bg);color:var(--ink)}*{box-sizing:border-box}
body{margin:0;background:radial-gradient(ellipse at 92% 0%,#164f516e,transparent 50%),#0b1018;min-height:100vh}
main{width:min(940px,calc(100% - 28px));margin:0 auto;padding:32px 0 64px}
.kicker{color:var(--teal);text-transform:uppercase;letter-spacing:.17em;font-size:11px;font-weight:800}
h1{font-size:clamp(27px,5vw,39px);line-height:1.13;margin:10px 0 14px}h2{margin:0 0 10px;font-size:19px}p{color:var(--muted);line-height:1.55;font-size:14px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:18px;margin:16px 0}
.tabs{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin:22px 0 16px}.tab{font-family:inherit;border:1px solid var(--border);background:#101922;color:var(--ink);padding:15px 12px;border-radius:13px;text-align:left;cursor:pointer;line-height:1.3}.tab strong{display:block;font-size:14px}.tab small{display:block;margin-top:6px;color:var(--muted);font-size:12px}.tab[aria-selected="true"]{border:2px solid var(--accent);background:#322218;padding:14px 11px}
.hint{display:inline-block;border-radius:20px;background:#234542;color:#9ce7e2;padding:5px 10px;font-size:12px;margin:3px 0 14px}
audio{width:100%;min-height:50px;margin:5px 0 4px}.meter{display:grid;grid-template-columns:1fr auto;gap:6px 12px;margin:18px 0 3px}.meter label{font-weight:650;font-size:14px}.meter .val{font-weight:800;font-variant-numeric:tabular-nums}.track{height:13px;background:#33404a;border-radius:999px;overflow:hidden;grid-column:1/-1}.fill{height:100%;width:0;transition:width .12s linear;background:var(--accent);border-radius:999px}.teal{background:var(--teal)}.micro{font-size:12px;color:#acb9c2}.badge{border:1px solid #5a656e;color:#cdd8dd;border-radius:20px;font-size:11px;padding:5px 8px;white-space:nowrap}
.row{display:flex;align-items:center;justify-content:space-between;gap:10px}.row h2{margin-bottom:3px}.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}.stat{border:1px solid var(--border);border-radius:12px;padding:13px;background:#111c23}.stat strong{font-size:23px;display:block}.stat small{font-size:12px;color:var(--muted)}
.note{border-left:3px solid var(--teal);padding:5px 13px;margin:22px 0;background:#1430334f;color:#c9dddf;font-size:13px;line-height:1.6}.footer{color:#9cabb4;font-size:11px}
@media(max-width:620px){.tabs{grid-template-columns:1fr}.two{grid-template-columns:1fr}.tab strong{font-size:14px}main{padding-top:22px}}
</style></head><body><main>
<div class="kicker">Bharat Mode / Audio Lab / MUSIC-06</div><h1>Approved soundtrack balance: Option B</h1><p>Choose a mix below and press Play. All three use the <b>same approved narrator</b>. The only difference is how prominently the techno-thriller soundtrack plays.</p>
<div class="tabs" role="tablist" aria-label="Mix choices">
  <button class="tab" id="tab-a" type="button" role="tab" aria-selected="false" data-id="a"><strong>A — Original</strong><small>Quieter soundtrack</small></button>
  <button class="tab" id="tab-b" type="button" role="tab" aria-selected="true" data-id="b"><strong>B — Approved</strong><small>Deeper bass is more present</small></button>
  <button class="tab" id="tab-c" type="button" role="tab" aria-selected="false" data-id="c"><strong>C — Stronger</strong><small>Music takes a larger role</small></button>
</div>
<section class="card"><div class="row"><h2 id="heading">B · Music louder</h2><span class="badge" id="badge">Approved</span></div><p id="desc"></p>
<audio id="audio" controls preload="metadata"></audio>
<p class="micro">The narrator enters at <b>0:02</b> and ends at around <b>0:10</b>. Listen there to judge whether the music masks words. Changing mix keeps approximately the same playback position.</p>
</section>
<section class="card"><div class="row"><h2>Easy 0–100 level meter</h2><span class="badge">Moving during playback</span></div><p><b>0</b> means muted; <b>100</b> means unchanged original recording volume. The bars show <b>mixer settings</b>, not how loud your ears will perceive each track.</p>
<div class="meter"><label>Voice level</label><span class="val" id="voice-number">88 / 100</span><div class="track"><div class="fill teal" id="voice-fill" style="width:88%"></div></div></div>
<div class="meter"><label>Music level</label><span class="val" id="music-number">55 / 100</span><div class="track"><div class="fill" id="music-fill" style="width:55%"></div></div></div>
<p id="duck-label" class="micro">Music automatically gets softer while the narrator speaks.</p></section>
<section class="card"><h2>At a glance</h2><div class="two"><div class="stat"><strong id="between">55 / 100</strong><small>Music in gaps and before speech</small></div><div class="stat"><strong id="during">32 / 100</strong><small>Music while voice is active</small></div></div><p id="comment"></p></section>
<p class="note"><b>Important:</b> This is still a 20-second mix test using the <i>original approved Qwen voice reference</i> — not the newly generated BM-0003 story narration. The test does not establish final mobile-speaker loudness. The owner has selected B as the baseline. Final episode mixing and phone-speaker checks are still required.</p>
<p class="footer">Bharat Mode / private review · Audio embedded in this HTML (no external media or account sign-in required) · Selected MUSIC-06 master remains stored privately.</p>
</main>
<script>
const mixData=__DATA__;
let preset='b';const audio=document.getElementById('audio');
function select(id){
 const next=mixData.find(d=>d.id===id);if(!next)return;
 const wasPlaying=!audio.paused;const position=audio.currentTime||0;
 audio.pause();preset=id;audio.src=next.url;audio.load();
 audio.addEventListener('loadedmetadata',()=>{try{audio.currentTime=Math.min(position,19.8);if(wasPlaying)audio.play().catch(()=>{})}catch{}},{once:true});
 document.getElementById('heading').textContent=next.title;document.getElementById('desc').textContent=next.desc;
 document.getElementById('badge').textContent=id==='b'?'Approved':'Comparison';
 document.getElementById('between').textContent=Math.round(next.normal*100)+' / 100';document.getElementById('during').textContent=Math.round(next.speaking*100)+' / 100';
 document.getElementById('comment').textContent=id==='a'?'This is what you heard before.':id==='b'?'This raises the soundtrack while keeping speech clearly in front.':'This is deliberately more music-forward; check if it starts competing with the voice.';
 document.querySelectorAll('.tab').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.id===id)));
 meter();
}
function meter(){const x=mixData.find(d=>d.id===preset);const t=audio.currentTime||0;const i=Math.min(x.gainCurveSamples.length-1,Math.floor(t*10));const env=x.gainCurveSamples[i]||0;
 const level=x.normal+(x.speaking-x.normal)*env;const voice=(t>=2&&t<9.6)?88:0;
 document.getElementById('music-number').textContent=Math.round(level*100)+' / 100';document.getElementById('voice-number').textContent=voice+' / 100';
 document.getElementById('music-fill').style.width=(level*100)+'%';document.getElementById('voice-fill').style.width=voice+'%';
 document.getElementById('duck-label').textContent=env>.4?'Music ducking: the score is lowered while the voice speaks.':'Music at its normal level between spoken phrases.';
}
document.querySelectorAll('.tab').forEach(b=>b.addEventListener('click',()=>select(b.dataset.id)));
audio.addEventListener('timeupdate',meter);audio.addEventListener('seeked',meter);audio.addEventListener('ended',meter);
select('b');
</script></body></html>'''
htmltext=htmltext.replace('__DATA__',json.dumps(client,separators=(',',':')))
p=OUT/'BharatMode_MUSIC06_Louder_Mix_Review.html';p.write_text(htmltext,encoding='utf-8')
report=[{k:v for k,v in row.items() if k not in ['gainCurveSamples','url']} for row in settings]
(OUT/'BharatMode_MUSIC06_Louder_Mix_Metrics.json').write_text(json.dumps(report,indent=2))
print('HTML',p,'bytes',p.stat().st_size)
print(json.dumps(report,indent=2))