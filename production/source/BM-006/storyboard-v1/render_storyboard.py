from pathlib import Path
import math, html, json, base64, bisect, zipfile
import cairosvg
from PIL import Image, ImageDraw, ImageFont
B=Path(__file__).resolve().parent
W,H=1080,1920
IV='#FFF7EB'; DK='#0B1018'; INK='#283039'; TEAL='#117A7A'; OR='#E8752E'; MINT='#70D3CC'; PEACH='#FFBE91'; BROWN='#A63F17'
FONTS='/usr/share/fonts/opentype/inter/'
SCRIPTS=["Chariot Artificial Intelligence, an Indian AI company, has unveiled Chariot One, a family of language and speech models trained from scratch in India.","Its largest language model contains nearly eleven billion parameters, but selectively activates around four billion for each token it processes.","Its IndicShift technology represents characters from twelve Indian scripts using a shared alphabet, reportedly reducing the number of tokens needed by up to sixty percent.","Another innovation, called Nested Training, allows three differently sized models to be developed through a single training run.","Chariot's speech model also supports English and at least ten Indian languages, interpreting numbers, abbreviations and measurements in context.","Supported by the IndiaAI Mission, Chariot is helping build AI technology designed around India's own linguistic diversity."]
BOUNDS=[0,10,19,30,38,47,55]
SCENES=[('midnight','TRAINED FROM SCRATCH IN INDIA',['Chariot-1','Homegrown AI'],'silicon-network'),('ivory','MIXTURE OF EXPERTS',['Selective','activation'],'routing-grid'),('saffron','INDICSHIFT',['Many scripts.','Shared symbols.'],'script-matrix'),('ivory','NESTED TRAINING',['Three models.','One training run.'],'nested-contours'),('midnight','MULTILINGUAL SPEECH',['From text','to natural speech.'],'audio-spectrum'),('ivory','INDIAAI MISSION',['AI for a','multilingual India.'],'connected-services')]
logo=(B/'avatar.svg').read_text();logo=logo[logo.index('>')+1:logo.rindex('</svg>')]
def clip(x):return max(0,min(1,x))
def ease(x):return 1-(1-clip(x))**3
def tw(s,size,weight=700):return ImageFont.truetype(FONTS+('Inter-Bold.otf' if weight>=700 else 'Inter-Medium.otf'),int(size)).getlength(s)
def esc(s):return html.escape(str(s))
def txt(x,y,s,size=40,fill=INK,weight=700,anchor='start',extra=''):
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
 local=dt-delay;p=ease(local/.56); n=min(len(s),max(0,int(local*18)+1)) if local>=0 else 0
 # Preserve the full label anchor during typing, so partial text doesn't shift laterally.
 left=x-tw(s,size,weight)/2 if anchor=='middle' else x-tw(s,size,weight) if anchor=='end' else x
 return group(txt(left,y,s[:n],size,c,weight,extra=extra),id,p,f'translate({(1-p)*28:.2f} 0)')
def pulse(x,y,t,c,r=7):return circ(x,y,r*2.7,c,op=.09+.08*math.sin(t*4))+circ(x,y,r,c,op=.7+.3*math.sin(t*4))
def trace(d,c,p,width=5):return f'<path d="{d}" stroke="{c}" stroke-width="{width}" fill="none" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="{100*clip(p):.3f} 100"/>'
def check(x,y,c,scale=1):return path(f'M{x} {y} l{13*scale} {13*scale} l{25*scale} {-28*scale}',c,5*scale)
# All graphics are original conceptual technical illustrations, not actual Chariot architecture or UI.
def poly(pts,fill,stroke='none',w=1,op=1):return path('M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in pts)+' Z',stroke,w,fill,op)
def bg(i,t):
 theme=SCENES[i][0];dark=theme=='midnight';saf=theme=='saffron';base=DK if dark else OR if saf else IV
 s=rect(0,0,1080,1920,base);c='#395B65' if dark else '#803F22' if saf else '#89A8A0'
 if i==0:
  s+='<defs><radialGradient id="glow"><stop stop-color="#1C4149"/><stop offset="1" stop-color="#0B1018"/></radialGradient></defs>'+ell(540,1020,690,610,'url(#glow)')
  for k in range(11):
   x=70+k*94;s+=path(f'M{x} 620 V{790+k%3*45} L{x+40} {830+k%3*45} V1440',c,2,op=.32)
 elif i==1:
  for k in range(18):s+=line(80,620+k*48,1000,620+k*48,c,1,.22)
  for k in range(20):s+=line(80+k*48,620,80+k*48,1436,c,1,.20)
 elif i==2:
  for k in range(9):s+=ell(540,1050,180+k*58,135+k*42,'none',c,2,.18)
 elif i==3:
  for k in range(9):s+=path(f'M{80+k*36} 1330 L{540+k*36} 655 L{1000+k*36} 1330',c,1.7,op=.17)
 elif i==4:
  for j in range(24):
   x=90+j*39;h=80+65*(1+math.sin(j*1.3+t*.8));s+=line(x,980-h,x,980+h,c,2,.24)
  for j in range(6):s+=line(84,700+j*145,996,700+j*145,c,1,.3)
 else:
  for j in range(9):s+=path(f'M{90+j*110} 650 V{790+(j%3)*150} H{130+j*110} V1435',c,2,op=.22)
 return s

def chip(x,y,w,h,t,dark=True):
 # Layered substrate, etched traces, pins and fine die cells.
 c='#71D3CC' if dark else TEAL; a=rect(x-w/2+12,y-h/2+18,w,h,'#111F2A',20,op=.4)
 a+=rect(x-w/2,y-h/2,w,h,'#163A44' if dark else '#C9DCD3',20,c,3)
 for j in range(15):
  xx=x-w/2+22+j*(w-44)/14
  for sg in [-1,1]:a+=line(xx,y+sg*h/2,xx,y+sg*(h/2+24),c,3,.8)
 for j in range(10):
  yy=y-h/2+20+j*(h-40)/9
  for sg in [-1,1]:a+=line(x+sg*w/2,yy,x+sg*(w/2+24),yy,c,3,.8)
 a+=rect(x-w*.34,y-h*.34,w*.68,h*.68,'#0D202A' if dark else '#E8F0E7',8,c,2)
 for j in range(8):
  for k in range(5):
   xx=x-w*.30+j*w*.076;yy=y-h*.28+k*h*.112;active=(j+2*k+int(t*3))%7==0
   a+=rect(xx,yy,w*.062,h*.089,PEACH if active else c,2,op=.85 if active else .24)
 return a

def drawlink(x,y,X,Y,p,c,w=4):
 p=clip(p);return line(x,y,x+(X-x)*p,y+(Y-y)*p,c,w) if p>0 else ''

def hero(i,dt,t,dark):
 saf=SCENES[i][0]=='saffron';fg=IV if dark else INK;ac=MINT if dark else DK if saf else TEAL;hi=PEACH if dark else DK if saf else BROWN; a=[]
 def R(s,id,d,dur=.55,dx=30,dy=12):a.append(reveal(s,id,dt,max(0,d-.35),dur,dx,dy))
 def T(x,y,s,size,c,d,id,anchor='start',weight=700):a.append(typed(x,y,s,size,c,dt,max(0,d-.35),id,weight,anchor))
 if i==0:
  R(chip(540,1000,400,330,dt),'processor',1.2,.85,0,30)
  for j,(x,y) in enumerate([(200,780),(880,780),(200,1200),(880,1200)]):
   p=ease((dt-2.6-j*.25)/.7);X=340 if x<540 else 740;Y=920 if y<1000 else 1080
   if p>0:a.append(drawlink(X,Y,x,y,p,MINT,3));a.append(circ(X+(x-X)*p,Y+(y-Y)*p,7,PEACH))
   R(chip(x,y,126,94,dt+j),'node'+str(j),3+j*.25,.6,0,8)
  T(540,670,'Chariot Artificial Intelligence',39,IV,.4,'company','middle')
  T(540,1370,'Language models  +  Speech models',35,MINT,5.1,'suite','middle')
 elif i==1:
  T(86,698,'10.7B',100,BROWN,.8,'total',weight=800);T(90,752,'Total parameters',32,INK,1.0,'total-label')
  T(990,698,'4B',100,TEAL,3.4,'active','end',800);T(990,752,'Active per token',32,INK,3.6,'active-label','end')
  R(rect(370,810,340,74,'#DBE9DE',9,TEAL,2),'input',1.6, .4,0,10);T(540,857,'Input token',32,INK,1.8,'input-t','middle')
  R(chip(540,974,180,94,dt,False),'router',2.3,.5,0,10);T(540,984,'Router',29,INK,2.5,'router-label','middle')
  for j in range(6):
   x=130+164*j;p=ease((dt-3.4-j*.10)/.6);active=j in (1,4)
   if p>0:a.append(drawlink(540,1045,x,1130,p,OR if active else '#A2B9B0',5 if active else 2))
   R(chip(x,1190,104,104,dt+j,False),'expert'+str(j),3.5+j*.1,.5,0,10)
   if active and dt>4.1:a.append(rect(x-61,1129,122,122,'none',10,OR,4,.8))
   p=ease((dt-5.0-j*.1)/.6)
   if active and p>0:a.append(drawlink(x,1253,540,1333,p,TEAL,4))
  T(540,1390,'Selective computation',38,TEAL,5.7,'output','middle')
 elif i==2:
  T(540,660,'12 Indian scripts',50,DK,.7,'scripts','middle')
  for j,(glyph,name,font) in enumerate([('क','Devanagari','Noto Sans Devanagari'),('ಕ','Kannada','Noto Sans Kannada'),('క','Telugu','Noto Sans Telugu'),('ক','Bengali','Noto Sans Bengali')]):
   x=147+j*262;z=rect(x-82,727,164,138,'#FFF7EB',12,DK,2,.95)+f'<text x="{x}" y="815" font-family="{font}" font-size="68" text-anchor="middle" fill="{DK}">{glyph}</text>'
   R(z,'script'+str(j),1.4+j*.3,.5,0,14);T(x,906,name,27,DK,2+j*.3,'script-label'+str(j),'middle')
   p=ease((dt-4.0-j*.15)/.8)
   if p>0:a.append(drawlink(x,930,540,1040,p,DK,3))
  R(rect(285,1030,510,94,DK,12),'shared',4.6,.55,0,10);T(540,1088,'Shared representation',36,IV,4.7,'shared-label','middle')
  T(90,1203,'Normalized token count',31,DK,6.1,'comparison')
  for j,(label,w,c) in enumerate([('100',740,IV),('40',296,DK)]):
   y=1230+j*78;p=ease((dt-6.6-j*.55)/.9);ww=w*p
   if ww>0:a.append(rect(90,y,ww,45,c,min(12,ww/2)))
   T(860,y+34,label,33,DK,7.1+j*.55,'bar'+str(j))
  T(540,1430,'Up to 60% fewer tokens · reported',35,DK,7.6,'claim','middle')
 elif i==3:
  R(chip(540,775,330,160,dt,False),'training',.8,.7,0,15);T(540,910,'Shared training run',38,TEAL,1.1,'run','middle')
  for j,(x,n,dim) in enumerate([(195,'10.7B',164),(540,'1.7B',132),(885,'745M',100)]):
   p=ease((dt-3.1-j*.22)/.8)
   if p>0:a.append(drawlink(540,940,x,1110,p,TEAL,4))
   R(chip(x,1210,dim,dim,dt+j,False),'size'+str(j),3.8+j*.25,.6,0,12)
   T(x,1360,n,53,BROWN,4.4+j*.25,'size-label'+str(j),'middle',800)
  T(540,1440,'Three different model sizes',34,INK,5.4,'three','middle')
 elif i==4:
  T(540,680,'English + 10 Indian languages',43,MINT,.9,'langs','middle')
  # Context-aware example is illustrative, not model output.
  R(rect(140,760,800,156,'#172D38',14,'#476C76',2),'text-surface',2.8,.65,0,14)
  T(540,860,'₹1,500',83,IV,3.1,'written','middle',800)
  p=ease((dt-4.1)/.6)
  if p>0:a.append(drawlink(540,930,540,1020,p,MINT,4))
  for j in range(65):
   x=110+j*13.2;h=(18+75*abs(math.sin(j*.24+dt*2))*abs(math.cos(j*.37-dt*1.8)))*ease((dt-4.5-j*.009)/.65)
   if h>0:a.append(line(x,1090-h,x,1090+h,MINT if j%5 else PEACH,6,.85))
  T(540,1260,'One thousand five hundred',40,IV,5.4,'spoken1','middle');T(540,1316,'rupees',40,IV,5.8,'spoken2','middle')
  T(540,1420,'Illustrative pronunciation',30,MINT,6.4,'example','middle',500)
 else:
  R(chip(540,815,260,160,dt,False),'core',.7,.65,0,15);T(540,955,'Multilingual AI',40,TEAL,1.2,'core-label','middle')
  for j,(x,name) in enumerate([(195,'Education'),(540,'Accessibility'),(885,'Digital services')]):
   p=ease((dt-2.5-j*.25)/.8)
   if p>0:a.append(drawlink(540,985,x,1130,p,TEAL,3))
   # Technical line illustrations: book, headset, phone.
   z=rect(x-85,1135,170,144,'#E1EBE0',12,TEAL,2)
   if j==0:z+=path(f'M{x} 1165 L{x-57} 1152 V1228 L{x} 1243 L{x+57} 1228 V1152 Z',TEAL,4,IV)+line(x,1165,x,1243,TEAL,3)+line(x-43,1182,x-12,1190,TEAL,3)+line(x+12,1190,x+43,1182,TEAL,3)
   elif j==1:z+=path(f'M{x-53} 1202 A53 53 0 0 1 {x+53} 1202',TEAL,7)+rect(x-61,1195,22,43,TEAL,6)+rect(x+39,1195,22,43,TEAL,6)+path(f'M{x+50} 1238 V1250 H{x+10}',TEAL,4)
   else:z+=rect(x-35,1150,70,110,IV,9,TEAL,4)+rect(x-24,1164,48,66,'#B9D9CE',3)+circ(x,1245,5,TEAL)
   R(z,'app'+str(j),3.2+j*.25,.6,0,12);T(x,1345,name,29,INK,3.8+j*.25,'app-label'+str(j),'middle')
  T(540,1432,'Potential applications',32,TEAL,5.2,'potential','middle')
 return ''.join(a)

def frame(t):
 i=min(5,bisect.bisect_right(BOUNDS,t)-1);dt=t-BOUNDS[i];theme,kicker,heads,_=SCENES[i];dark=theme=='midnight';saf=theme=='saffron';fg=IV if dark else INK;ac=MINT if dark else DK if saf else BROWN
 a=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">',bg(i,t),f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{logo}</svg>',rect(730,100,278,65,IV if dark else DK,33),txt(869,139,'ARTIFICIAL INTELLIGENCE',17,DK if dark else IV,500,'middle',extra='letter-spacing=".7"')]
 a.append(typed(86,312,kicker,26,ac,dt,0,'kicker',extra='letter-spacing="2.3"'))
 size=min(91,int(min(900/max(1,tw(h,91))*91 for h in heads)))
 for j,h in enumerate(heads):a.append(typed(83,438+j*109,h,size,fg,dt,j*.18,'headline'+str(j),800,extra='letter-spacing="-2"'))
 a.append(hero(i,dt,t,dark))
 # Provisional captions: estimated pacing only, replaced by acoustic alignment in narrated render.
 words=SCRIPTS[i].replace('Chariot One','Chariot-1').split();groups=[];g=[]
 for w in words:
  if g and (len(g)>=5 or tw(' '.join(g+[w]),51)>700):groups.append(g);g=[]
  g.append(w)
 if g:groups.append(g)
 idx=max(0,min(len(words)-1,int((dt-.2)/max(.1,BOUNDS[i+1]-BOUNDS[i]-.5)*len(words))));pos=0
 for g in groups:
  if idx<pos+len(g):v=g[:idx-pos+1];break
  pos+=len(g)
 size=51;ws=[tw(w,size) for w in v];total=sum(ws)+14*(len(v)-1);x=540-total/2
 a.append(rect(x-24,1501,total+48,112,DK,24,op=.76 if saf else .3 if dark else .1))
 for j,w in enumerate(v):a.append(txt(x,1578,w,size,(PEACH if dark or saf else BROWN) if j==len(v)-1 else IV if dark or saf else INK));x+=ws[j]+14
 sw=(912-5*14)/6
 for j in range(6):
  x=84+j*(sw+14);p=clip((t-BOUNDS[j])/(BOUNDS[j+1]-BOUNDS[j]));a.append(rect(x,1721,sw,13,'#914D2D' if saf else '#607078' if dark else '#D4C8B7',6.5));a.append(rect(x,1721,sw*p,13,IV if saf else OR,min(6.5,sw*p/2)))
 return ''.join(a)+'</svg>'
