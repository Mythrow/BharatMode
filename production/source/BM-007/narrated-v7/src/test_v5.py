import build_v5 as v
import render_storyboard as r
import numpy as np, re, unittest, xml.etree.ElementTree as ET
from itertools import combinations
from PIL import ImageFont
from functools import lru_cache
from shapely.geometry import box,LineString
NS='{http://www.w3.org/2000/svg}'
@lru_cache(maxsize=128)
def font(size,weight):return ImageFont.truetype(r.FONTS+('Inter-Bold.otf' if weight>=700 else 'Inter-Medium.otf'),size)
def mat(s):
 m=np.eye(3)
 for typ,args in re.findall(r'(translate|scale|matrix)\(([^)]*)\)',s or ''):
  a=list(map(float,re.findall(r'-?[\d.]+(?:e[-+]?\d+)?',args)));q=np.eye(3)
  if typ=='translate':q[0,2]=a[0];q[1,2]=a[1] if len(a)>1 else 0
  elif typ=='scale':q[0,0]=a[0];q[1,1]=a[1] if len(a)>1 else a[0]
  else:q=np.array([[a[0],a[2],a[4]],[a[1],a[3],a[5]],[0,0,1]])
  m=m@q
 return m

def texts(root):
 out=[]
 def walk(e,m,op):
  op*=float(e.get('opacity','1'))
  if op<=.015:return
  if e.tag==NS+'defs':return
  m=m@mat(e.get('transform'))
  if e.tag==NS+'text' and e.text:
   x=float(e.get('x',0));y=float(e.get('y',0));size=int(float(e.get('font-size',40)));weight=int(e.get('font-weight','700'));f=font(size,weight)
   l,t,rr,b=f.getbbox(e.text,anchor='ls');w=f.getlength(e.text);spacing=float(e.get('letter-spacing','0'));rr+=max(0,spacing)*(len(e.text)-1);w+=spacing*(len(e.text)-1)
   if e.get('text-anchor')=='middle':x-=w/2
   elif e.get('text-anchor')=='end':x-=w
   pts=[m@np.array([x+a,y+c,1]) for a in (l,rr) for c in (t,b)]
   out.append((e.text,box(min(k[0] for k in pts),min(k[1] for k in pts),max(k[0] for k in pts),max(k[1] for k in pts))))
  for ch in e:walk(ch,m,op)
 walk(root,np.eye(3),1)
 return out

class Preview(unittest.TestCase):
 def test_all_frames(self):
  min_gap=999;min_caption=999;map_n=0;transition_n=0;max_cap=0
  for k in range(v.N):
   t=min(k/60,v.END-1/60);i,dt,bg,op=v.state(t);root=ET.fromstring(v.frame_svg(k));ids=[e.get('id') for e in root.iter() if e.get('id')]
   self.assertEqual(len(ids),len(set(ids)),k)
   self.assertEqual(sum(x=='scene-content' for x in ids),1);self.assertEqual(sum(x=='fixed-foreground' for x in ids),1)
   if op<.999:transition_n+=1
   for (a,A),(b,B) in combinations(texts(root),2):
    self.assertLessEqual(A.intersection(B).area,.1,(k,i,a,b,A.bounds,B.bounds))
   caps=v.cap_layout(i,dt,t)
   if caps:
    left=caps[0][1]-caps[0][3]/2;right=caps[-1][1]+caps[-1][3]/2;max_cap=max(max_cap,right-left+48);self.assertGreater(left-24,70);self.assertLess(right+24,1010)
    for a,b in zip(caps,caps[1:]):min_caption=min(min_caption,b[1]-b[3]/2-a[1]-a[3]/2)
   if i==2:
    map_n+=1;local=v.n.vt(i,dt);z,fx,fy=r.map_camera(local)
    for j in range(2):
     x,y,p,b=r.map_label_state(j,local)
     if p<=0:continue
     l,top,rr,bt=b;world=box(fx+(l-540)/z,fy+(top-920)/z,fx+(rr-540)/z,fy+(bt-920)/z);gap=r.LAND.distance(world)*z-2*z;min_gap=min(min_gap,gap);self.assertGreaterEqual(gap,12)
     self.assertGreaterEqual(LineString(r.leader_points(j,b,x,y)).distance(box(*b)),11.9)
   if i==4:
    self.assertGreater(1070-11.5,1028) # ring top vs illustration animated bounds
    for label,x in [('Indigenous content',288),('MSMEs across India',792)]:
     w=r.tw(label,34);self.assertLess(w,440);self.assertGreater(x-w/2,50);self.assertLess(x+w/2,1030)
    self.assertLess(1220+150+11.5,1440-34);self.assertLess(1440+34*.25,1575)
  print('Frame states:',v.N,'transition states:',transition_n,'map states:',map_n,'map clearance:',min_gap,'caption nominal gap:',min_caption,'max caption backing:',max_cap)
 def test_gauge(self):
  s=v.industry(8,40);self.assertIn('75%',s);self.assertIn('200+',s);self.assertIn('A150 150 0 1 1 138.000 1220.000',s);self.assertNotIn('rect x="80"',s)
if __name__=='__main__':unittest.main()
