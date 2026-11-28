import narrated as n
import patch as p
import render_storyboard as r
from render_motion import raster
import math,sys,subprocess,bisect,json,re
from pathlib import Path
B=Path(__file__).resolve().parent
D=n.D;BOUNDS=n.BOUNDS;N=n.N;END=n.END
# V2 approved motion changes, reconstructed from original source; V3 industry/fleet are the recovered original functions.
BASE_HERO=r.hero
# Complete the wide return at 5.12s (22.16s global), before the 0.18s exit.
# Both shipyard callouts are fully settled by then; actual speech timings unchanged.
n.CUES[2]=[(0,0),(.65,.65),(1.12,1.32),(1.65,1.90),(2.75,2.92),(3.9,3.65),(4.2,4.05),(5.5,4.60),(6.55,5.12),(7,5.23),(7.01,n.D[2])]
WIPE=.18
ICON_START=3.0
ICON_STEP=.125
ICON_ENTRY=.115

def msme_units(dt,t):
 s=''
 for j in range(24):
  x=592+(j%8)*54;y=(1072,1125,1324)[j//8]
  start=ICON_START+j*ICON_STEP
  if dt<start:continue
  a=r.smoothstep(start,start+ICON_ENTRY,dt)
  # Open, non-intersecting lanes above and below the count. No box behind the number.
  q=.33+.09*(.5+.5*math.sin((dt-start)*2.4+j))
  icon=r.poly([(0,37),(0,14),(10,14),(10,2),(16,2),(16,19),(26,12),(26,19),(37,12),(37,37)],'#638F88')
  for k in range(3):icon+=r.rect(5+k*11,25,6,6,r.IV,1)
  s+=r.group(icon,f'msme-unit-{j}',a*q,f'translate({x} {y+(1-a)*7:.3f})')
 return s


def art(i,dt,t):
 if i==4:return industry(dt,t)
 if i==5:return p.sea(t).split('</defs>',1)[1]+p.fleet(dt,t) if False else p.sea(t).replace(r.rect(0,0,1080,1920,r.DK),'',1)+p.fleet(dt,t)
 v=n.vt(i,dt)
 if i==0:
  q=r.ease(v/.85);s=r.group(r.ship(r.lerp(-780,105,q),740,870,t,True),'opening-ship',.18+.82*q,f'translate(0 {(1-q)*8+math.sin(t*1.3)*2:.2f})')
  s+=r.typed(540,1120,'Vindhyagiri',57,r.IV,v,.65,'ship-name',700,'middle')
  for j in range(7):s+=r.group(r.ship(139+j*117,1190,100,t,True),f'delivery-{j}',r.ease((v-2.3-j*.25)/.45))
  return r.bg(i,t).replace(r.rect(0,0,1080,1920,r.DK),'',1)+s+r.typed(540,1322,'7 / 7 delivered',62,r.MINT,v,4.1,'complete',800,'middle')
 s=BASE_HERO(i,v,t,n.theme(i)[0]);bg=r.bg(i,t).replace(r.rect(0,0,1080,1920,base_color(i)),'',1)
 if i==2:s=s.split('<defs><linearGradient id="map-top-fade"',1)[0]
 return bg+s

def industry(dt,t):
 # The exact V3 illustration, including the animated hoist; remove only its old metric groups.
 s=p.industry(dt,t).split('<g id="industry-percent"',1)[0]
 a=r.smoothstep(1.08,2.13,dt);b=r.smoothstep(4.51,5.35,dt)
 cx,cy,rad,stroke=288,1220,150,23
 arc=r.circ(cx,cy,rad,'none','#CFDDD5',stroke)
 if a>0:arc+=r.path(f'M{cx} {cy-rad} A{rad} {rad} 0 {int(.75*a>.5)} 1 {cx+rad*math.sin(2*math.pi*.75*a):.3f} {cy-rad*math.cos(2*math.pi*.75*a):.3f}',r.TEAL,stroke)
 arc+=r.txt(cx,1256,f'{round(75*a)}%',94,r.TEAL,800,'middle')
 s+=r.group(arc,'industry-percent',r.smoothstep(1.08,1.35,dt))
 s+=r.typed(cx,1440,'Indigenous content',34,r.INK,dt,1.25,'industry-percent-label',700,'middle')
 s+=msme_units(dt,t)
 s+=r.group(r.txt(792,1256,f'{round(200*b):,}'+('+' if b==1 else ''),96,r.TEAL,800,'middle'),'industry-msme',r.smoothstep(4.51,4.78,dt))
 s+=r.typed(792,1440,'MSMEs across India',34,r.INK,dt,4.66,'industry-msme-label',700,'middle')
 return s

def base_color(i):return r.DK if i in (0,5) else r.OR if i==3 else r.IV
REPL={0:{11:(12,'7'),17:(19,'17A.')},1:{10:(14,'149'),19:(23,'6,700')},2:{0:(1,'4'),9:(10,'3')},**p.REPL}
G=[]
for i,j in enumerate(n.J):
 words=j['words'];toks=[];k=0
 while k<len(words):
  e,txt=REPL[i].get(k,(k+1,words[k]['text']));toks.append({'text':txt,'start':words[k]['start'],'end':words[e-1]['end']});k=e
 groups=[];g=[]
 for tok in toks:
  if g and (len(g)>=5 or sum(r.tw(x['text'],51)*1.12 for x in g+[tok])+20*len(g)>810):groups.append(g);g=[]
  g.append(tok)
 if g:groups.append(g)
 G.append(groups)

def cap_layout(i,dt,t):
 if dt<n.J[i]['words'][0]['start'] or t>=BOUNDS[-1]:return []
 g=next(g for g in reversed(G[i]) if g[0]['start']<=dt);v=[w for w in g if w['start']<=dt];size=51
 widths=[];scales=[]
 for k,w in enumerate(v):
  q=r.clip((dt-w['start'])/.2);scale=(.6+.52*q/.55 if q<.55 else 1.12-.12*(q-.55)/.45) if k==len(v)-1 else 1
  scales.append(scale);widths.append(r.tw(w['text'],size)*scale)
 total=sum(widths)+20*(len(v)-1);x=540-total/2;out=[]
 for k,w in enumerate(v):
  out.append((w['text'],x+widths[k]/2,scales[k],widths[k],k==len(v)-1));x+=widths[k]+20
 return out

def chrome(i,dt,t):
 dark,saf=n.theme(i);s=f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{r.logo}</svg>'+r.rect(730,100,278,65,r.IV if dark else r.DK,33)+r.txt(869,139,'DEFENCE',25,r.DK if dark else r.IV,500,'middle',extra='letter-spacing=".7"')
 items=cap_layout(i,dt,t)
 if items:
  l=items[0][1]-items[0][3]/2;rr=items[-1][1]+items[-1][3]/2;s+=r.rect(l-24,1575,rr-l+48,112,r.DK,24,op=.76 if saf else .3 if dark else .1)
  for text,cx,scale,w,last in items:
   ink=(r.PEACH if dark or saf else r.BROWN) if last else r.IV if dark or saf else r.INK
   s+=r.txt(cx,1652,text,51,ink,700,'middle',extra=f'transform="translate({cx} 1634) scale({scale}) translate({-cx} -1634)"')
 sw=(912-5*14)/6
 for k in range(6):
  x=84+k*(sw+14);q=r.clip((t-BOUNDS[k])/(BOUNDS[k+1]-BOUNDS[k]));s+=r.rect(x,1805,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5)+r.rect(x,1805,sw*q,13,r.IV if saf else r.OR,min(6.5,sw*q/2))
 return s

def rgbmix(c,d,x):return '#'+''.join(f'{round(r.lerp(int(c[k:k+2],16),int(d[k:k+2],16),x)):02x}' for k in (1,3,5))
# One active content scene at a time; background changes across the boundary, never ghosted labels.
# Incoming heading begins typing at the first frame, incoming art fades over .28 seconds.
def state(t):
 i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=min(D[i],t-BOUNDS[i]);bg=base_color(i);op=1
 if i>0 and dt<.28:
  op=.12+.88*r.smoothstep(0,.28,dt);bg=base_color(i) if i==3 else rgbmix(base_color(i-1),bg,r.smoothstep(-.18,.28,dt))
 if i<5 and i!=2 and D[i]-dt<.18:
  rem=D[i]-dt;op=r.smoothstep(0,.18,rem);bg=rgbmix(bg,base_color(i+1),r.smoothstep(-.18,.28,-rem))
 return i,dt,bg,op

def frame_svg(f):
 t=min(f/60,END-1/60);i,dt,bg,op=state(t)
 # Background, single editorial content layer, then permanent foreground overlay.
 content=art(i,dt,t)+n.header(i,dt)
 # Short directional content exit, on the original ivory background.
 transform=''
 if i==2 and D[i]-dt<WIPE:
  u=r.smoothstep(0,WIPE,WIPE-(D[i]-dt));op=1-u;transform=f'translate({-64*u:.3f} 0)'
 return n.svg(r.rect(0,0,1080,1920,bg)+r.group(content,'scene-content',op,transform)+r.group(chrome(i,dt,t),'fixed-foreground',1))

if __name__=='__main__':
 start,end=map(int,sys.argv[1:3]);out=sys.argv[3]
 proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgra','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','1','-preset','ultrafast','-crf','18','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',out],stdin=subprocess.PIPE)
 last=None
 for f in range(start,end):
  if f/60<END or last is None:last=raster(frame_svg(f)).tobytes()
  proc.stdin.write(last)
  if f%120==0:print(f,flush=True)
 proc.stdin.close();assert proc.wait()==0
