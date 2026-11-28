import render_storyboard as r
from render_motion import raster
import json,pathlib,hashlib,wave,math,bisect,sys,subprocess,re
import numpy as np
B=pathlib.Path(__file__).resolve().parent; A=B.parent/'audio'
J=[json.loads((A/f'scene-{i:02}-alignment.json').read_text()) for i in range(1,7)]
D=[]
for i,j in enumerate(J):
 p=A/f'scene-{i+1:02}.wav';assert hashlib.sha256(p.read_bytes()).hexdigest()==j['audio']['sha256'];D.append(j['audio']['durationSeconds'])
BOUNDS=np.r_[0,np.cumsum(D)].tolist();END=BOUNDS[-1]+.8;N=2960
CUES4=[(0,0),(.4,2.50),(4.3,4.15),(5.6,5.07),(8,6.86),(11,D[3])]
# All graphic elements are original conceptual illustrations. Artwork and text occupy independent lanes.
def industry(dt,t):
 s=''; p=r.ease(dt/.65)
 # industrial illustration: gantry crane + factory + machining component, with no tiny text or connectors.
 art=r.line(110,1008,970,1008,'#B8CFC6',3)
 # Factory body and roof, three windows in independent silhouette.
 art+=r.poly([(125,994),(125,797),(236,730),(236,797),(348,730),(348,797),(460,730),(460,994)],'#D6E5DC','#527C76',4)
 art+=r.rect(153,690,53,96,'#789A93',3,'#527C76',3)+r.rect(162,666,35,28,'#527C76',3)
 for x in [156,247,338]:
  art+=r.rect(x,850,66,58,'#527C76',4)+r.line(x+33,851,x+33,908,'#D6E5DC',2)+r.line(x,879,x+66,879,'#D6E5DC',2)
 art+=r.rect(357,937,68,57,'#94B5AC',3)
 # crane with moving hoist and suspended generic machined component
 art+=r.rect(526,698,34,296,'#799C95',3)+r.rect(875,698,34,296,'#799C95',3)+r.rect(505,681,425,37,'#527C76',3)
 for x in range(530,894,48):art+=r.line(x,688,x+24,710,'#BBD7CD',3)
 hx=720+45*math.sin(t*1.3);hy=817+13*math.sin(t*1.8)
 art+=r.rect(hx-24,716,48,19,'#E8752E',4)+r.line(hx,735,hx,hy,'#527C76',3)
 art+=r.path(f'M{hx-42} {hy+30} L{hx} {hy} L{hx+42} {hy+30}', '#527C76',3)+r.rect(hx-65,hy+30,130,49,'#A9C4B8',7,'#527C76',3)
 # assembly table and component outlines
 art+=r.rect(600,950,236,19,'#527C76',3)+r.rect(620,969,18,26,'#799C95')+r.rect(798,969,18,26,'#799C95')
 for x in [642,688,734,780]:art+=r.rect(x,931,30,19,'#A9C4B8',3,'#527C76',2)
 s+=r.group(art,'industry-art',p,f'translate(0 {(1-p)*20:.2f})')
 # Independent numeric areas; no graphic, line or icon enters either text area.
 a=r.smoothstep(1.08,2.13,dt);b=r.smoothstep(4.51,5.35,dt)
 s+=r.group(r.txt(288,1190,f'{round(75*a)}%',100,r.TEAL,800,'middle')+r.txt(288,1250,'Indigenous content',34,r.INK,700,'middle'),'industry-percent',r.smoothstep(1.08,1.35,dt))
 s+=r.group(r.txt(792,1190,f'{round(200*b):,}'+('+' if b==1 else ''),96,r.TEAL,800,'middle')+r.txt(792,1250,'MSMEs across India',34,r.INK,700,'middle'),'industry-msme',r.smoothstep(4.51,4.78,dt))
 return s
# Camera pullback is continuous, but each arriving ship has its own non-overlapping entry interval.
FLEET=[(410,925,260,0,0,0),(242,715,250,-1,1.10,1.83),(588,715,250,1,1.88,2.61),(120,925,250,-1,2.66,3.39),(710,925,250,1,3.44,4.17),(242,1135,250,-1,4.22,4.95),(588,1135,250,1,5.00,5.73)]
def zoom(dt):
 knots=[(0,2.95),(.55,2.95),(1.10,1.53),(2.66,1.12),(5.73,1.0)]
 for (a,x),(b,y) in zip(knots,knots[1:]):
  if dt<=b:return r.lerp(x,y,r.smoothstep(a,b,dt))
 return 1.0
def fleet_state(dt):
 z=zoom(dt);states=[]
 for j,(x,y,w,side,start,end) in enumerate(FLEET):
  if j and dt<start:continue
  sw=w*z;target=540+(x-540)*z;sy=970+(y-970)*z
  if j:
   p=r.smoothstep(start,end,dt);sx=r.lerp(-sw-16 if side<0 else 1096,target,p)
  else:sx=target;p=1
  states.append((j,sx,sy,sw,side,p))
 return states

def sea(t):
 s=r.rect(0,0,1080,1920,r.DK)
 s+='<defs><linearGradient id="ocean-water" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#0B1018"/><stop offset=".19" stop-color="#164553"/><stop offset=".60" stop-color="#216474"/><stop offset=".86" stop-color="#123642"/><stop offset="1" stop-color="#0B1018"/></linearGradient></defs>'
 s+=r.rect(0,550,1080,950,'url(#ocean-water)')
 for j in range(17):
  y=620+j*43; phase=t*1.6+j*.8
  s+=r.path(f'M-35 {y+5*math.sin(phase):.1f} Q145 {y-17+5*math.sin(phase):.1f} 320 {y:.1f} T685 {y:.1f} T1085 {y+4:.1f}', '#78BCC5',2.2,op=.14+.12*math.sin(j*.8)**2)
  for k in range(3):
   x=(j*173+k*370+t*24)%1200-60
   s+=r.line(x,y+14,x+50+12*math.sin(j+k),y+12,'#B4DFDE',2,op=.12)
 return s

def fleet(dt,t):
 s=''
 for j,x,y,w,side,p in fleet_state(dt):
  # Water contact and foam sit immediately under the hull; no opaque card or fade.
  h=w/800;wy=y+276*h
  s+=r.ell(x+w*.50,wy+5*h,w*.47,max(2,7*h),'#91D0D1',op=.25)
  for k in range(3):
   yy=wy+(5+k*7)*h
   s+=r.path(f'M{x+w*.08:.2f} {yy:.2f} Q{x+w*.32:.2f} {yy+4*math.sin(t*3+k):.2f} {x+w*.51:.2f} {yy:.2f} T{x+w*.92:.2f} {yy:.2f}','#9ADADB',max(1,2.5*h),op=.55-.12*k)
  # Right-side ships face into the frame, left-side ships sail bow-first to the right.
  ship=r.ship(x,y,w,t,True)
  if side>0:ship=f'<g transform="translate({2*x+w:.6f} 0) scale(-1 1)">{ship}</g>'
  s+=r.group(ship,f'formation-{j}',1)
 s+=r.typed(540,1410,'Seven delivered. One milestone.',42,r.MINT,dt*1.7,5.73*1.7,'close',700,'middle')
 return s

def art(i,dt,t):
 if i==4:return r.rect(0,0,1080,1920,r.IV)+industry(dt,t)
 if i==5:return sea(t)+fleet(dt,t)
 return r.bg(i,t)+r.hero(i,float(np.interp(dt,[b for a,b in CUES4],[a for a,b in CUES4])),t,False)
def header(i,dt):
 th,kicker,heads,_=r.SCENES[i];dark=th=='midnight';saf=th=='saffron';fg=r.IV if dark else r.INK;ac=r.MINT if dark else r.DK if saf else r.BROWN
 h=r.typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"');size=min(91,int(min(900/max(1,r.tw(x,91))*91 for x in heads)))
 for k,x in enumerate(heads):h+=r.typed(83,438+k*109,x,size,fg,dt,k*.18,'headline'+str(k),800,extra='letter-spacing="-2"')
 return r.group(h,'editorial-heading',1)
# Display-only numerical normalization preserves the original speech and timing spans.
REPL={3:{1:(2,'7'),9:(10,'23'),15:(16,'68'),19:(20,'16')},4:{3:(5,'75%'),10:(12,'200')},5:{}}
G={}
for i in (3,4,5):
 words=J[i]['words'];toks=[];k=0
 while k<len(words):
  e,txt=REPL[i].get(k,(k+1,words[k]['text']));toks.append({'text':txt,'start':words[k]['start'],'end':words[e-1]['end']});k=e
 groups=[];g=[]
 for tok in toks:
  if g and (len(g)>=5 or sum(r.tw(x['text'],51) for x in g+[tok])+14*len(g)>690):groups.append(g);g=[]
  g.append(tok)
 if g:groups.append(g)
 G[i]=groups

def chrome(i,dt,t):
 th=r.SCENES[i][0];dark=th=='midnight';saf=th=='saffron';s=f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{r.logo}</svg>'+r.rect(730,100,278,65,r.IV if dark else r.DK,33)+r.txt(869,139,'DEFENCE',25,r.DK if dark else r.IV,500,'middle',extra='letter-spacing=".7"')
 if dt>=J[i]['words'][0]['start'] and t<BOUNDS[-1]:
  g=next(g for g in reversed(G[i]) if g[0]['start']<=dt);v=[w for w in g if w['start']<=dt];size=51;ws=[r.tw(w['text'],size) for w in v];total=sum(ws)+14*(len(v)-1);x=540-total/2
  s+=r.rect(x-24,1575,total+48,112,r.DK,24,op=.76 if saf else .3 if dark else .1)
  for k,w in enumerate(v):
   age=dt-w['start'];p=r.clip(age/.2);scale=(.6+.52*p/.55 if p<.55 else 1.12-.12*(p-.55)/.45) if k==len(v)-1 else 1;ink=(r.PEACH if dark or saf else r.BROWN) if k==len(v)-1 else r.IV if dark or saf else r.INK;cx=x+ws[k]/2
   s+=r.txt(x,1652,w['text'],size,ink,700,extra=f'transform="translate({cx} 1634) scale({scale}) translate({-cx} -1634)"');x+=ws[k]+14
 sw=(912-5*14)/6
 for k in range(6):
  x=84+k*(sw+14);p=r.clip((t-BOUNDS[k])/(BOUNDS[k+1]-BOUNDS[k]));s+=r.rect(x,1805,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5)+r.rect(x,1805,sw*p,13,r.IV if saf else r.OR,min(6.5,sw*p/2))
 return s

def frame_svg(n):
 t=min(n/60,END-1/60);i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=min(D[i],t-BOUNDS[i]);base=art(i,dt,t)
 if i>=4 and dt<.34:
  old=art(i-1,D[i-1],BOUNDS[i]-1/60);old=re.sub(r'id="([^"]+)"',r'id="old-\1"',old);old=re.sub(r'url\(#([^\)]+)\)',r'url(#old-\1)',old);base=r.rect(0,0,1080,1920,r.DK if i==5 else r.IV)+r.group(old,'outgoing-art',1-r.smoothstep(0,.17,dt))+r.group(base,'incoming-art',r.smoothstep(.17,.34,dt))
 return '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'+base+header(i,dt)+chrome(i,dt,t)+'</svg>'
if __name__=='__main__':
 start,end=map(int,sys.argv[1:3]);out=sys.argv[3]
 p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgra','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','1','-preset','ultrafast','-crf','18','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',out],stdin=subprocess.PIPE)
 last=None
 for n in range(start,end):
  if n/60<END or last is None:last=raster(frame_svg(n)).tobytes()
  p.stdin.write(last)
 p.stdin.close();assert p.wait()==0
