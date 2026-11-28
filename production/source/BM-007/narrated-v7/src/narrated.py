import render_storyboard as r
from render_motion import raster
import json,pathlib,hashlib,wave,math,bisect,sys,subprocess,re
import numpy as np
B=pathlib.Path(__file__).resolve().parent; A=B.parent/'audio'
J=[json.loads((A/f'scene-{i:02}-alignment.json').read_text()) for i in range(1,7)]
S=json.loads((A/'script.json').read_text());assert S==r.SCRIPTS
D=[]
for i,j in enumerate(J):
 p=A/f'scene-{i+1:02}.wav';assert hashlib.sha256(p.read_bytes()).hexdigest()==j['audio']['sha256'];assert j['transcript']==S[i];assert j['source']=='final-audio-acoustic-alignment';assert [w['text'] for w in j['words']]==S[i].split()
 with wave.open(str(p)) as w:
  assert (w.getframerate(),w.getnchannels(),w.getsampwidth())==(24000,1,2);d=w.getnframes()/24000
 assert abs(d-j['audio']['durationSeconds'])<1e-6;last=0
 for w in j['words']:assert last<=w['start']<w['end']<=d;last=w['end']
 D.append(d)
BOUNDS=np.r_[0,np.cumsum(D)].tolist();END=BOUNDS[-1]+.8;N=math.ceil((END+1)*60-1e-8)
# Storyboard local time -> real local time; anchors selected using actual phrase onsets and visual lead.
CUES=[[(0,0),(.65,1.56),(2.3,3.85),(4.1,4.55),(8,D[0])],[(0,0),(1.05,2.3),(1.7,2.85),(3,3.59),(6.6,5.20),(7.6,5.55),(8.2,5.85),(8.85,6.18),(12,D[1])],[(0,0),(.65,.65),(1.12,1.32),(1.65,1.90),(2.75,3.12),(3.9,3.90),(4.2,4.35),(5.5,5.55),(6.55,5.88),(7,D[2])],[(0,0),(.4,2.50),(4.3,4.15),(5.6,5.07),(8,6.86),(11,D[3])],[(0,0),(.4,1.08),(4.7,4.51),(9,D[4])],[(0,0),(.55,.65),(2.4,2.10),(3.4,3.16),(5.15,4.8),(5.5,5.19),(8,D[5])]]
def vt(i,dt):return float(np.interp(dt,[b for a,b in CUES[i]],[a for a,b in CUES[i]]))
def svg(s):return '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'+s+'</svg>'
def theme(i):
 t=r.SCENES[i][0];return t=='midnight',t=='saffron'
def art(i,dt,t):return r.bg(i,t)+r.hero(i,vt(i,dt),t,theme(i)[0])
def header(i,dt):
 th,kicker,heads,_=r.SCENES[i];dark,saf=theme(i);fg=r.IV if dark else r.INK;ac=r.MINT if dark else r.DK if saf else r.BROWN;v=vt(i,dt);op=1
 if i==1:op=1-r.smoothstep(1.05,1.7,v)+r.smoothstep(8.2,8.8,v)
 if i==2:op=1-r.smoothstep(.3,.65,v)+r.smoothstep(6.55,6.95,v)
 h=r.typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"');size=min(91,int(min(900/max(1,r.tw(x,91))*91 for x in heads)))
 for k,x in enumerate(heads):h+=r.typed(83,438+k*109,x,size,fg,dt,k*.18,'headline'+str(k),800,extra='letter-spacing="-2"')
 return r.group(h,'editorial-heading',r.clip(op))
G=[]
for j in J:
 groups=[];g=[]
 for w in j['words']:
  if g and (len(g)>=5 or sum(r.tw(x['text'],51) for x in g+[w])+14*len(g)>690):groups.append(g);g=[]
  g.append(w)
 if g:groups.append(g)
 G.append(groups)
def chrome(i,dt,t):
 dark,saf=theme(i);s=f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{r.logo}</svg>'+r.rect(730,100,278,65,r.IV if dark else r.DK,33)+r.txt(869,139,'DEFENCE',25,r.DK if dark else r.IV,500,'middle',extra='letter-spacing=".7"')
 if dt>=J[i]['words'][0]['start'] and t<BOUNDS[-1]:
  g=next(g for g in reversed(G[i]) if g[0]['start']<=dt);v=[w for w in g if w['start']<=dt];size=51;ws=[r.tw(w['text'],size) for w in v];total=sum(ws)+14*(len(v)-1);x=540-total/2
  s+=r.rect(x-24,1501,total+48,112,r.DK,24,op=.76 if saf else .3 if dark else .1)
  for k,w in enumerate(v):
   age=dt-w['start'];p=r.clip(age/.2);scale=(.6+.52*p/.55 if p<.55 else 1.12-.12*(p-.55)/.45) if k==len(v)-1 else 1;ink=(r.PEACH if dark or saf else r.BROWN) if k==len(v)-1 else r.IV if dark or saf else r.INK;cx=x+ws[k]/2
   s+=r.txt(x,1578,w['text'],size,ink,700,extra=f'transform="translate({cx} 1560) scale({scale}) translate({-cx} -1560)"');x+=ws[k]+14
 sw=(912-5*14)/6
 for k in range(6):
  x=84+k*(sw+14);p=r.clip((t-BOUNDS[k])/(BOUNDS[k+1]-BOUNDS[k]));s+=r.rect(x,1721,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5)+r.rect(x,1721,sw*p,13,r.IV if saf else r.OR,min(6.5,sw*p/2))
 return s
def frame_svg(n):
 t=min(n/60,END-1/60);i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=min(D[i],t-BOUNDS[i]);base=art(i,dt,t)
 if i and dt<.34:
  old=art(i-1,D[i-1],BOUNDS[i]-1/60);old=re.sub(r'id="([^"]+)"',r'id="old-\1"',old);old=re.sub(r'url\(#([^\)]+)\)',r'url(#old-\1)',old);base+=r.group(old,'outgoing-art',1-r.smoothstep(0,.34,dt))
 return svg(base+header(i,dt)+chrome(i,dt,t))
if __name__=='__main__':
 start,end=map(int,sys.argv[1:3]);out=sys.argv[3]
 p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgra','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','1','-preset','ultrafast','-crf','18','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',out],stdin=subprocess.PIPE)
 last=None
 for n in range(start,end):
  if n/60<END or last is None:last=raster(frame_svg(n)).tobytes()
  p.stdin.write(last)
  if n%120==0:print(n,flush=True)
 p.stdin.close();assert p.wait()==0
