from pathlib import Path
import ctypes as C, numpy as np, cv2, subprocess, sys, bisect, math, re, functools
import render_storyboard as r
r.tw=functools.lru_cache(4096)(r.tw)
W,H=1080,1920
cv2.setNumThreads(1)
lib=C.CDLL('librsvg-2.so.2');ca=C.CDLL('libcairo.so.2');g=C.CDLL('libgobject-2.0.so.0')
P=C.c_void_p; I=C.c_int; D=C.c_double
class Rect(C.Structure):_fields_=[('x',D),('y',D),('width',D),('height',D)]
def sig(lib,n,rest,args):f=getattr(lib,n);f.restype=rest;f.argtypes=args;return f
new=sig(lib,'rsvg_handle_new_from_data',P,[C.c_char_p,C.c_size_t,P]);draw=sig(lib,'rsvg_handle_render_document',I,[P,P,C.POINTER(Rect),P]);unref=sig(g,'g_object_unref',None,[P]);surf=sig(ca,'cairo_image_surface_create_for_data',P,[P,I,I,I,I]);create=sig(ca,'cairo_create',P,[P]);flush=sig(ca,'cairo_surface_flush',None,[P]);destroy=sig(ca,'cairo_destroy',None,[P]);sd=sig(ca,'cairo_surface_destroy',None,[P]);viewport=Rect(0,0,W,H)
def raster(s):
 b=s.encode();a=np.zeros((H,W,4),np.uint8);s=surf(a.ctypes.data,0,W,H,W*4);cr=create(s);h=new(b,len(b),None)
 if not h or not draw(h,cr,C.byref(viewport),None):raise RuntimeError('SVG render failed')
 flush(s);unref(h);destroy(cr);sd(s);return a
# Frame function: approved SVG scene, with fixed chrome independent of crossfade; current captions stay stationary.
def parts(t):
 # raw=r.frame(t); # split at top-level markup using stable source functions rather than raster crops
 i=min(5,bisect.bisect_right(r.BOUNDS,t)-1);dt=t-r.BOUNDS[i];theme,kicker,heads,bgid=r.SCENES[i];dark=theme=='midnight';fg=r.IV if dark else r.INK;ac=r.MINT if dark else r.BROWN
 hdr='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
 # Text begins after dissolve. Existing headline/kicker and graphics are preserved.
 a=[r.background(i,t),r.typed(86,312,kicker,26,ac,dt,.36,'kicker',extra='letter-spacing="2.3"')];size=min(91,int(min(900/max(1,r.tw(h,91))*91 for h in heads)))
 for j,h in enumerate(heads):a.append(r.typed(83,438+j*109,h,size,fg,dt,.48+j*.47,f'headline-{j}',800,extra='letter-spacing="-2"'))
 a.append(r.hero(i,dt,t,dark));return hdr+''.join(a)+'</svg>',i,dark
# Provisional captions are fresh transparent layers, grouped by measured width, with 0.2s word pop.
def chrome(t,i,dark):
 hdr='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'; a=[f'<svg x="86" y="89" width="88" height="88" viewBox="0 0 320 320">{r.logo}</svg>',r.rect(730,100,278,65,r.IV if dark else r.DK,33),r.txt(869,142,'HEALTHCARE',25,r.DK if dark else r.IV,500,'middle',extra='letter-spacing="1.4"')]
 words=r.SCRIPTS[i].split();dt=t-r.BOUNDS[i];span=r.BOUNDS[i+1]-r.BOUNDS[i];wpos=max(0,dt/span*len(words));idx=min(len(words)-1,int(wpos));groups=[];gg=[]
 for w in words:
  if gg and (len(gg)>=5 or r.tw(' '.join(gg+[w]),51)>730):groups.append(gg);gg=[]
  gg.append(w)
 if gg:groups.append(gg)
 pos=0
 for gg in groups:
  if idx<pos+len(gg):visible=gg[:idx-pos+1];break
  pos+=len(gg)
 size=min(57,max(42,int(720/max(1,r.tw(' '.join(visible),57))*57))) if r.tw(' '.join(visible),57)>720 else 57
 widths=[r.tw(w,size) for w in visible];gap=14;total=sum(widths)+gap*(len(visible)-1);x=540-total/2;a.append(r.rect(x-24,1437,total+48,112,r.DK,24,op=.30 if dark else .10))
 for j,w in enumerate(visible):
  age=(wpos-idx)*span/len(words);p=r.clip(age/.2);scale=(.6+.52*p/.55 if p<.55 else 1.12-.12*(p-.55)/.45) if j==len(visible)-1 else 1; ink=(r.PEACH if dark else r.BROWN) if j==len(visible)-1 else r.IV if dark else r.INK;cx=x+widths[j]/2
  a.append(r.txt(x,1514,w,size,ink,700,extra=f'transform="translate({cx} 1495) scale({scale}) translate({-cx} -1495)"'));x+=widths[j]+gap
 sw=(912-5*8)/6
 for j in range(6):
  x=84+j*(sw+8);p=r.clip((t-r.BOUNDS[j])/(r.BOUNDS[j+1]-r.BOUNDS[j]));a.append(r.rect(x,1721,sw,13,'#607078' if dark else '#D4C8B7',6.5));a.append(r.rect(x,1721,sw*p,13,r.OR,min(6.5,sw*p/2)))
 return hdr+''.join(a)+'</svg>'
# Composite premultiplied BGRA chrome over opaque scene in strips to avoid whole-frame copies.
def frame(n):
 t=n/60;s,i,dark=parts(t);a=raster(s);dt=t-r.BOUNDS[i]
 if i and dt<.34:
  b=raster(parts(r.BOUNDS[i]-1/60)[0]);p=r.ease(dt/.34);a=cv2.addWeighted(a,p,b,1-p,0)
 c=raster(chrome(t,i,dark));
 for y,Y in [(75,185),(1425,1565),(1715,1740)]:
  sub=c[y:Y];dst=a[y:Y];alpha=sub[:,:,3:4].astype(np.uint16);dst[:,:,:3]=np.minimum(255,sub[:,:,:3].astype(np.uint16)+((dst[:,:,:3].astype(np.uint16)*(255-alpha)+127)//255)).astype(np.uint8)
 return a[:,:,:3].copy()
def main():
 start,end=map(int,sys.argv[1:3]);out=sys.argv[3];cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','1','-preset','veryfast','-crf','17','-profile:v','high','-pix_fmt','yuv420p','-vf','scale=out_color_matrix=bt709','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-movflags','+faststart',out];p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for n in range(start,end):
  p.stdin.write(frame(n).tobytes())
  if n%120==0:print(n,flush=True)
 p.stdin.close();assert p.wait()==0
if __name__=='__main__':main()
