from pathlib import Path
import math, html, json, base64, bisect, zipfile
import cairosvg
from PIL import Image, ImageDraw, ImageFont
B=Path(__file__).resolve().parent
W,H=1080,1920
IV='#FFF7EB'; DK='#0B1018'; INK='#283039'; TEAL='#117A7A'; OR='#E8752E'; MINT='#70D3CC'; PEACH='#FFBE91'; BROWN='#A63F17'
FONTS='/usr/share/fonts/opentype/inter/'
SCRIPTS=["The Indian Navy has received Vindhyagiri, completing the delivery of all seven homegrown stealth frigates under Project Seventeen A.","Designed by the Indian Navy, these advanced stealth warships are a hundred and forty-nine metres long and weigh nearly six thousand seven hundred tonnes when fully loaded.","Four were built at Mazagon Dock in Mumbai, and three at Garden Reach Shipbuilders in Kolkata.","All seven were delivered over a span of about twenty-three months. The final ship took sixty-eight months to build, sixteen months less than the first.","The programme achieved seventy-five percent indigenous content, involving more than two hundred micro, small and medium enterprises across India.","From design to construction, the programme marks a major milestone in India's ability to build advanced warships at home."]
BOUNDS=[0,8,20,27,38,47,55]
SCENES=[('midnight','PROJECT 17A',['Seven warships.','All delivered.'],'ocean-horizon'),('ivory','INDIAN NAVAL DESIGN',['Built on','a massive scale.'],'naval-blueprint'),('ivory','TWO INDIAN SHIPYARDS',['Built across','two cities.'],'coastal-geography'),('saffron','ENGINEERING EFFICIENCY',['Building','warships faster.'],'shipyard-timeline'),('ivory','DOMESTIC INDUSTRY',['Powered by','Indian industry.'],'industrial-grid'),('midnight','NAVAL SELF-RELIANCE',['Designed here.','Built here.'],'formation-sea')]
logo=(B/'avatar.svg').read_text();logo=logo[logo.index('>')+1:logo.rindex('</svg>')]
def clip(x):return max(0,min(1,x))
def ease(x):return 1-(1-clip(x))**3
def tw(s,size,weight=700):return ImageFont.truetype(FONTS+('Inter-Bold.otf' if weight>=700 else 'Inter-Medium.otf'),int(size)).getlength(s)
def esc(s):return html.escape(str(s))
def viewer_text(s):
 # Internal reference, QA and production annotations are not audience-facing copy.
 if any(term in str(s).casefold() for term in ('illustrative pronunciation','reference text','source note','internal note','helper text','placeholder','qa note','storyboard only')): raise ValueError(f'Internal annotation in visible layer: {s}')
 return s
def txt(x,y,s,size=40,fill=INK,weight=700,anchor='start',extra=''):
 viewer_text(s)
 return f'<text x="{x}" y="{y}" fill="{fill}" font-family="Inter" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{esc(s)}</text>'
def rect(x,y,w,h,fill,rx=0,stroke='none',sw=1,op=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
def circ(x,y,r,fill,stroke='none',sw=1,op=1):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
def ell(x,y,rx,ry,fill,stroke='none',sw=1,op=1):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
def path(d,c,w=3,fill='none',op=1):return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>'
def line(x,y,X,Y,c,w=3,op=1):return path(f'M{x} {y} L{X} {Y}',c,w,op=op)
def group(s,id,op=1,transform=''):return f'<g id="{id}" opacity="{op}" transform="{transform}">{s}</g>'
def reveal(s,id,dt,delay=0,dur=.6,dx=45,dy=12):
 p=ease((dt-delay)/dur);return group(s,id,p,f'translate({(1-p)*dx:.2f} {(1-p)*dy:.2f})')
def typed(x,y,s,size,c,dt,delay,id,weight=700,anchor='start',extra=''):
 viewer_text(s)  # Validate full text before typewriter slicing.
 local=dt-delay;p=ease(local/.56); n=min(len(s),max(0,int(local*18)+1)) if local>=0 else 0
 # Preserve the full label anchor during typing, so partial text doesn't shift laterally.
 left=x-tw(s,size,weight)/2 if anchor=='middle' else x-tw(s,size,weight) if anchor=='end' else x
 return group(txt(left,y,s[:n],size,c,weight,extra=extra),id,p,f'translate({(1-p)*28:.2f} 0)')
def pulse(x,y,t,c,r=7):return circ(x,y,r*2.7,c,op=.09+.08*math.sin(t*4))+circ(x,y,r,c,op=.7+.3*math.sin(t*4))
def trace(d,c,p,width=5):return f'<path d="{d}" stroke="{c}" stroke-width="{width}" fill="none" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="{100*clip(p):.3f} 100"/>'
def check(x,y,c,scale=1):return path(f'M{x} {y} l{13*scale} {13*scale} l{25*scale} {-28*scale}',c,5*scale)
# Original conceptual technical graphics; not a verified engineering drawing.
def poly(pts,fill,stroke='none',w=1,op=1):return path('M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in pts)+' Z',stroke,w,fill,op)
MAP=json.loads((B/'map.json').read_text())
# Ship coordinate system: 800 x 310. Coherent conceptual frigate profile, not exact configuration.
def ship(x,y,w,t=0,dark=False):
 c='#A8B8BE' if dark else '#71858D';light='#D8E1DF' if dark else '#A7B7B9'; edge='#4C686F' if dark else '#3C525A';low='#526A74' if dark else '#425960'
 s=poly([(0,204),(660,204),(790,170),(800,180),(737,256),(82,264),(21,242)],c,edge,2)
 s+=poly([(21,242),(737,239),(713,267),(85,276)],low,edge,2)+line(34,238,754,231,'#E8752E',2)
 s+=poly([(68,201),(95,161),(252,161),(282,201)],light,edge,2)
 s+=poly([(260,200),(296,119),(382,119),(410,89),(491,89),(526,200)],c,edge,2)
 s+=poly([(420,89),(437,53),(490,53),(513,89)],light,edge,2)
 s+=poly([(530,200),(558,144),(630,144),(659,200)],light,edge,2)
 s+=poly([(319,119),(333,78),(371,78),(389,119)],light,edge,2)
 s+=poly([(445,53),(454,8),(475,8),(485,53)],c,edge,2)+line(465,9,465,-20,edge,3)+line(449,-8,482,-8,edge,3)
 for j in range(6):s+=rect(422+j*12,100,9,13,low,1)
 for j in range(9):s+=rect(112+j*57,214,16,5,low,2)
 s+=path('M82 196 H260 M527 196 H659 M666 201 L752 181',edge,2)+line(104,164,240,164,'#E5ECE7',2)
 s+=path('M40 247 L92 259 L704 252 L747 234',edge,1.2,op=.75)
 for z in (162,208,309,360,418,574,610):s+=line(z,205,z-2,234,edge,1,op=.55)
 for z in (112,152,192):s+=rect(z,176,23,11,low,1,op=.6)
 s+=poly([(296,119),(382,119),(410,89),(399,119),(390,158),(280,158)],light,edge,1,op=.65)
 s+=line(438,55,477,55,'#E5ECE7',2)+line(559,146,628,146,'#E5ECE7',2)
 # Subtle deck lighting separated from silhouette.
 for j in range(3):s+=circ(315+j*67,190,3,'#70D3CC',op=.55+.22*math.sin(t*3+j))
 return f'<g transform="translate({x} {y}) scale({w/800})">{s}</g>'
def bg(i,t):
 th=SCENES[i][0];dark=th=='midnight';saf=th=='saffron';s=rect(0,0,W,H,DK if dark else OR if saf else IV)
 if i==0:
  s+='<defs><linearGradient id="sea" x2="0" y2="1"><stop stop-color="#173A47"/><stop offset="1" stop-color="#0B1018"/></linearGradient></defs>'+rect(0,680,W,770,'url(#sea)')
  for j in range(13):
   y=812+j*49;s+=path(f'M0 {y} Q270 {y-14+6*math.sin(t+j)} 540 {y} T1080 {y}', '#548D99',2,op=.19)
 elif i==1:
  for k in range(21):s+=line(72,624+k*38,1008,624+k*38,'#A8BAB6',1,.2)
  for k in range(25):s+=line(72+k*39,624,72+k*39,1400,'#A8BAB6',1,.2)
 elif i==2:
  for j in range(8):s+=path(f'M72 {630+j*100} Q290 {600+j*100} 540 {650+j*100} T1008 {630+j*100}', '#94B2AA',1.5,op=.23)
 elif i==3:
  for j in range(10):s+=line(60+j*112,640,260+j*112,1400,'#934922',2,.16)
 elif i==4:
  for j in range(7):
   x=92+j*148;s+=path(f'M{x} 680 V{800+(j%3)*90} H{x+45} V1380','#92ADA3',2,op=.2)
 elif i==5:
  for j in range(11):
   y=690+j*66;s+=path(f'M0 {y} Q540 {y-60-j*3} 1080 {y}','#37616B',2,op=.28)
 return s

def metric(x,y,value,label,dt,delay,id,c,fg,size=90,suffix=''):
 p=ease((dt-delay)/.9);num=round(value*p); v=f'{num:,}'+suffix
 s=group(txt(x,y,v,size,c,800,'middle'),id,p,f'translate(0 {(1-p)*16:.2f})')
 return s+typed(x,y+53,label,30,fg,dt,delay+.18,id+'-label',500,'middle')

def hero(i,dt,t,dark):
 th=SCENES[i][0];fg=IV if dark else INK;c=MINT if dark else DK if th=='saffron' else TEAL;s=''
 if i==0:
  p=ease(dt/.48);s+=group(ship(105,740,870,t,True),'opening-ship',.22+.78*p,f'translate(0 {(1-p)*48+math.sin(t*1.3)*2:.2f})')
  s+=typed(540,1120,'Vindhyagiri',57,IV,dt,.65,'ship-name',700,'middle')
  for j in range(7):
   p=ease((dt-2.3-j*.25)/.45);s+=group(ship(139+j*117,1190,100,t,True),f'delivery-{j}',p)
  s+=typed(540,1322,'7 / 7 delivered',62,MINT,dt,4.1,'complete',800,'middle')
 elif i==1:
  s+=reveal(ship(122,750,836,t), 'ship-profile',dt,.35,.6,35,0)
  # Dimension line separate from labels above and below. No overlaps with hull.
  p=ease((dt-3.5)/.75);s+=group(line(124,1105,124+832*p,1105,TEAL,4)+line(124,1084,124,1126,TEAL,4)+line(124+832*p,1084,124+832*p,1126,TEAL,4),'measure',p)
  s+=metric(290,1235,149,'metres long',dt,3.5,'length',TEAL,fg,87,' m')
  s+=metric(790,1235,6670,'fully loaded',dt,7.0,'weight',TEAL,fg,72,' t')
 elif i==2:
  s+=reveal(group(path(MAP['path'],'#648B84',2,'#D5E6DC'),'map-scale',1,'translate(540 940) scale(1.16) translate(-540 -965)'),'map',dt,0,.55,0,10)
  # Pins on map; labels in independent lower columns, no lines through text.
  for j,city in enumerate(['Mumbai','Kolkata']):
   xx,yy=MAP[city];x=540+(xx-540)*1.16;y=940+(yy-965)*1.16;delay=.6+j*2.9;p=ease((dt-delay)/.6);ex=310 if j==0 else 795;end=x-18 if j==0 else x+18;s+=group(circ(x,y,16,IV,TEAL,4)+circ(x,y,6,TEAL)+line(end,y,ex,y,TEAL,3),f'pin{j}',p);s+=typed(295 if j==0 else 810,y+10,city,30,TEAL,dt,delay+.1,f'mapcity{j}',700,'end' if j==0 else 'start')
  for j,(x,city,yard,n,delay) in enumerate([(270,'Mumbai','Mazagon Dock',4,.6),(810,'Kolkata','Garden Reach',3,3.5)]):
   s+=typed(x,1238,yard,38,TEAL,dt,delay+.2,f'yard{j}',700,'middle')+typed(x,1281,city,28,fg,dt,delay+.2,f'city{j}',500,'middle')
   for k in range(n):s+=reveal(ship(x-(n*93-8)/2+k*93,1320,85,t),f'yardship{j}-{k}',dt,delay+.4+k*.18,.45,12,0)
   s+=typed(x,1422,f'{n} warships',30,fg,dt,delay+.65,f'count{j}',700,'middle')
 elif i==3:
  s+=metric(540,785,23,'months: first to final delivery',dt,.4,'span',DK,fg,114)
  # Bars are redrawn with rounded ends on each step, labels outside the bars.
  for j,(n,label,delay) in enumerate([(84,'First frigate',4.3),(68,'Final frigate',5.6)]):
   y=987+j*186;p=ease((dt-delay)/1);s+=typed(110,y-24,label,33,DK,dt,delay,f'barlabel{j}',700)
   s+=group(rect(110,y,860,42,'#9C4D2C',21,op=.35)+rect(110,y,860*n/84*p,42,IV,min(21,860*n/84*p/2)),f'bar{j}',p)
   s+=group(txt(970,y+100,f'{round(n*p)} months',42,DK,700,'end'),f'months{j}',p)
  s+=typed(540,1407,'16 months faster',49,DK,dt,8.0,'faster',800,'middle')
 elif i==4:
  p=ease((dt-.4)/1.1);s+=circ(540,884,198,'none','#CFDDD5',28)
  s+=path(f'M540 686 A198 198 0 {1 if p*.75>.5 else 0} 1 {540+198*math.sin(2*math.pi*.75*p):.3f} {884-198*math.cos(2*math.pi*.75*p):.3f}',TEAL,28) if p>0 else ''
  s+=group(txt(540,922,f'{round(75*p)}%',111,TEAL,800,'middle'),'percent',p)
  s+=typed(540,1150,'Indigenous content',43,fg,dt,.65,'indig',700,'middle')
  s+=metric(540,1300,200,'MSMEs across India',dt,4.7,'msme',TEAL,fg,90,'+')
 elif i==5:
  # Same proportional ship artwork; seven staggered formations.
  for j,(x,y,w) in enumerate([(205,680,320),(555,680,320),(104,915,265),(408,915,265),(712,915,265),(205,1145,320),(555,1145,320)]):
   p=ease((dt-.25-j*.27)/.6);s+=group(ship(x,y,w,t,True),f'formation-{j}',p,f'translate({(1-p)*28:.2f} {(1-p)*20+math.sin(t+j)*2:.2f})')
  s+=typed(540,1398,'Seven delivered. One milestone.',42,MINT,dt,3.4,'close',700,'middle')
 return s

def frame(t):
 i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=t-BOUNDS[i];theme,kicker,heads,_=SCENES[i];dark=theme=='midnight';saf=theme=='saffron';fg=IV if dark else INK;ac=MINT if dark else DK if saf else BROWN
 a=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">',bg(i,t),f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{logo}</svg>',rect(730,100,278,65,IV if dark else DK,33),txt(869,139,'DEFENCE',25,DK if dark else IV,500,'middle',extra='letter-spacing=".7"')]
 a.append(typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"'))
 size=min(91,int(min(900/max(1,tw(h,91))*91 for h in heads)))
 for j,h in enumerate(heads):a.append(typed(83,438+j*109,h,size,fg,dt,j*.18,'headline'+str(j),800,extra='letter-spacing="-2"'))
 a.append(hero(i,dt,t,dark))
 # Provisional captions: estimated pacing only, replaced by acoustic alignment in narrated render.
 words=SCRIPTS[i].replace('Project Seventeen A','Project 17A').split();groups=[];g=[]
 for w in words:
  if g and (len(g)>=5 or sum(tw(z,51) for z in g+[w])+14*len(g)>700):groups.append(g);g=[]
  g.append(w)
 if g:groups.append(g)
 idx=max(0,min(len(words)-1,int((dt-.2)/max(.1,BOUNDS[i+1]-BOUNDS[i]-.5)*len(words))));pos=0
 for g in groups:
  if idx<pos+len(g):v=g[:idx-pos+1];break
  pos+=len(g)
 size=51;ws=[tw(w,size) for w in v];total=sum(ws)+14*(len(v)-1);x=540-total/2
 a.append(rect(x-24,1501,total+48,112,DK,24,op=.76 if saf else .3 if dark else .1))
 for j,w in enumerate(v):
  a.append(txt(x,1578,w,size,(PEACH if dark or saf else BROWN) if j==len(v)-1 else IV if dark or saf else INK));x+=ws[j]+14
 sw=(912-5*14)/6
 for j in range(6):
  x=84+j*(sw+14);p=clip((t-BOUNDS[j])/(BOUNDS[j+1]-BOUNDS[j]));a.append(rect(x,1721,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5));a.append(rect(x,1721,sw*p,13,IV if saf else OR,min(6.5,sw*p/2)))
 return ''.join(a)+'</svg>'

