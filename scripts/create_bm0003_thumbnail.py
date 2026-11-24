from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json, math, numpy as np, shutil, hashlib, argparse, subprocess
ap=argparse.ArgumentParser(description='BM-0003 custom cover composite, using verified map, marks and approved MP4')
ap.add_argument('--video',type=Path,required=True);ap.add_argument('--assets',type=Path,required=True);ap.add_argument('--out-dir',type=Path,required=True)
args=ap.parse_args();P=args.out_dir;A=args.assets;P.mkdir(parents=True,exist_ok=True);W,H=1080,1920
subprocess.run(['ffmpeg','-v','error','-y','-ss','4','-i',str(args.video),'-frames:v','1',str(P/'ref.png')],check=True)
base=np.array([11,16,24],dtype=float); yy,xx=np.mgrid[:H,:W]; glow=np.exp(-((xx-580)/660)**2-((yy-1120)/640)**2)[...,None]; im=Image.fromarray(np.uint8(np.clip(base+glow*np.array([8,29,31]),0,255)),'RGB'); d=ImageDraw.Draw(im)
I='#FFF7EB'; S='#E8752E'; T='#7DD8CC'; muted='#A8C9C9'; fontdir=Path('/usr/share/fonts/opentype/inter')
def font(s,b=True):return ImageFont.truetype(str(fontdir/('InterDisplay-ExtraBold.otf' if b else 'Inter-Medium.otf')),s)
def tx(s,x,y,size,fill=I,b=True,anchor='lt',limit=None):
 f=font(size,b)
 while limit and d.textlength(s,font=f)>limit:
  size-=1; f=font(size,b)
 d.text((x,y),s,font=f,fill=fill,anchor=anchor)
def line(pts,fill,width=2):d.line(pts,fill=fill,width=width,joint='curve')
def poly(pts,fill,outline=None,width=1):
 d.polygon(pts,fill=fill)
 if outline:line([*pts,pts[0]],outline,width)
# unobtrusive environmental line work
for i in range(5):
 pts=[(x, int(1300+i*115+70*math.sin(x/270+i*.5))) for x in range(-30,1120,12)];line(pts,'#203D42',2)
# Brand mark reused from approved original raster, without redrawing
ref=Image.open(P/'ref.png'); logo=ref.crop((84,84,178,178)).resize((100,100),Image.Resampling.LANCZOS); mask=Image.new('L',(100,100),0); md=ImageDraw.Draw(mask); md.ellipse((1,1,98,98),fill=255); im.paste(logo,(72,93),mask)
tx('BHARAT MODE',193,123,32,I,True);tx('AI INFRASTRUCTURE',1008,126,26,T,False,'rt')
# Strong hierarchy and central mobile crop safe messaging
line([(80,236),(185,236)],S,8)
tx('L&T’s new',80,270,116,I,True,limit=920)
tx('AI order',80,396,143,I,True,limit=920)
tx('₹2,500–5,000',80,592,112,S,True,limit=920)
tx('CRORE  •  ORDER VALUE RANGE',84,720,33,muted,False,limit=920)
# map shape from the previously verified Natural Earth geometry
j=json.loads((A/'naturalearth-bm0003.json').read_text())
def decode(s):
 out=[];xy=[0,0];i=0
 while i<len(s):
  for ax in (0,1):
   v=shift=0
   while True:
    ch=ord(s[i])-63;i+=1;v|=(ch&31)<<shift;shift+=5
    if ch<32:break
   xy[ax]+=~(v>>1) if v&1 else v>>1
  out.append([q/10000 for q in xy])
 return np.array(out)
india=decode(j['india']); scale=14.5; lon=80; lat=22.8
# 30 deg width gives 430px; center on x=315, y=1100

def proj(a):
 a=np.atleast_2d(a);return [(round(306+(x-lon)*math.cos(math.radians(lat))*scale),round(1090-(y-lat)*scale)) for x,y in a]
for x in range(80,570,63):line([(x,815),(x,1365)],'#1A383D',1)
for y in range(815,1366,63):line([(80,y),(565,y)],'#1A383D',1)
poly(proj(india),'#225358','#639A97',3)
for k in ['Karnataka','Kerala','Andhra Pradesh']:
 line(proj(decode(j[k]))+[proj(decode(j[k]))[0]],'#508781',2)
poly(proj(decode(j['Tamil Nadu'])),S,'#FFBE91',3)
q=proj(j['chennai'])[0]
for r in [18,29,43]:d.ellipse([q[0]-r,q[1]-r,q[0]+r,q[1]+r],outline='#FFAD70',width=2)
d.ellipse([q[0]-9,q[1]-9,q[0]+9,q[1]+9],fill=I)
line([q,(q[0]+64,q[1]+44),(q[0]+148,q[1]+44)],'#FFBE91',2)
tx('Chennai',q[0]+25,q[1]+58,32,I,True)
# Custom GPU stack: 3D isometric modules, non-photographic schematic
for a in range(6):
 for b in range(5):
  x=604+a*65-b*28;y=1030+b*51-a*19
  # integrated data pathways
  poly([(x,y),(x+52,y-15),(x+77,y+3),(x+25,y+19)],'#5FABA7','#A6D8CA',1)
  poly([(x+25,y+19),(x+77,y+3),(x+77,y+18),(x+25,y+34)],'#155B61','#397D80',1)
  poly([(x,y),(x+25,y+19),(x+25,y+34),(x,y+15)],'#103C45','#397D80',1)
  line([(x+14,y+4),(x+48,y-6)],'#C2E9DF',2)
# GPU label in clear space above cluster
nv=Image.open(A/'nvidia_eye.png').convert('RGBA').resize((65,65),Image.Resampling.LANCZOS)
im.paste(nv,(608,856),nv); tx('NVIDIA',687,870,37,I);tx('B300 GPUs',609,925,35,T,False)
# secondary plan figure, visually distinct from new order
line([(80,1396),(1000,1396)],'#41666A',2)
tx('10,000',82,1430,86,I); tx('PLANNED GPUs',455,1447,43,T,True,limit=535);tx('Previously announced AI factory plan',457,1503,26,muted,False,limit=543)
# Separate verified company chain from supplier tech (already named above)
line([(80,1589),(1000,1589)],'#41666A',2)
lt=Image.open(A/'lt_badge.png').convert('RGB').resize((75,75),Image.Resampling.LANCZOS);im.paste(lt,(84,1620));tx('L&T',175,1634,42,I)
tx('Vyoma.AI',399,1635,40,I,True);tx('LTN Compute',704,1635,37,I,True,limit=296)
# keep footer free of clutter
out=P/'BM-0003-lt-chennai-ai-cluster-order-thumbnail.png';im.save(out,optimize=True)
shutil.copyfile(args.video,P/'BM-0003-lt-chennai-ai-cluster-order.mp4')
for p in [out,P/'BM-0003-lt-chennai-ai-cluster-order.mp4']:print(p.name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
im.resize((540,960),Image.Resampling.LANCZOS).save(P/'thumbnail-preview.jpg',quality=93)