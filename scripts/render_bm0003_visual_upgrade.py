#!/usr/bin/env python3
"""Original animated CGI evidence visuals for BM-0003.

Works entirely in the current chat/container with Python/OpenCV/FFmpeg. Reuses the
already approved V6 title/caption/chapter/logo video and its mixed narration.
No real L&T or NVIDIA facility is represented; graphics are explicitly schematic.
Work is not part of this rendering process and must ONLY generate the six WAVs,
transcripts and word timings in future productions.
"""
import argparse, math, os, subprocess, json, time
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W,H=922,590
FPS=30
FRAMES=1245
X,Y=79,642
BG=(8,16,24) # RGB for aesthetics
TEAL=(115,224,214)
TEAL2=(37,140,148)
ORANGE=(243,136,70)
IVORY=(255,244,228)
MUTED=(146,177,182)
NIGHT=(8,15,23)
BORDER=(60,102,111)
DUR=[203,212,193,176,263,198]
BOUND=np.cumsum([0]+DUR).tolist()
REGULAR='/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf'
BOLD='/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'
font={size:ImageFont.truetype(BOLD,size) for size in [17,19,23,28,34,39,45,55,65,82]}
reg={size:ImageFont.truetype(REGULAR,size) for size in [17,19,23,28,34,39,45,55]}

def col(rgb):return tuple(rgb[::-1])
def cvline(im,p1,p2,color,th=1):cv2.line(im,tuple(map(int,p1)),tuple(map(int,p2)),col(color),th,cv2.LINE_AA)
def rect(im,x,y,w,h,color,th=-1):cv2.rectangle(im,(int(x),int(y)),(int(x+w),int(y+h)),col(color),th,cv2.LINE_AA)
def circle(im,x,y,r,color,th=-1):cv2.circle(im,(int(x),int(y)),int(r),col(color),th,cv2.LINE_AA)
def polygon(im,pts,color,th=-1):
 poly=np.array(pts,dtype='int32'); cv2.fillConvexPoly(im,poly,col(color),cv2.LINE_AA) if th<0 else cv2.polylines(im,[poly],True,col(color),th,cv2.LINE_AA)
def opacityblend(im,ov,opacity):return cv2.addWeighted(im,1-opacity,ov,opacity,0)
def text(im,where,s,size=23,color=IVORY,bold=False,anchor=None,stroke=0):
 if not s:return im
 pim=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
 dr=ImageDraw.Draw(pim)
 f=(font if bold else reg)[size]
 dr.text(where,str(s),fill=color,font=f,anchor=anchor,stroke_width=stroke,stroke_fill=NIGHT)
 return cv2.cvtColor(np.asarray(pim),cv2.COLOR_RGB2BGR)
def blurb(im,slight=0.14):
 blurred=cv2.GaussianBlur(im,(0,0),12)
 return cv2.addWeighted(im,1-slight,blurred,slight,0)

# Static rounded dark panel with controlled background/scanline effects.
gridx=np.arange(W,dtype=np.float32)[None,:]
gridy=np.arange(H,dtype=np.float32)[:,None]
rx=np.broadcast_to(gridx,(H,W)); ry=np.broadcast_to(gridy,(H,W))
rad=np.sqrt(((rx-W*.53)/(W*.82))**2+((ry-H*.40)/(H*.86))**2)
vig=np.clip(1-.28*rad,0,1)
BASE=np.empty((H,W,3),dtype=np.uint8)
BASE[:,:,0]=np.uint8(np.clip((31+17*(1-ry/H))*vig,0,255))
BASE[:,:,1]=np.uint8(np.clip((24+26*(1-ry/H))*vig,0,255))
BASE[:,:,2]=np.uint8(np.clip((17+16*(1-ry/H))*vig,0,255))
# bgr base: deep teal navy
BASE=cv2.GaussianBlur(BASE,(3,3),0)
GLOW_SRC=np.zeros((H,W,3),dtype=np.uint8)
cv2.circle(GLOW_SRC,(W//2,H//2),170,col(TEAL2),-1)
GLOW_SRC=cv2.GaussianBlur(GLOW_SRC,(0,0),65)
for iy in range(50,H-48,39):cvline(BASE,(30,iy),(W-30,iy),(30,56,66),1)
for ix in range(45,W-38,54):cvline(BASE,(ix,40),(ix,H-35),(23,41,50),1)
MASK=np.zeros((H,W),dtype=np.uint8)
cv2.rectangle(MASK,(27,0),(W-27,H-1),255,-1)
cv2.rectangle(MASK,(0,27),(W-1,H-28),255,-1)
for px in [27,W-28]:
 for py in [27,H-28]:cv2.circle(MASK,(px,py),27,255,-1,cv2.LINE_AA)

# helpers shared by the story scene drawings
def backdrop(t,scene):
 im=BASE.copy()
 # ambient pulsing light in background
 cx=int((.52+.075*math.sin(t*.33+scene)) * W)
 cy=int((.48+.10*math.sin(t*.15))*H)
 glow=cv2.warpAffine(GLOW_SRC,np.float32([[1,0,cx-W//2],[0,1,cy-H//2]]),(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)
 im=cv2.addWeighted(im,1.0,glow,.20,0)
 for j in range(23):
  x=int((j*241.7+48)%W);y=int((j*179.3+13+t*(8+j%3*4))%(H-30))
  circle(im,x,y,1 if j%3 else 2,(63,113,123))
 # outer panel border and a thin sci-fi accent line
 cv2.rectangle(im,(0,0),(W-1,H-1),col(BORDER),2,cv2.LINE_AA)
 cvline(im,(35,73),(W-34,73),(45,94,100),2)
 cvline(im,(34,H-43),(W-34,H-43),(39,81,90),1)
 return im

def label_band(im,title,tag):
 im=text(im,(39,24),tag.upper(),19,TEAL,bold=True)
 im=text(im,(W-39,24),title.upper(),17,MUTED,anchor='ra')
 return im

def led_rack(im,bb,t,seed=0,shade=.9):
 x,y,w,h=bb
 # rounded-esque 3D rack frame with rails and servers
 polygon(im,[(x,y),(x+w,y),(x+w-3,y+h),(x+5,y+h)],(33,69,77))
 cv2.rectangle(im,(int(x+5),int(y+8)),(int(x+w-6),int(y+h-10)),col((7,17,23)),-1)
 cvline(im,(x+5,y+9),(x+w-6,y+9),(78,142,147),2)
 cvline(im,(x+9,y+h-11),(x+w-9,y+h-11),(40,87,94),2)
 for row in range(8):
  yy=y+21+row*(h-45)/8
  rect(im,x+12,yy,w-25,max(5,(h-46)/11),(18+seed*2,44,51))
  cvline(im,(x+15,yy+3),(x+w-33,yy+3),(51,86,98),1)
  active=math.sin(t*(2.8+row*.08)+seed*4+row*3.21)>-.2
  circle(im,x+w-23,yy+5,2 if active else 1,TEAL if active else (43,69,70))

def gpu_chip(im,x,y,w,h,t,shade=1):
 # chip pad/shadow
 rect(im,x+13,y+16,w,h,(8,23,30))
 polygon(im,[(x+15,y),(x+w,y+8),(x+w-6,y+h),(x+5,y+h-12)],(24,56,70))
 cv2.rectangle(im,(int(x+36),int(y+24)),(int(x+w-36),int(y+h-33)),col((12,24,35)),-1)
 cv2.rectangle(im,(int(x+35),int(y+23)),(int(x+w-36),int(y+h-33)),col(TEAL2),2)
 for dx in range(0,w-40,26):
  cvline(im,(x+18+dx,y-11),(x+18+dx,y+4),(57,138,152),2)
  cvline(im,(x+18+dx,y+h-1),(x+18+dx,y+h+13),(57,138,152),2)
 for dy in range(0,h-32,24):
  cvline(im,(x-10,y+18+dy),(x+5,y+18+dy),(57,138,152),2)
  cvline(im,(x+w-3,y+18+dy),(x+w+14,y+18+dy),(57,138,152),2)
 # die core
 core=(x+w/2,y+h/2)
 circle(im,*core,min(w,h)*.17,(51,132,144))
 circle(im,*core,min(w,h)*.11,TEAL)
 for a in np.linspace(0,2*math.pi,8,endpoint=False):
  q=(core[0]+math.cos(a)*w*.27,core[1]+math.sin(a)*h*.24)
  cvline(im,core,q,(45,124,133),2)

# CGI scene 1: animated parallax server-room aisle
def scene0(im,t):
 van=(460,205)
 for k in range(12):
  yy=van[1]+(H-van[1])*(k/11)**1.65
  cvline(im,(0,yy),(W,yy),(38,84,91),1)
 for x in np.arange(-700,W+800,120):cvline(im,van,(x,H),(25,65,78),1)
 # aisle receding walls, moving racks: simulate Z motion
 for side in [-1,1]:
  for k in range(9):
   z=((k/9 + t*.13) %1.0)
   depth=0.05+z*z
   ww=13+125*depth
   hh=45+440*depth
   nearx=van[0]+side*(80+((W*.5-80)*depth))
   bx=nearx-ww if side<0 else nearx
   y=van[1]-hh*.45
   if bx<0 or bx+ww>=W or y<0 or y+hh>H-30:continue
   led_rack(im,(bx,y,ww,hh),t,k,shade=depth)
  # converging floor light
  cvline(im,van,(0 if side<0 else W,H-65),(30,136,163),3)
 # central core pulse
 pulse=6+4*math.sin(t*4)
 circle(im,van[0],van[1],pulse,TEAL)
 cvline(im,(van[0]-55,van[1]),(van[0]+55,van[1]),(73,160,167),2)
 im=label_band(im,'AI NEEDS PHYSICAL MACHINES','01 / THE HIDDEN INFRASTRUCTURE')
 im=text(im,(40,H-108),'DATA CENTRES  /  CHIPS  /  POWER',28,IVORY,True)
 im=text(im,(40,H-69),'A schematic look inside AI compute',19,MUTED)
 return im

# CGI scene 2: GPU board deploying in Chennai, night skyline, schematic
def scene1(im,t):
 # city skyline/horizon with parallax
 for k in range(19):
  x=42+k*48
  yy=195+((k*31)%64)
  h=280-yy
  rect(im,x,yy,36,h,(12+ k%4*3,34+k%3*2,45+k%3*3))
  for wx in range(4):
   for wy in range(6):
    if (wx+wy+k)%3==0:
     rect(im,x+5+wx*8,yy+8+wy*15,3,6,(33,105,117))
 cvline(im,(27,289),(W-30,289),(60,114,124),2)
 # rack units arranged like a 'data centre site' build
 shift=15*math.sin(.55*t)
 for k in range(6):
  x=390+k*69+shift
  y=238-k*7
  led_rack(im,(x,y,54,200),t,k)
 # oscillating GPU-chip overlay left
 gpu_chip(im,77,220,242,192,t)
 # data flow from chip to server racks
 for j in range(5):
  yy=265+j*24
  cvline(im,(325,yy),(415,yy),(49,143,148),2)
  x=326+((t*92+j*28)%85)
  circle(im,x,yy,4,ORANGE)
 # caption chips
 im=label_band(im,'NEW MULTI-YEAR GPU ORDER','02 / CHENNAI')
 im=text(im,(62,137),'NVIDIA B300',45,IVORY,True)
 im=text(im,(62,192),'GPU deployment illustration',19,MUTED)
 im=text(im,(40,H-100),'CHENNAI  ·  INDIA',28,ORANGE,True)
 im=text(im,(40,H-64),'New order announced 23 November 2026',19,MUTED)
 return im

def scene2(im,t):
 # wide left rack columns behind large range graphical display
 for k in range(7):
  x=65+k*116
  h=140+((k*23)%80)
  led_rack(im,(x,250+(205-h),87,h),t,k)
 # luminous budget/range bar
 y=230
 cvline(im,(93,y),(W-93,y),(40,99,115),15)
 cvline(im,(202,y),(W-178,y),(64,185,179),10)
 for p in [202,W-178]:circle(im,p,y,12,ORANGE)
 pos=202+((W-178-202)*min(1,max(0,t/3.2)))
 circle(im,pos,y,9,IVORY)
 im=label_band(im,'ORDER VALUE BAND, NOT EXACT VALUE','03 / SCALE')
 im=text(im,(W//2,141),'Rs 2,500 – 5,000 Cr',55,IVORY,True,anchor='mm')
 im=text(im,(W//2,194),'L&T CLASSIFIES IT AS A LARGE ORDER',19,TEAL,True,anchor='mm')
 im=text(im,(40,H-96),'Contract amount: range disclosed',28,ORANGE,True)
 im=text(im,(40,H-61),'Exact amount and added GPU count undisclosed',19,MUTED)
 return im

def scene3(im,t):
 # Perspective of thousands of GPU capacity placeholders, staggerly lighting up
 cols,rows=32,12
 left,top=60,124
 for yy in range(rows):
  for xx in range(cols):
   x=left+xx*25.3+11*math.sin(t*.2+yy*.2)
   y=top+yy*26
   activation=(yy*cols+xx)/(cols*rows)
   bright=t/4.2>activation
   c=TEAL if bright else (33,59,67)
   rect(im,x,y,16,16,c)
   if (xx+yy)%11==0 and bright:
    circle(im,x+8,y+8,3,ORANGE)
 # vertical camera radar
 scanx=60+(t*152)%(W-120)
 cvline(im,(scanx,120),(scanx,455),(86,156,171),2)
 im=label_band(im,'CAPACITY PLAN / AUGUST ANNOUNCEMENT','04 / THE BIGGER PROJECT')
 im=text(im,(W//2,95),'10,000 GPUs',65,IVORY,True,anchor='mm')
 im=text(im,(40,H-96),'PLANNED CLUSTER',28,ORANGE,True)
 im=text(im,(40,H-63),'This is not a verified live GPU count',19,MUTED)
 return im

def scene4(im,t):
 # Left actively drawn conceptual future campus; right intentionally unspecified
 left=(48,132,392,320)
 right=(481,132,392,320)
 for xx,yy,ww,hh in [left,right]:
  cv2.rectangle(im,(xx,yy),(xx+ww,yy+hh),col((49,92,102)),2)
  rect(im,xx+2,yy+2,ww-4,hh-4,(15,32,41))
 for k in range(4):
  led_rack(im,(80+k*84,222,60,179),t,k)
 for k in range(5):
  x=520+k*64
  for q in range(5):
   y=237+q*32
   cv2.rectangle(im,(x,y),(x+47,y+23),col((46,64,69)),1)
 # Unknown over right, no depiction of active running racks
 circle(im,677,316,74,(25,50,61),2)
 im=text(im,(678,316),'?',82,MUTED,True,anchor='mm')
 im=label_band(im,'PLANNED IS NOT OPERATIONAL','05 / WHAT IS VERIFIED')
 im=text(im,(91,161),'PLANNED',28,TEAL,True)
 im=text(im,(506,161),'NOT CONFIRMED',28,ORANGE,True)
 im=text(im,(40,H-101),'The 10,000 figure is a plan',28,IVORY,True)
 im=text(im,(40,H-66),'Publicly verified active GPU count: undisclosed',19,MUTED)
 return im

def scene5(im,t):
 # AI core -> radial scientific applications with orbiting signal pulses
 core=(461,280)
 for r in [60,118,173,235]:cv2.circle(im,core,r,col((29,66,74)),2,cv2.LINE_AA)
 labs=[(220,150,'RESEARCH'),(700,148,'INDUSTRY'),(770,357,'SCIENCE'),(212,376,'COMPUTE'),(452,117,'AI')]
 for j,(x,y,lab) in enumerate(labs):
  cvline(im,core,(x,y),(46,112,120),2)
  p=(t*.26+j*.17)%1
  px=core[0]+(x-core[0])*p;py=core[1]+(y-core[1])*p
  circle(im,px,py,6,ORANGE)
  circle(im,x,y,31,(17,50,61))
  circle(im,x,y,24,TEAL2,2)
  circle(im,x,y,5,TEAL)
  im=text(im,(x,y+43),lab,17,IVORY,True,anchor='mm')
 gpu_chip(im,376,213,170,132,t)
 im=label_band(im,'INFRASTRUCTURE FOR WHAT COMES NEXT','06 / INDIA BUILDS')
 im=text(im,(40,H-98),'Powering the next generation',28,IVORY,True)
 im=text(im,(40,H-64),'Compute capacity is the foundation, not the outcome',19,MUTED)
 return im

DRAW=[scene0,scene1,scene2,scene3,scene4,scene5]
def render_scene(scene,local):
 im=backdrop(local,scene)
 im=DRAW[scene](im,local)
 # inner rounded highlights and wordless cinematic scanline animation
 cvline(im,(21,21),(W-22,21),(35,78,88),1)
 # black mask with rounded corners; note outside gets themed solid fill in subsequent compositing
 # Keep sharp corners here to avoid showing remnants of previous cards.
 return im

# Scan video scene durations are exact 30fps frame counts from Work's audio-build process.
def render_frame(frame):
 scene=max(0,min(5,np.searchsorted(BOUND,frame,side='right')-1))
 local=(frame-BOUND[scene])/FPS
 im=render_scene(scene,local)
 # minimal 0.34 second scene cross-dissolve, matching V6's clean and premium transition language.
 transition_frames=10
 if scene>0 and frame-BOUND[scene]<transition_frames:
  q=(frame-BOUND[scene])/transition_frames
  prev=(frame-BOUND[scene-1])/FPS
  old=render_scene(scene-1,prev)
  im=cv2.addWeighted(old,1-q,im,q,0)
 return im

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--input',default='out/BM-0003-review.mp4')
 parser.add_argument('--out',default='out/BM-0003-visual-upgrade.mp4')
 parser.add_argument('--graphics-only',action='store_true')
 parser.add_argument('--check',action='store_true')
 args=parser.parse_args()
 out=Path(args.out);out.parent.mkdir(exist_ok=True,parents=True)
 if args.check:
  stamps=[55,256,466,697,861,1110]
  imgs=[]
  for fr in stamps:
   scene=render_frame(fr)
   sm=cv2.resize(scene,(690,443),interpolation=cv2.INTER_AREA)
   imgs.append(sm)
   cv2.imwrite(str(out.parent/f'graphic_sample_{fr:04d}.png'),scene)
  sheet=np.vstack([np.hstack(imgs[:3]),np.hstack(imgs[3:])])
  cv2.imwrite(str(out.parent/'visual-storyboard.png'),sheet)
  print('Wrote visual-storyboard.png')
  return
 # render entire dynamic graphic with software h264 (not Work, no APIs)
 graphics=out.parent/'BM-0003-generated-graphics.mp4'
 enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}',
                       '-r',str(FPS),'-i','pipe:0','-an','-c:v','libx264','-preset','veryfast','-crf','20',
                       '-pix_fmt','yuv420p','-movflags','+faststart',str(graphics)],stdin=subprocess.PIPE)
 for frame in range(FRAMES):
  im=render_frame(frame)
  try:enc.stdin.write(im.tobytes())
  except BrokenPipeError:raise RuntimeError('FFmpeg graphics encoder failed')
  if frame%300==0:print(f'Graphics render {frame}/{FRAMES}',flush=True)
 enc.stdin.close();ret=enc.wait()
 if ret:raise RuntimeError('Encoding failed: '+str(ret))
 print('Motion graphics encoded:',graphics.stat().st_size,flush=True)
 if args.graphics_only:return
 # Composite new visual sequences into EXISTING approved V6 frame; stream-copy original narration/music.
 cmd=['ffmpeg','-y','-loglevel','error','-i',str(args.input),'-i',str(graphics),
      '-filter_complex',f'[0:v][1:v]overlay=x={X}:y={Y}:shortest=1:format=auto[v]',
      '-map','[v]','-map','0:a:0','-c:v','libx264','-preset','veryfast','-crf','19',
      '-pix_fmt','yuv420p','-r',str(FPS),'-c:a','copy','-movflags','+faststart',str(out)]
 subprocess.run(cmd,check=True)
 print('Finished',str(out),out.stat().st_size,flush=True)

if __name__=='__main__':main()