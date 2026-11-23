#!/usr/bin/env python3
"""BM-0003 visual revision 3, rendered in the *main conversation*, never in Work.

Applies a geographically accurate 2.5D Natural Earth map/camera to the Chennai beat,
adds clearly identified businesses, and introduces subtle camera push/pan across the
other five existing CGI evidence sequences. Leaves original V6 branding, captions,
chapter bars, narration and MUSIC-06 Option B encoded audio completely unchanged.

The historic BM-0003 revision 2 MP4 is a temporary source *only for this episode*.
Future production must start with verified audio-only Work files in this chat.
"""
import argparse, json, math, hashlib, subprocess, sys
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

LT_BADGE = cv2.imread(str(Path(__file__).resolve().parent / 'lt_badge.png'),cv2.IMREAD_UNCHANGED)
NVIDIA_EYE = cv2.imread(str(Path(__file__).resolve().parent / 'nvidia_eye.png'),cv2.IMREAD_UNCHANGED)

def paste_png(im, icon, x, y, sz):
    if icon is None:return
    data=cv2.resize(icon,(sz,sz),interpolation=cv2.INTER_AREA)
    if data.shape[2]==4:
        alpha=data[:,:,3:4].astype(np.float32)/255.
        im[y:y+sz,x:x+sz] = (im[y:y+sz,x:x+sz].astype(np.float32)*(1-alpha)+data[:,:,:3]*alpha).astype(np.uint8)
    else: im[y:y+sz,x:x+sz]=data


ROOT=Path(__file__).resolve().parent
FONTS=['/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf','/usr/share/fonts/truetype/lato/Lato-Heavy.ttf']
REG='/usr/share/fonts/opentype/inter/Inter-Regular.otf'
if not Path(REG).exists(): REG='/usr/share/fonts/truetype/lato/Lato-Regular.ttf'

def font(size,bold=True):
    return ImageFont.truetype(next(p for p in (FONTS if bold else [REG]) if Path(p).exists()),size)

def decoded(s):
    xy=[0,0];i=0;out=[]
    while i<len(s):
        for axis in (0,1):
            value=shift=0
            while True:
                ch=ord(s[i])-63;i+=1;value|=(ch&31)<<shift;shift+=5
                if ch<32:break
            xy[axis]+= ~(value>>1) if value&1 else value>>1
        out.append([x/1e4 for x in xy])
    return np.asarray(out,np.float64)

def clamp(v,a=0,b=1):return max(a,min(b,v))
def smooth(x): x=clamp(x);return x*x*(3-2*x)
def tween(a,b,u):return a+(b-a)*smooth(u)

def new_canvas(w=928,h=626):
    yy=np.linspace(0,1,h)[:,None]
    img=np.empty((h,w,3),dtype=np.uint8)
    for c,(t,b) in enumerate(zip((42,32,9),(28,20,5))):img[:,:,c]=np.broadcast_to(t+(b-t)*yy,(h,w)).astype(np.uint8)
    for x in range(28,w,53):cv2.line(img,(x,0),(x,h),(44,43,22),1,cv2.LINE_AA)
    for y in range(22,h,53):cv2.line(img,(0,y),(w,y),(44,43,22),1,cv2.LINE_AA)
    return img

def project(coords,cen,zoom,w,h):
    lat0=cen[1]
    out=np.empty_like(coords)
    out[:,0]=w*.5+(coords[:,0]-cen[0])*math.cos(math.radians(lat0))*zoom
    out[:,1]=h*.5-(coords[:,1]-cen[1])*zoom
    return np.round(out).astype(np.int32)

def text(canvas,txt,x,y,sz=28,color=(240,247,251),bold=True,anchor=None):
    pil=Image.fromarray(cv2.cvtColor(canvas,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(pil)
    fill=tuple(int(c) for c in color)
    d.text((x,y),txt,font=font(sz,bold),fill=fill,anchor=anchor)
    return cv2.cvtColor(np.asarray(pil),cv2.COLOR_RGB2BGR)

def add_text_blocks(im,blocks):
    """Batch typography into one PIL pass; block colors are RGB."""
    pil=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(pil)
    for value,position,pt,rgb,bold in blocks:
        d.text(position,value,font=font(pt,bold),fill=rgb)
    return cv2.cvtColor(np.asarray(pil),cv2.COLOR_RGB2BGR)

def rounded(b,x0,y0,x1,y1,rad,color,thickness=-1):
    cv2.rectangle(b,(x0+rad,y0),(x1-rad,y1),color,thickness)
    cv2.rectangle(b,(x0,y0+rad),(x1,y1-rad),color,thickness)
    for (x,y) in [(x0+rad,y0+rad),(x1-rad,y0+rad),(x0+rad,y1-rad),(x1-rad,y1-rad)]:
        cv2.circle(b,(x,y),rad,color,thickness,cv2.LINE_AA)

def branded_panel(mapimg,u):
    h,w=mapimg.shape[:2]
    shade=mapimg.copy()
    cv2.rectangle(shade,(18,h-124),(w-18,h-18),(30,21,6),-1)
    cv2.addWeighted(shade,.87,mapimg,.13,0,mapimg)
    for x,ww in [(38,158),(211,210),(435,236),(689,215)]:
        rounded(mapimg,x,h-101,x+ww,h-40,10,(66,44,26))
    paste_png(mapimg,LT_BADGE,49,h-92,41)
    paste_png(mapimg,NVIDIA_EYE,705,h-91,42)
    blocks=[('L&T',(99,h-91),27,(245,250,250),True),
            ('Vyoma.AI',(228,h-88),27,(142,232,218),True),
            ('LTN Compute',(451,h-88),26,(245,250,250),True),
            ('NVIDIA',(752,h-87),25,(194,247,198),True),
            ('LARSEN & TOUBRO',(38,h-31),12,(147,178,179),False),
            ('B300 GPUS   /   EDITORIAL IDENTIFICATION',(486,h-31),12,(147,178,179),False)]
    return add_text_blocks(mapimg,blocks)

def map_hero(local,dur,geos,w=928,h=626):
    p=clamp(local/dur)
    # Camera: India -> South India / Tamil Nadu -> Chennai, continuous logarithmic zoom.
    if p<.36:
        u=smooth(p/.36);lon=tween(79.4,79.5,u);lat=tween(23.5,13.4,u);scale=19*math.exp(math.log(43/19)*u)
    elif p<.78:
        u=smooth((p-.36)/.42);lon=tween(79.5,79.75,u);lat=tween(13.4,12.9,u);scale=43*math.exp(math.log(110/43)*u)
    else:
        u=smooth((p-.78)/.22);lon=tween(79.75,80.278053,u);lat=tween(12.9,13.091934,u);scale=110*math.exp(math.log(195/110)*u)
    canvas=new_canvas(w,h)
    ctr=[lon,lat]
    india=project(geos['india'],ctr,scale,w,h)
    cv2.fillPoly(canvas,[india],(77,63,33),cv2.LINE_AA)
    cv2.polylines(canvas,[india],True,(176,142,97),2,cv2.LINE_AA)
    if p>.22:
        for st in ('Karnataka','Kerala','Andhra Pradesh'):
            xy=project(geos[st],ctr,scale,w,h)
            cv2.polylines(canvas,[xy],True,(110,118,71),2,cv2.LINE_AA)
    tn=project(geos['Tamil Nadu'],ctr,scale,w,h)
    overlay=canvas.copy(); cv2.fillPoly(overlay,[tn],(60,122,231),cv2.LINE_AA)
    alpha=tween(.03,.63,(p-.15)/.38)
    cv2.addWeighted(overlay,alpha,canvas,1-alpha,0,canvas)
    if p>.2:
        cv2.polylines(canvas,[tn],True,(95,174,249),4,cv2.LINE_AA)
    # Cities are coordinates from the official Natural Earth populated-places layer.
    cx,cy=project(np.array([[80.278053,13.091934]]),ctr,scale,w,h)[0]
    if p>.48 and -80<cx<w+80 and -80<cy<h+80:
        pulse=1+0.24*math.sin(local*7)
        for r in (20,35):
            layer=canvas.copy();cv2.circle(layer,(int(cx),int(cy)),int(r*pulse),(75,167,252),2,cv2.LINE_AA)
            cv2.addWeighted(layer,.55,canvas,.45,0,canvas)
        cv2.circle(canvas,(int(cx),int(cy)),10,(245,253,255),-1,cv2.LINE_AA)
        cv2.circle(canvas,(int(cx),int(cy)),6,(57,157,244),-1,cv2.LINE_AA)
        lx=max(40,min(w-265,int(cx)+22));ly=max(108,min(h-193,int(cy)-44))
        rounded(canvas,lx-10,ly-3,lx+244,ly+69,9,(15,32,38))
        canvas=add_text_blocks(canvas,[('CHENNAI',(lx,ly+2),26,(255,249,243),True),
                ('Tamil Nadu · India',(lx,ly+36),18,(171,218,222),False)])
    canvas=add_text_blocks(canvas,[('GEO FOCUS  /  SOUTH INDIA',(28,23),16,(168,210,210),True),
      (('INDIA' if p<.25 else ('TAMIL NADU' if p<.65 else 'CHENNAI')),(28,57),42,(255,247,235),True),
      ('City-level marker, not the exact L&T campus',(28,h-144),15,(183,201,199),False)])
    canvas=branded_panel(canvas,p)
    cv2.rectangle(canvas,(0,0),(w-1,h-1),(66,111,116),2,cv2.LINE_AA)
    cv2.line(canvas,(28,113),(w-28,113),(100,94,44),2,cv2.LINE_AA)
    return canvas

def scene_bounds():
    # Work manifest's exact observed combined video: 1245 frames and 6 scene boundaries.
    # Counts reconstructed from verified scene WAV durations + spacing (frame-rounded).
    return [0,202,414,607,783,1045,1245]

def upgrade(base,output,geos,qa_dir=None):
    cv2.setNumThreads(2)
    cap=cv2.VideoCapture(str(base));fps=cap.get(cv2.CAP_PROP_FPS)
    count=round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if count!=1245 or abs(fps-30)>.01:raise ValueError('Expected verified original 1245-frame, 30fps cut')
    W=int(cap.get(3));H=int(cap.get(4))
    if (W,H)!=(1080,1920):raise ValueError('Expected locked 1080x1920 V6')
    args=['ffmpeg','-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24',
           '-video_size','1080x1920','-framerate','30','-i','pipe:0','-i',str(base),
           '-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','veryfast',
           '-crf','23','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(output)]
    proc=subprocess.Popen(args,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    limits=scene_bounds();x0,y0,w,h=77,640,928,626
    saved=[]
    for n in range(count):
        ret,frame=cap.read()
        if not ret:raise RuntimeError(f'Missing frame {n}')
        i=next((i for i in range(6) if limits[i]<=n<limits[i+1]),5)
        local=(n-limits[i])/30;duration=(limits[i+1]-limits[i])/30
        if i==1:
            visual=map_hero(local,duration,geos,w,h)
            # blend near boundaries to retain V6's clean scene dissolve.
            alpha=min(1.,local/.32,(duration-local)/.31)
            if alpha>0:
                section=frame[y0:y0+h,x0:x0+w]
                frame[y0:y0+h,x0:x0+w]=cv2.addWeighted(visual,alpha,section,1-alpha,0)
        else:
            # Gentle genuine 2.5D pan/dolly on all existing CGI evidence panels.
            area=frame[y0:y0+h,x0:x0+w]; p=smooth(local/duration)
            zoom=1.012+.054*p;dx=(-8+15*p) * (1 if i%2==0 else -1);dy=-6+13*p
            m=np.array([[zoom,0, (1-zoom)*w/2 + dx],[0,zoom,(1-zoom)*h/2 + dy]],np.float32)
            moved=cv2.warpAffine(area,m,(w,h),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT_101)
            fade=min(1,local/.25,(duration-local)/.25)
            if fade>0:frame[y0:y0+h,x0:x0+w]=cv2.addWeighted(moved,fade,area,1-fade,0)
        if qa_dir and n in [70,220,265,325,379,478,650,840,1120]:
            qa_dir.mkdir(parents=True,exist_ok=True)
            cv2.imwrite(str(qa_dir/f'frame_{n:04}.jpg'),cv2.resize(frame,(540,960)))
            saved.append(n)
        try:proc.stdin.write(frame.tobytes())
        except BrokenPipeError:raise RuntimeError(f'FFmpeg pipe failed at frame {n}')
        if n%240==0:print(f'frame {n}/{count}',flush=True)
    cap.release();proc.stdin.close();err=proc.stderr.read().decode();returncode=proc.wait()
    if returncode:raise RuntimeError(f'FFmpeg failure: {err[-800:]}')
    print(json.dumps({'input':str(base),'output':str(output),'frames':count,'durationSeconds':count/30,
         'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'qaFrames':saved},indent=2))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--geo',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--qa',type=Path);args=ap.parse_args()
    encoded=json.loads(args.geo.read_text());geos={k:decoded(v) for k,v in encoded.items() if k not in ('source','chennai')}
    # Sanity check accurate Natural Earth shape and Chennai city point.
    tn=geos['Tamil Nadu'];chennai=np.asarray(encoded['chennai']);assert 76<tn[:,0].min()<77 and 8<tn[:,1].min()<9
    assert 80<chennai[0]<81 and 13<chennai[1]<14
    args.out.parent.mkdir(parents=True,exist_ok=True)
    upgrade(args.input,args.out,geos,args.qa)

if __name__=='__main__':main()