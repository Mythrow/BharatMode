"""Native silent review segments from the exact storyboard renderer."""
import ctypes as C, sys, subprocess
import numpy as np
import render_storyboard as r
W,H=1080,1920
lib=C.CDLL('librsvg-2.so.2');ca=C.CDLL('libcairo.so.2');g=C.CDLL('libgobject-2.0.so.0')
P=C.c_void_p; I=C.c_int; D=C.c_double
class Rect(C.Structure):_fields_=[('x',D),('y',D),('width',D),('height',D)]
def sig(lib,n,rest,args):f=getattr(lib,n);f.restype=rest;f.argtypes=args;return f
new=sig(lib,'rsvg_handle_new_from_data',P,[C.c_char_p,C.c_size_t,P]);draw=sig(lib,'rsvg_handle_render_document',I,[P,P,C.POINTER(Rect),P]);unref=sig(g,'g_object_unref',None,[P]);surf=sig(ca,'cairo_image_surface_create_for_data',P,[P,I,I,I,I]);create=sig(ca,'cairo_create',P,[P]);flush=sig(ca,'cairo_surface_flush',None,[P]);destroy=sig(ca,'cairo_destroy',None,[P]);sd=sig(ca,'cairo_surface_destroy',None,[P]);viewport=Rect(0,0,W,H)
def raster(svg):
 b=svg.encode();a=np.zeros((H,W,4),np.uint8);s=surf(a.ctypes.data,0,W,H,W*4);cr=create(s);h=new(b,len(b),None)
 if not h or not draw(h,cr,C.byref(viewport),None):raise RuntimeError('SVG render failed')
 flush(s);unref(h);destroy(cr);sd(s);return a
if __name__=='__main__':
 start,end=map(int,sys.argv[1:3]);out=sys.argv[3]
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgra','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','2','-preset','ultrafast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',out]
 p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for n in range(start,end):
  p.stdin.write(raster(r.frame(n/60)).tobytes())
  if n%120==0:print(n,flush=True)
 p.stdin.close();assert p.wait()==0
