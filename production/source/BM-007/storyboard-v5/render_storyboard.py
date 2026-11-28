from pathlib import Path
import math, html, json, base64, bisect, zipfile, functools, re
from shapely.geometry import Polygon, box, LineString
from shapely.ops import unary_union
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
def lerp(a,b,t):return a+(b-a)*clip(t)
def smoothstep(a,b,x):
 t=clip((x-a)/max(1e-9,b-a));return t*t*(3-2*t)
@functools.lru_cache(maxsize=4096)
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
MUMBAI=tuple(MAP['Mumbai']); KOLKATA=tuple(MAP['Kolkata'])
def india_shape(fill='#D5E6DC',stroke='#648B84',sw=2):
 return path(MAP['path'],stroke,sw,fill)
def camera_content(content,id,z,fx,fy,cx,cy,top,bottom,left=68,right=1012):
 # Explicitly clipped artwork layer: text remains in screen coordinates outside it.
 return (f'<defs><clipPath id="{id}-clip"><rect x="{left}" y="{top:.3f}" width="{right-left}" height="{bottom-top:.3f}"/></clipPath></defs>'
  f'<g clip-path="url(#{id}-clip)"><g id="{id}" transform="translate({cx} {cy}) scale({z:.6f}) translate({-fx:.6f} {-fy:.6f})">{content}</g></g>')
def ship_camera(dt):
 # User requested left-to-right screen traversal: start at the left end, finish at the right.
 if dt<1.7:return 1,540,920
 if dt<3.0:
  u=smoothstep(1.7,3,dt);return lerp(1,1.95,u),lerp(540,255,u),lerp(920,990,u)
 if dt<6.6:
  u=smoothstep(3,6.6,dt);return 1.95,lerp(255,825,u),990
 u=smoothstep(6.6,8.2,dt);return lerp(1.95,1,u),lerp(825,540,u),lerp(990,920,u)
def map_camera(dt):
 if dt<.65:return 1.08,540,920
 if dt<1.65:
  u=smoothstep(.65,1.65,dt);return lerp(1.08,2.35,u),lerp(540,MUMBAI[0],u),lerp(920,MUMBAI[1],u)
 if dt<2.75:return 2.35,*MUMBAI
 if dt<4.2:
  u=smoothstep(2.75,4.2,dt);return 2.35,lerp(MUMBAI[0],KOLKATA[0],u),lerp(MUMBAI[1],KOLKATA[1],u)
 if dt<5.5:return 2.35,*KOLKATA
 u=smoothstep(5.5,6.55,dt);return lerp(2.35,1.08,u),lerp(KOLKATA[0],540,u),lerp(KOLKATA[1],920,u)
# Geographic annotations share the camera, but occupy genuinely empty space.
MAP_LABELS=[('Mumbai','Mazagon Dock',4,MUMBAI,-1,1.12),('Kolkata','Garden Reach Shipbuilders',3,KOLKATA,1,3.9)]
LAND=unary_union([Polygon([(float(x),float(y)) for x,y in re.findall(r'(-?[\d.]+),(-?[\d.]+)',part)]).buffer(0) for part in MAP['path'].split('Z') if len(re.findall(r'(-?[\d.]+),(-?[\d.]+)',part))>=3])
def map_label_state(j,dt):
 city,yard,n,(x,y),side,delay=MAP_LABELS[j]; z,fx,fy=map_camera(dt)
 sx=540+(x-fx)*z; sy=920+(y-fy)*z
 w,h=(215,142) if j==0 else (225,174)
 left=sx-75-w if j==0 else sx+135; top=sy+(40 if j==0 else 65)
 right=left+w; bottom=top+h
 # Test the full reserved label + ship icon rectangle against actual map polygons,
 # converted back to world coordinates. Margin includes the projected coast stroke.
 worldbox=box(fx+(left-540)/z,fy+(top-920)/z,fx+(right-540)/z,fy+(bottom-920)/z)
 clearance=LAND.distance(worldbox)*z-2*z
 margin=min(left-50,1030-right,top-600,1315-bottom,clearance-12)
 gate=smoothstep(0,8,margin)
 focus=(1-smoothstep(2.75,3.2,dt))+smoothstep(5.75,6.35,dt) if j==0 else 1
 op=clip(focus)*gate*smoothstep(delay,delay+.25,dt)
 return sx,sy,op,(left,top,right,bottom)
def leader_points(j,b,sx,sy):
 side=MAP_LABELS[j][4];left,top,right,bottom=b
 end=right+12 if side<0 else left-12
 return [(sx+side*11,sy),(sx+side*30,sy),(end,top+20)]
def map_label(j,dt,z):
 city,yard,n,(x,y),side,delay=MAP_LABELS[j];sx,sy,op,b=map_label_state(j,dt)
 if op<=0:return ''
 left,top,right,bottom=b; xx=(right if side<0 else left)-sx; yy=top-sy
 def mt(label,y,size,color,weight,lag):
  nchar=min(len(label),max(0,int((dt-delay-lag)*22)+1))
  if nchar==0:return ''
  fullw=tw(label,size,weight); tx=xx-fullw if side<0 else xx
  return txt(tx,y,label[:nchar],size,color,weight)
 pts=leader_points(j,b,sx,sy)
 # Leader stops before the label rectangle, never passing underneath text.
 content=path('M'+' L'.join(f'{px-sx:.3f} {py-sy:.3f}' for px,py in pts),TEAL,2.5)
 content+=mt(city,yy+42,40,TEAL,800,0)
 yard_lines=['Garden Reach','Shipbuilders'] if j==1 else [yard]
 for k,l in enumerate(yard_lines):content+=mt(l,yy+78+k*32,28,INK,700,.12+k*.25)
 count_y=yy+111+32*(len(yard_lines)-1)
 content+=mt(f'{n} warships',count_y,27,TEAL,700,.48+.25*(len(yard_lines)-1))
 for k in range(n):
  pp=ease((dt-delay-.5-k*.12)/.3)
  start=xx-(n*50-5) if side<0 else xx
  content+=group(ship(start+k*50,count_y+8,45,dt),f'mapship-{j}-{k}',pp)
 return group(content,f'geo-label{j}',op,f'translate({x} {y}) scale({1/z:.8f})')
def fleet_camera(dt):
 return lerp(2.95,1,smoothstep(.55,5.5,dt)),540,970
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
  pass # Uncluttered open water around geographic callouts.
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
  z,fx,fy=ship_camera(dt)
  # Heading leaves before artwork is allowed to expand upwards; restores only after return.
  expand=smoothstep(1.75,2.65,dt)*(1-smoothstep(7.0,8.2,dt));top=lerp(625,350,expand)
  scan=smoothstep(3.0,6.6,dt)
  shipg=ship(122,750,836,t)
  # World-space ruler grows from left to right, matching the camera traversal.
  if dt>=2.65:
   end=124+832*scan
   shipg+=line(124,1096,end,1096,TEAL,3)+line(124,1081,124,1111,TEAL,3)+line(end,1081,end,1111,TEAL,3)
   for k in range(1,15):
    q=k/14
    if q<=scan:shipg+=line(124+832*q,1096,124+832*q,1087,TEAL,1.7)
  s+=camera_content(shipg,'ship-camera',z,fx,fy,540,920,top,1150)
  # One uninterrupted measurement counter; slide into final column only after scan finishes.
  if dt>=2.8:
   slide=smoothstep(7.6,8.7,dt); op=smoothstep(2.8,3.15,dt)
   x=lerp(540,290,slide)
   s+=group(txt(x,1258,f'{round(149*scan)} m',83,TEAL,800,'middle'),'length',op)
   s+=typed(x,1311,'metres long',30,INK,dt,3.1,'length-label',500,'middle')
  s+=metric(790,1258,6670,'fully loaded',dt,8.85,'weight',TEAL,fg,72,' t')
 elif i==2:
  z,fx,fy=map_camera(dt)
  g=india_shape('#CEE3D8','#5D8A83',1.6)
  # Pins and their labels share the same map camera; no rectangular clip path.
  for j,(x,y) in enumerate((MUMBAI,KOLKATA)):
   p=ease((dt-(.4 if j==0 else 3.45))/.4)
   g+=group(circ(x,y,14/z,TEAL,op=.16)+circ(x,y,8/z,IV,TEAL,2.6/z)+circ(x,y,3.8/z,TEAL),f'geo-pin{j}',p)
  for j in range(2):g+=map_label(j,dt,z)
  s+=group(g,'map-camera',1,f'translate(540 920) scale({z:.6f}) translate({-fx:.6f} {-fy:.6f})')
  # Full-width soft fades reserve chrome and captions without creating visible square map edges.
  s+='<defs><linearGradient id="map-top-fade" x1="0" x2="0" y1="0%" y2="100%"><stop stop-color="#FFF7EB" stop-opacity="1"/><stop offset="1" stop-color="#FFF7EB" stop-opacity="0"/></linearGradient><linearGradient id="map-bottom-fade" x1="0" x2="0" y1="0%" y2="100%"><stop stop-color="#FFF7EB" stop-opacity="0"/><stop offset="1" stop-color="#FFF7EB" stop-opacity="1"/></linearGradient></defs>'
  s+=rect(0,0,1080,205,IV)+rect(0,205,1080,155,'url(#map-top-fade)')+rect(0,1325,1080,145,'url(#map-bottom-fade)')+rect(0,1470,1080,450,IV)
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
  z,fx,fy=fleet_camera(dt)
  # One continuous central ship; identical world geometry throughout pullback.
  world=[(410,925,260),(236,715,260),(584,715,260),(95,925,260),(725,925,260),(236,1135,260),(584,1135,260)]
  fleet=''
  for j,(x,y,w) in enumerate(world):
   delay=[0,2.4,2.6,2.8,3.0,3.2,3.4][j]
   # Conservative transformed bounds include stroke, mast and ongoing bobbing.
   x0=540+(x-3-fx)*z; x1=540+(x+w+3-fx)*z
   y0=970+(y-20*w/800-4-fy)*z; y1=970+(y+276*w/800+4-fy)*z
   margin=min(x0-68,1012-x1,y0-610,1330-y1)
   p=1 if j==0 else ease((dt-delay)/.55)*smoothstep(0,18,margin)
   fleet+=group(ship(x,y,w,t,True),f'formation-{j}',p,f'translate(0 {math.sin(t+j)*1.5:.2f})')
  s+=camera_content(fleet,'fleet-camera',z,fx,fy,540,970,610,1330)
  s+=typed(540,1410,'Seven delivered. One milestone.',42,MINT,dt,5.15,'close',700,'middle')
 return s

def frame(t):
 i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=t-BOUNDS[i];theme,kicker,heads,_=SCENES[i];dark=theme=='midnight';saf=theme=='saffron';fg=IV if dark else INK;ac=MINT if dark else DK if saf else BROWN
 a=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">',bg(i,t),hero(i,dt,t,dark) if i==2 else '',f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{logo}</svg>',rect(730,100,278,65,IV if dark else DK,33),txt(869,139,'DEFENCE',25,DK if dark else IV,500,'middle',extra='letter-spacing=".7"')]
 hdr_op=1
 if i==1:hdr_op=1-smoothstep(1.05,1.7,dt)+smoothstep(8.2,8.8,dt)
 if i==2:hdr_op=1-smoothstep(.3,.65,dt)+smoothstep(6.55,6.95,dt)
 header=typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"')
 size=min(91,int(min(900/max(1,tw(h,91))*91 for h in heads)))
 for j,h in enumerate(heads):header+=typed(83,438+j*109,h,size,fg,dt,j*.18,'headline'+str(j),800,extra='letter-spacing="-2"')
 a.append(group(header,'editorial-heading',clip(hdr_op)))
 if i!=2:a.append(hero(i,dt,t,dark))
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

