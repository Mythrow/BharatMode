#!/usr/bin/env python3
"""BM-0003 V4: open-canvas motion graphics, no evidence cards. Audio copied from V3.
Main-chat render bridge: retains native V6 titles, captions, logo and progress from
approved base; all story graphics and moving backdrops freshly drawn. Original
schematics, not documentary site footage. No paid services or video work delegation.
"""
import argparse, math, json, subprocess, hashlib
from pathlib import Path
from functools import lru_cache
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H=540,960
BOUNDS=[0,202,414,607,783,1045,1245]
TEAL=(122,215,199); SAFF=(232,117,46); IVORY=(255,247,235); NAVY=(11,16,24)
THEMES=['dark','light','dark','light','dark','saffron']
BASE={'dark':NAVY,'light':(252,243,230),'saffron':(233,130,59)}
F='/usr/share/fonts/truetype/lato/'
cv2.setNumThreads(1)
def sm(x): x=max(0,min(1,x));return x*x*(3-2*x)
def enter(t,delay=0,d=.65):return sm((t-delay)/d)
def mix(a,b,k):return tuple(int(x*(1-k)+y*k) for x,y in zip(a,b))
def bgr(c):return tuple(int(x) for x in c[::-1])
def poly(im,pts,c):cv2.fillPoly(im,[np.round(pts).astype(np.int32)],bgr(c),cv2.LINE_AA)
def line(im,a,b,c,th=1):cv2.line(im,tuple(map(round,a)),tuple(map(round,b)),bgr(c),th,cv2.LINE_AA)
def circ(im,p,r,c,th=-1):cv2.circle(im,tuple(map(round,p)),max(1,round(r)),bgr(c),th,cv2.LINE_AA)
def ink(theme):return IVORY if theme=='dark' else NAVY
def accent(theme):return TEAL if theme=='dark' else (17,122,122)
def rect(im,x,y,w,h,c):poly(im,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],c)
@lru_cache(maxsize=600)
def label_bitmap(s,size,bold,color):
    font=ImageFont.truetype(F+('Lato-Heavy.ttf' if bold else 'Lato-Medium.ttf'),size)
    box=font.getbbox(s); out=Image.new('RGBA',(max(1,box[2]-box[0]+4),max(1,box[3]-box[1]+4)))
    ImageDraw.Draw(out).text((2-box[0],2-box[1]),s,font=font,fill=(*color,255));return np.array(out)[:,:,[2,1,0,3]].copy()
def paste(im,a,x,y,op=1):
    x=int(x);y=int(y);h,w=a.shape[:2];l=max(0,x);r=min(W,x+w);u=max(0,y);v=min(H,y+h)
    if r<=l or v<=u or op<=0:return
    src=a[u-y:v-y,l-x:r-x];dst=im[u:v,l:r];alpha=src[:,:,3:4].astype(np.float32)*(op/255)
    dst[:]=(dst*(1-alpha)+src[:,:,:3]*alpha).astype(np.uint8)
def txt(im,s,x,y,size,c,bold=True,anchor='left',op=1):
    a=label_bitmap(s,size,bold,c)
    if anchor=='center':x-=a.shape[1]/2
    if anchor=='right':x-=a.shape[1]
    paste(im,a,x,y,op)
def load_logo(p,sz):
    a=cv2.imread(str(p),cv2.IMREAD_UNCHANGED)
    if a is None:raise FileNotFoundError(p)
    if a.shape[2]==3:a=cv2.cvtColor(a,cv2.COLOR_BGR2BGRA)
    return cv2.resize(a,(sz,sz),interpolation=cv2.INTER_AREA)
@lru_cache(maxsize=4)
def backdrop(theme):
    base=np.array(bgr(BASE[theme]),np.float32)
    yy,xx=np.mgrid[0:H,0:W]; v=np.exp(-((xx-270)**2/(370**2)+(yy-490)**2/(310**2)))[:,:,None]
    color=np.array(bgr({'dark':(16,44,49),'light':(233,238,224),'saffron':(249,166,87)}[theme]))
    return np.uint8(np.clip(base+(color-base)*v,0,255))
def ambient(im,t,theme,i):
    base=BASE[theme];a=accent(theme);c=mix(base,a,.13 if theme!='dark' else .26)
    # Moving depth contours and small tracers, visible beyond the story hero.
    for k in range(5):
        phase=t*.26+k*.37+i*.32
        p=[]
        for x in range(-20,565,14):
            y=530+74*k+38*math.sin(x/130+phase)+16*math.sin(x/60-phase*.7)
            p.append((x,y))
        cv2.polylines(im,[np.array(p,np.int32)],False,bgr(c),1,cv2.LINE_AA)
    for k in range(23):
        x=(k*89.7+13*t*(1+(k%3)*.5))%560-10;y=305+(k*57.3+9*t*(1+k%2))%520
        r=1+(k%4==0);circ(im,(x,y),r,mix(base,a,.23+.12*(.5+.5*math.sin(t*2+k))))
    # broad moving bands at bottom, no rectangular hero or panel
    for k in range(3):
        cy=900+36*k;cx=270+65*math.sin(t*.38+k*.6)
        cv2.ellipse(im,(round(cx),cy),(315+28*k,100+16*k),-13,0,360,bgr(c),1,cv2.LINE_AA)
def decode(s):
    out=[];xy=[0,0];i=0
    while i<len(s):
        for ax in (0,1):
            value=shift=0
            while True:
                ch=ord(s[i])-63;i+=1;value|=(ch&31)<<shift;shift+=5
                if ch<32:break
            xy[ax]+=~(value>>1) if value&1 else value>>1
        out.append([x/1e4 for x in xy])
    return np.array(out,np.float64)
def draw_racks(im,t,d):
    p=t/d;e=enter(t);vp=np.array([270+25*math.sin(t*.7),455-22*sm(p)])
    # Perspective floor, converging lines and luminous traveling data.
    for k in range(-7,8):line(im,vp,(270+k*105,735),(28,82,89),1)
    for k in range(18):
        z=((k/18+t*.18)%1)**2.6; y=vp[1]+(735-vp[1])*z
        line(im,(0,y),(540,y),(22,56,62),1)
    for side in [-1,1]:
        for k in range(7,-1,-1):
            depth=1/(1+k*.40);scale=depth*(.82+.16*sm(p));h=295*scale;w=76*scale
            e2=enter(t,.07*k,.7);x=vp[0]+side*(46+170*scale+75*(1-e2));y=vp[1]+140*scale-h*.55+22*(1-e2)
            if side<0:x-=w
            dx=side*17*scale;dy=-14*scale
            # Each rack has side face, top and face. Nearest racks move independently.
            poly(im,[(x,y),(x+dx,y+dy),(x+w+dx,y+dy),(x+w,y)],(62,108,112))
            poly(im,[(x+w,y),(x+w+dx,y+dy),(x+w+dx,y+h+dy),(x+w,y+h)],(17,38,43))
            rect(im,x,y,w,h,(22,47,53));line(im,(x,y),(x+w,y),(101,158,155),1);line(im,(x,y),(x,y+h),(65,124,125),1)
            for j in range(9):
                yy=y+7*scale+j*(h-14*scale)/9
                rect(im,x+5*scale,yy,w-10*scale,(h-14*scale)/9-3*scale,(31,67,73))
                circ(im,(x+w-10*scale,yy+4*scale),max(1,2*scale),mix((43,93,96),TEAL,.25+.75*(.5+.5*math.sin(t*4+j+k))))
    for k in range(9):
        z=((t*.45+k/9)%1)**2;pt=vp+(np.array([270+(-1)**k*120,730])-vp)*z
        circ(im,pt,2+z*3,TEAL)
    txt(im,'COMPUTE  /  POWER  /  DATA',270,665,14,TEAL,anchor='center',op=enter(t,.7))
    txt(im,'Illustrative server infrastructure',270,686,12,(143,181,179),False,anchor='center',op=enter(t,1))
def map_scene(im,t,d,geos,logos):
    p=t/d;u=sm(p/.48);v=sm((p-.48)/.52)
    lon=79.2+.55*u+.53*v;lat=23.5-10.0*u-.41*v;scale=11.2*math.exp(math.log(27/11.2)*u+math.log(58/27)*v)
    center=np.array([270+28*v,486-14*v]);theme='light';coast=(49,112,116);land=(186,211,199);orange=(232,117,46)
    def proj(a):return np.column_stack((center[0]+(a[:,0]-lon)*math.cos(math.radians(lat))*scale,center[1]-(a[:,1]-lat)*scale))
    # Entire scene is the map canvas, with water using the same ivory background.
    for k in range(7):
        y=310+k*48+(t*10)%48;line(im,(0,y),(540,y),(220,229,219),1)
    for k in range(12):
        x=k*48-(t*6)%48;line(im,(x,285),(x,686),(220,229,219),1)
    xy=proj(geos['india']);poly(im,xy,land);cv2.polylines(im,[xy.astype(np.int32)],True,bgr(coast),1,cv2.LINE_AA)
    for name in ('Karnataka','Kerala','Andhra Pradesh'):
        a=proj(geos[name]);cv2.polylines(im,[a.astype(np.int32)],True,bgr((132,173,159)),1,cv2.LINE_AA)
    a=proj(geos['Tamil Nadu']);poly(im,a,mix(land,orange,sm((p-.05)/.34)*.92));cv2.polylines(im,[a.astype(np.int32)],True,bgr(mix(coast,(175,83,36),sm(p/.35))),2,cv2.LINE_AA)
    q=proj(np.array([geos['chennai']]))[0];f=enter(t,d*.35,.45)
    if f>.01 and 0<q[0]<540 and 270<q[1]<680:
        for j in range(3):
            r=(5+((t*29+j*15)%42))*f;circ(im,q,r,mix(land,orange,max(.15,1-r/50)),1)
        circ(im,q,7,(255,248,235));circ(im,q,4,(174,60,18))
        x=min(415,max(135,q[0]+23));y=min(560,max(325,q[1]-24));line(im,q,(x-5,y+9),(154,76,37),1)
        txt(im,'Chennai',x,y,25,NAVY,op=f);txt(im,'Tamil Nadu',x,y+28,14,(32,100,103),False,op=f)
    if p<.48:txt(im,'INDIA',38,318,20,NAVY,op=enter(t,.1)*(1-sm((p-.30)/.18)))
    if p>.19 and p<.8:txt(im,'TAMIL NADU',35,330,17,(154,76,37),op=sm((p-.19)/.16)*(1-sm((p-.62)/.18)))
    # Fade geography into the scene's own lower background, keeping identities readable.
    ground=backdrop('light'); yy=np.arange(610,710,dtype=np.float32)
    f=np.clip((yy-610)/77,0,1); f=(f*f*(3-2*f))[:,None,None]
    im[610:710]=np.uint8(im[610:710]*(1-f)+ground[610:710]*f)
    im[710:]=ground[710:]
    # Individual marks enter from alternating directions, without chips/cards.
    for j,(name,xx,icon) in enumerate([('L&T',41,'lt'),('Vyoma.AI',139,None),('LTN Compute',269,None),('NVIDIA',434,'nv')]):
        a=enter(t,.25+j*.21,.7);y=657+24*(1-a);color=NAVY
        if icon:
            paste(im,logos[icon],xx-8,y-2,a);off=28
        else:off=0
        txt(im,name,xx+off,y+2,14 if j==2 else 16,color,op=a)
    txt(im,'B300 GPUs  •  Chennai city marker',270,695,13,(46,94,95),False,anchor='center',op=enter(t,.8))
def money(im,t,d):
    a=enter(t,.05);b=enter(t,.85);c=enter(t,1.5);p=t/d
    txt(im,'L&T  /  LARGE ORDER CLASSIFICATION',270,316,14,TEAL,anchor='center',op=a)
    txt(im,'₹2,500',36-55*(1-a),366,65,IVORY,op=a)
    txt(im,'₹5,000',504+55*(1-b),480,65,IVORY,anchor='right',op=b)
    txt(im,'CRORE',43,438,16,(146,186,186),op=a);txt(im,'CRORE',497,552,16,(146,186,186),anchor='right',op=b)
    # One diagonal range connection grows from the min to max; no misleading actual amount.
    start=np.array([64,488]);end=np.array([476,588]);head=start+(end-start)*c
    line(im,start,end,(39,75,80),3);line(im,start,head,SAFF,6)
    for k in range(13):
        q=start+(end-start)*k/12;line(im,q+np.array([0,-7]),q+np.array([0,7]),(109,147,145),1)
    circ(im,start,6,TEAL);circ(im,head,7,SAFF)
    for k in range(5):
        q=start+(end-start)*((t*.30+k/5)%1)*c;circ(im,q,3,IVORY)
    txt(im,'ORDER-VALUE RANGE',270,622,17,TEAL,anchor='center',op=c)
    txt(im,'Exact contract amount undisclosed',270,651,15,(172,195,193),False,anchor='center',op=c)
def capacity(im,t,d):
    a=enter(t,.05);b=enter(t,.35);p=t/d
    txt(im,'10,000',270,310-24*(1-a),83,NAVY,anchor='center',op=a)
    txt(im,'GPU  /  PLANNED CLUSTER',270,402,16,(17,122,122),anchor='center',op=b)
    # 100 outlined GPU modules arrive in waves; one tile represents 100 planned GPUs.
    for r in range(10):
        for c in range(10):
            e=enter(t,.3+(r+c)*.085,.48);x=62+c*43+(r-4.5)*2.8+9*math.sin(t*.7);y=450+r*17-4*c+38*(1-e)
            if e<.01:continue
            col=mix((220,229,220),(17,122,122),.3+.7*e)
            poly(im,[(x,y),(x+33,y-3),(x+39,y+9),(x+6,y+12)],mix(col,(105,175,162),.35))
            poly(im,[(x+6,y+12),(x+39,y+9),(x+39,y+15),(x+6,y+18)],col)
            line(im,(x+6,y+3),(x+26,y+1),(237,247,230),1)
    txt(im,'1 tile = 100 planned GPUs',270,641,13,(38,106,109),False,anchor='center',op=enter(t,.8))
    txt(im,'ANNOUNCED AUGUST 2026  •  NOT LIVE COUNT',270,666,13,(154,76,37),anchor='center',op=enter(t,1.1))
def comparison(im,t,d):
    a=enter(t);b=enter(t,.6);c=enter(t,1.2);p=t/d
    cx=270;cy=426
    # GPU chip enters; wires grow toward separate workloads.
    chip=84*a
    for k in range(7):
        ofs=(k-3)*10*a
        line(im,(cx-chip/2-9,cy+ofs),(cx-chip/2,cy+ofs),TEAL,2);line(im,(cx+chip/2,cy+ofs),(cx+chip/2+9,cy+ofs),TEAL,2)
    rect(im,cx-chip/2,cy-chip/2,chip,chip,(25,73,77));rect(im,cx-chip*.31,cy-chip*.31,chip*.62,chip*.62,(44,117,116))
    txt(im,'GPU',cx,cy-11,20,IVORY,anchor='center',op=a)
    for s,label in [(-1,'TRAIN'),(1,'INFERENCE')]:
        end=np.array([cx+s*176,488]);st=np.array([cx+s*54,cy]);head=st+(end-st)*b;line(im,st,head,TEAL,2)
        for j in range(3):q=st+(head-st)*((t*.6+j/3)%1);circ(im,q,3,SAFF)
        circ(im,end,24*b,(20,49,53));circ(im,end,24*b,TEAL,1)
        if s<0:
            for j in range(3):line(im,end+[-11,j*7-7],end+[11,j*7-7],TEAL,2)
        else:poly(im,[end+[-7,-12],end+[12,0],end+[-7,12]],TEAL)
        txt(im,label,end[0],525,14,IVORY,anchor='center',op=b)
    # Distinct elements slide apart, no comparison boxes.
    txt(im,'10,000',48-35*(1-c),581,46,TEAL,op=c);txt(im,'PLANNED',52,633,15,(148,204,195),op=c)
    txt(im,'?',492+35*(1-c),574,62,SAFF,anchor='right',op=c);txt(im,'RUNNING COUNT',492,637,14,(255,190,145),anchor='right',op=c)
    txt(im,'NOT CONFIRMED',492,657,13,(177,190,189),anchor='right',op=c)
    line(im,(270,576),(270,669),(42,83,86),1)
def finale(im,t,d):
    a=enter(t);p=t/d;cx=270+10*math.sin(t*.75);cy=491;inkc=(23,43,46);tealc=(17,100,100)
    # Open radiating circuits; a push-out reveals the network.
    radius=124+28*sm(p)
    for k in range(3):
        r=(radius+38*k)*a;cv2.ellipse(im,(round(cx),cy),(max(1,round(r)),max(1,round(r*.62))),-14,0,360,bgr((191,111,54)),1,cv2.LINE_AA)
    nodes=[('RESEARCH',-2.55),('AI',-1.57),('INDUSTRY',-.48),('SCIENCE',.55),('COMPUTE',2.6)]
    for i,(lab,ang) in enumerate(nodes):
        e=enter(t,.22+i*.22,.7);ang+=.12*math.sin(t*.5);q=np.array([cx+radius*math.cos(ang),cy+radius*.73*math.sin(ang)]);st=np.array([cx,cy]);end=st+(q-st)*e
        line(im,st,end,tealc,2);circ(im,end,9*e,tealc);circ(im,end,5*e,IVORY)
        for j in range(2):z=(t*.45+j/2+i*.11)%1;circ(im,st+(end-st)*z,3,IVORY)
        txt(im,lab,q[0],q[1]+14,13,inkc,anchor='center',op=e)
    size=93*a;rect(im,cx-size/2,cy-size/2,size,size,inkc);rect(im,cx-size*.32,cy-size*.32,size*.64,size*.64,tealc)
    for k in range(7):
        of=(k-3)*10*a
        line(im,(cx-size/2-9,cy+of),(cx-size/2,cy+of),inkc,2);line(im,(cx+size/2,cy+of),(cx+size/2+9,cy+of),inkc,2)
        line(im,(cx+of,cy-size/2-9),(cx+of,cy-size/2),inkc,2);line(im,(cx+of,cy+size/2),(cx+of,cy+size/2+9),inkc,2)
    circ(im,(cx,cy),12*a,IVORY,2);circ(im,(cx,cy),4*a,IVORY)
    txt(im,'INFRASTRUCTURE FOR WHAT COMES NEXT',270,680,14,inkc,anchor='center',op=enter(t,.9))
def scene(i,t,geo,logos):
    theme=THEMES[i];d=(BOUNDS[i+1]-BOUNDS[i])/30
    im=backdrop(theme).copy();ambient(im,t,theme,i)
    if i==0:draw_racks(im,t,d)
    elif i==1:map_scene(im,t,d,geo,logos)
    elif i==2:money(im,t,d)
    elif i==3:capacity(im,t,d)
    elif i==4:comparison(im,t,d)
    else:finale(im,t,d)
    return im
# Preserve exact native V6 source title, captions, logo and progress. Feather around
# the old chrome; the open scene is full-width, with no rectangular card boundary.
def preservation_mask():
    yy,xx=np.mgrid[0:1920,0:1080].astype(np.float32);yy/=2;xx/=2
    def ramp(a,b,x):z=np.clip((x-a)/(b-a),0,1);return z*z*(3-2*z)
    top=1-ramp(278,321,yy)
    # retain only the caption/chapter regions, feather the edges to the new backdrop
    bar=ramp(824,828,yy)*(1-ramp(837,841,yy))*ramp(37,40,xx)*(1-ramp(500,504,xx))
    return np.maximum(top,bar)[:,:,None].astype(np.float32)
def preserve_caption(out,base):
    # Identify the actual visible word group. Preserve its compact backing ONLY,
    # rather than carrying the whole rectangular old background strip forward.
    # Work at native resolution; thresholds detect high-contrast original caption ink.
    region=base[1440:1540,60:1020];g=cv2.cvtColor(region,cv2.COLOR_BGR2GRAY)
    corner=base[50,50];dark=corner.mean()<90;saffron=int(corner[2])-int(corner[0])>75
    if dark: binary=g>120
    elif saffron: binary=g>170
    else: binary=g<145
    binary=binary.astype(np.uint8)*255
    n,_,stats,_=cv2.connectedComponentsWithStats(binary,8)
    good=[(x,y,w,h) for x,y,w,h,area in stats[1:] if 3<=w<=320 and 6<=h<=93 and area>=12]
    if not good:return
    x0=max(0,min(v[0] for v in good)+60-35);x1=min(1080,max(v[0]+v[2] for v in good)+60+35)
    y0=1408;y1=1570
    if x1-x0<25:return
    yy,xx=np.mgrid[y0:y1,x0:x1].astype(np.float32)
    def rr(a,b,v):z=np.clip((v-a)/(b-a),0,1);return z*z*(3-2*z)
    mask=(rr(x0,x0+15,xx)*(1-rr(x1-15,x1,xx))*rr(y0,y0+22,yy)*(1-rr(y1-22,y1,yy)))[:,:,None]
    out[y0:y1,x0:x1]=np.uint8(base[y0:y1,x0:x1]*mask+out[y0:y1,x0:x1]*(1-mask))

def get_geos(path):
    js=json.loads(path.read_text());return {k:decode(v) if k!='chennai' else np.array(v) for k,v in js.items() if k!='source'}
def render(args):
    geo=get_geos(args.geo);logos={'lt':load_logo(args.lt,23),'nv':load_logo(args.nv,23)}
    mask=preservation_mask();inv=1-mask
    cap=cv2.VideoCapture(str(args.input));cap.set(cv2.CAP_PROP_N_THREADS,2) if hasattr(cv2,'CAP_PROP_N_THREADS') else None
    if round(cap.get(cv2.CAP_PROP_FRAME_COUNT))!=1245 or abs(cap.get(cv2.CAP_PROP_FPS)-30)>.01:raise ValueError('Unexpected base timeline')
    cmd=['ffmpeg','-y','-v','error','-threads','2','-f','rawvideo','-pixel_format','bgr24','-video_size','1080x1920','-framerate','30','-i','-','-i',str(args.input),'-map','0:v:0','-map','1:a:0','-c:v','libx264','-threads','3','-preset','ultrafast','-crf','19','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(args.out)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE) if not args.stills else None
    qa=args.qa;qa.mkdir(parents=True,exist_ok=True)
    sample=[95,224,292,373,510,685,910,1140]
    indices=sample if args.stills else range(1245)
    for n in indices:
        if args.stills:cap.set(cv2.CAP_PROP_POS_FRAMES,n)
        ok,base=cap.read()
        if not ok:raise RuntimeError(f'Missing frame {n}')
        i=int(np.searchsorted(BOUNDS,n,side='right')-1);t=(n-BOUNDS[i])/30
        art=scene(i,t,geo,logos)
        # Clean 0.34-second soft dissolve of independent moving scenes.
        if i>0 and t<.34:
            old=scene(i-1,(BOUNDS[i]-BOUNDS[i-1])/30+t,geo,logos);alpha=sm(t/.34)
            old=cv2.warpAffine(old,np.float32([[1,0,-6*alpha],[0,1,0]]),(W,H),borderMode=cv2.BORDER_REFLECT_101)
            art=cv2.warpAffine(art,np.float32([[1,0,9*(1-alpha)],[0,1,0]]),(W,H),borderMode=cv2.BORDER_REFLECT_101)
            art=cv2.addWeighted(old,1-alpha,art,alpha,0)
        hero=cv2.resize(art,(1080,1920),interpolation=cv2.INTER_LINEAR)
        # Native text and original audio remain unchanged. Blend region-wise for speed.
        out=hero.copy()
        for y0,y1 in [(0,644),(1646,1684)]:
            m=mask[y0:y1];out[y0:y1]=np.uint8(base[y0:y1]*m+hero[y0:y1]*inv[y0:y1])
        preserve_caption(out,base)
        if n in sample:cv2.imwrite(str(qa/f'frame_{n:04}.jpg'),cv2.resize(out,(540,960)),[cv2.IMWRITE_JPEG_QUALITY,91])
        if proc:proc.stdin.write(out.tobytes())
        if n%200==0:print('frame',n,flush=True)
    cap.release()
    if proc:
        proc.stdin.close();err=proc.stderr.read();rc=proc.wait()
        if rc:raise RuntimeError(err.decode())
        print(json.dumps({'frames':1245,'duration':41.5,'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest()}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--geo',type=Path,required=True);p.add_argument('--lt',type=Path,required=True);p.add_argument('--nv',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--qa',type=Path,required=True);p.add_argument('--stills',action='store_true');render(p.parse_args())