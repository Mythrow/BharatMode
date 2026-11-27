import json,hashlib,wave,math,bisect,subprocess,sys,os,functools
from pathlib import Path
import numpy as np,cv2
import render_storyboard as r
from raster_base import raster
B=Path(__file__).resolve().parent; A=B.parent/'audio'; O=B.parent/'segments'; O.mkdir(exist_ok=True)
FPS=60
align=[json.loads((A/f'scene-{i+1:02d}-alignment.json').read_text()) for i in range(6)]
assert json.loads((A/'script.json').read_text())==r.SCRIPTS
D=[]
for i,a in enumerate(align):
 p=A/f'scene-{i+1:02d}.wav';assert hashlib.sha256(p.read_bytes()).hexdigest()==a['audio']['sha256'];assert a['source']=='final-audio-acoustic-alignment';assert ' '.join(w['text'] for w in a['words'])==r.SCRIPTS[i]
 with wave.open(str(p)) as w:
  assert (w.getframerate(),w.getnchannels(),w.getsampwidth())==(24000,1,2);d=w.getnframes()/24000
 assert abs(d-a['audio']['durationSeconds'])<1e-6
 last=0
 for w in a['words']:assert last<=w['start']<w['end']<=d;last=w['end']
 D.append(d)
r.BOUNDS=[0]+list(np.cumsum(D));END=r.BOUNDS[-1];RESOLVE=.8;HOLD=1;TOTAL=math.ceil((END+RESOLVE+HOLD)*FPS)
# Each reveal explicitly tied to the relevant acoustic word, offsets for diagram choreography.
idx=[{'company':0,'processor':9,'suite':14,**{f'node{j}':14 for j in range(4)}}, {'total':6,'total-label':8,'active':13,'active-label':16,'input':16,'input-t':16,'router':10,'router-label':10,'output':17,**{f'expert{j}':10 for j in range(6)}}, {'scripts':6,'shared':11,'shared-label':11,'comparison':14,'bar0':18,'bar1':21,'claim':21,**{f'script{j}':6 for j in range(4)},**{f'script-label{j}':7 for j in range(4)}}, {'training':3,'run':3,'three':6,**{f'size{j}':6 for j in range(3)},**{f'size-label{j}':8 for j in range(3)}}, {'langs':5,'text-surface':13,'written':13,'waveform':13,'spoken1':13,'spoken2':14}, {'core':5,'core-label':8,'potential':11,**{f'app{j}':10 for j in range(3)},**{f'app-label{j}':11 for j in range(3)}}]
# Keep some concepts visible early enough to finish, still linked to the first relevant spoken phrase.
r.CUE_MAP=[{k:align[i]['words'][v]['start']+(int(k[-1])*.1 if k[-1:].isdigit() and k.startswith(('node','expert','size','app','script')) else 0) for k,v in m.items()} for i,m in enumerate(idx)]
(B/'cue-map.json').write_text(json.dumps({'original':idx,'acoustic_seconds':r.CUE_MAP,'lead_seconds':.35,'adjusted':[dict({k:max(0,v-.35) for k,v in m.items()}, **({'processor':0.0} if i==0 else {})) for i,m in enumerate(r.CUE_MAP)],'script_examples_override':{'scene':3,'groups':[4,4,2],'start_seconds':[1.65,3.20,4.75],'entrance_seconds':0.26,'first_two_exit_start_relative_seconds':1.25,'exit_seconds':0.24,'hold_final_through_transition':True,'heading':'12 Indian scripts — reported','scope':'10 documented examples'},'opening_override':{'scene':1,'element':'processor','start_seconds':0.0,'duration_seconds':0.48,'initial_opacity':0.22,'initial_y_offset_px':48,'easing':'cubic ease-out'}},indent=2))
# native frame geometry and renderer from storyboard; separate scene/chrome for dissolve.
HDR='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
@functools.lru_cache(maxsize=256)
def groups(i):
 words=align[i].get('captionWords',align[i]['words']);g=[];current=[]
 for w in words:
  if current and (len(current)>=5 or r.tw(' '.join(x['text'] for x in current+[w]),51)>700):g.append(current);current=[]
  current.append(w)
 if current:g.append(current)
 return g

def scene(i,dt):
 theme,kicker,heads,_=r.SCENES[i];dark=theme=='midnight';saf=theme=='saffron';fg=r.IV if dark else r.INK;ac=r.MINT if dark else r.DK if saf else r.BROWN
 a=[r.bg(i,dt),r.typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"')];size=min(91,int(min(900/max(1,r.tw(h,91))*91 for h in heads)))
 for j,h in enumerate(heads):a.append(r.typed(83,438+j*109,h,size,fg,dt,j*.18,'headline'+str(j),800,extra='letter-spacing="-2"'))
 a.append(r.hero(i,dt,dt,dark));return HDR+''.join(a)+'</svg>'

def chrome(i,dt,t,tail=False):
 theme=r.SCENES[i][0];dark=theme=='midnight';saf=theme=='saffron';a=[f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{r.logo}</svg>',r.rect(730,100,278,65,r.IV if dark else r.DK,33),r.txt(869,139,'ARTIFICIAL INTELLIGENCE',17,r.DK if dark else r.IV,500,'middle',extra='letter-spacing=".7"')]
 if not tail:
  for g in groups(i):
   if g[0]['start']<=dt<=g[-1]['end']+.09:
    v=[w for w in g if w['start']<=dt];size=51;ws=[r.tw(w['text'],size) for w in v];total=sum(ws)+14*(len(v)-1);x=540-total/2
    a.append(r.rect(x-24,1501,total+48,112,r.DK,24,op=.76 if saf else .3 if dark else .1))
    for j,w in enumerate(v):
     active=w['start']<=dt<w['end'];p=r.clip((dt-w['start'])/.2);scale=(.6+.52*p/.55 if p<.55 else 1.12-.12*(p-.55)/.45) if active else 1;cx=x+ws[j]/2
     a.append(r.txt(x,1578,w['text'],size,(r.PEACH if dark or saf else r.BROWN) if active else r.IV if dark or saf else r.INK,extra=f'transform="translate({cx} 1557) scale({scale}) translate({-cx} -1557)"'));x+=ws[j]+14
    break
 sw=(912-5*14)/6
 for j in range(6):
  x=84+j*(sw+14);p=r.clip((t-r.BOUNDS[j])/(r.BOUNDS[j+1]-r.BOUNDS[j]));a.append(r.rect(x,1721,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5));a.append(r.rect(x,1721,sw*p,13,r.IV if saf else r.OR,min(6.5,sw*p/2)))
 return ''.join(a)

def full_svg(i,dt,t,tail=False):return scene(i,dt)[:-6]+chrome(i,dt,t,tail)+'</svg>'
@functools.lru_cache(maxsize=8)
def previous(i):return raster(scene(i-1,D[i-1]-1/FPS))
def frame(n):
 t=n/FPS; i=min(5,bisect.bisect_right(r.BOUNDS,t)-1);dt=t-r.BOUNDS[i];tail=t>=END
 if tail:dt=min(dt,D[-1]+RESOLVE)
 if i and dt<.34:
  a=raster(scene(i,dt));p=r.ease(dt/.34);a=cv2.addWeighted(a,p,previous(i),1-p,0)
  c=raster(HDR+chrome(i,dt,t,tail)+'</svg>');alpha=c[:,:,3:4].astype(np.uint16);a[:,:,:3]=np.minimum(255,c[:,:,:3].astype(np.uint16)+(a[:,:,:3].astype(np.uint16)*(255-alpha)+127)//255).astype(np.uint8)
 else:a=raster(full_svg(i,dt,t,tail))
 return a[:,:,:3].copy()

def run(i):
 start=math.ceil(r.BOUNDS[i]*FPS-1e-8);end=TOTAL if i==5 else math.ceil(r.BOUNDS[i+1]*FPS-1e-8);out=O/f'{i+1}.mp4';cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','1','-preset','ultrafast','-crf','18','-pix_fmt','yuv420p','-vf','scale=out_color_matrix=bt709','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',str(out)];p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for n in range(start,end):
  p.stdin.write(frame(n).tobytes())
  if n%120==0:print(i+1,n,flush=True)
 p.stdin.close();assert p.wait()==0;print('done',i+1,start,end,flush=True)
if __name__=='__main__':
 if sys.argv[1]=='sample':
  for i in range(6):
   n=int((r.BOUNDS[i+1]-.1)*FPS);cv2.imwrite(str(O/f'sample{i+1}.png'),frame(n))
 else:run(int(sys.argv[1]))
