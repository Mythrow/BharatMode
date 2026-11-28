"""Regression checks on EVERY provisional frame; geometric isolation, not just XML validity."""
import math, re, unittest, xml.etree.ElementTree as ET
import render_storyboard as r
NS={'s':'http://www.w3.org/2000/svg'}
def byid(root,id):return next((e for e in root.iter() if e.get('id')==id),None)
def cliprect(root,id):
 e=byid(root,id+'-clip').find('s:rect',NS)
 return [float(e.get(k)) for k in ('x','y','width','height')]
def bounds_text(e):
 # conservative full font height with ascent/descent, including current transform offsets for text groups.
 s=e.text or '';size=float(e.get('font-size'));x=float(e.get('x'));y=float(e.get('y'));w=r.tw(s,size,int(e.get('font-weight','700')))
 if e.get('text-anchor')=='middle':x-=w/2
 if e.get('text-anchor')=='end':x-=w
 return (x,y-size,x+w,y+size*.25)
class CameraTests(unittest.TestCase):
 def test_all_states(self):
  n=0
  for f in range(3300):
   t=f/60;root=ET.fromstring(r.frame(t));ids=[e.get('id') for e in root.iter() if e.get('id')];self.assertEqual(len(ids),len(set(ids)));n+=1
   scene=1 if 8<=t<20 else 2 if 20<=t<27 else 5 if t>=47 else None
   if scene is None:continue
   if scene==2:
    camera=byid(root,'map-camera');self.assertIsNotNone(camera);self.assertIsNone(byid(root,'map-camera-clip'))
    self.assertFalse(any(e.get('clip-path') for e in camera.iter()))
    if .65<=t-20<=6.55:self.assertAlmostEqual(float(byid(root,'editorial-heading').get('opacity')),0)
    for j in range(2):
     sx,sy,op,b=r.map_label_state(j,t-20); label=byid(camera,f'geo-label{j}')
     if op<=0:self.assertIsNone(label);continue
     self.assertIsNotNone(label);self.assertGreaterEqual(b[0],50);self.assertLessEqual(b[2],1030);self.assertGreaterEqual(b[1],360);self.assertLessEqual(b[3],1315)
     self.assertGreater(abs(sx-(b[2] if j==0 else b[0])),29)
     self.assertTrue(label.get('transform').startswith('translate('));self.assertIsNotNone(byid(camera,f'geo-pin{j}'))
    continue
   key={1:'ship-camera',5:'fleet-camera'}[scene];x,y,w,h=cliprect(root,key);self.assertLessEqual(y+h,1330);self.assertGreaterEqual(x,68);self.assertLessEqual(x+w,1012)
   head=byid(root,'editorial-heading');op=float(head.get('opacity'))
   # conservative headline lower extent (last baseline 547, size <=91 + descenders).
   if y<575:self.assertEqual(op,0)
   # all camera artwork is isolated in dedicated clipping group, never text.
   self.assertFalse(list(byid(root,key).iter('{http://www.w3.org/2000/svg}text')))
   # only inspect visible text inside these explicitly managed labels; clip can never reach them.
   keys={1:['length','length-label','weight','weight-label'],2:['yard0','city0','yard1','city1','count0','count1'],5:['close']}[scene]
   for k in keys:
    e=byid(root,k)
    if e is None or float(e.get('opacity','1'))<=0:continue
    for tx in e.iter('{http://www.w3.org/2000/svg}text'):
     if not tx.text:continue
     b=bounds_text(tx);self.assertGreaterEqual(b[1],y+h+8,(t,k,b,y+h));self.assertLess(b[3],1495,(t,k,b))
   if scene==5:
    z,fx,fy=r.fleet_camera(t-47)
    world=[(410,925,260),(236,715,260),(584,715,260),(95,925,260),(725,925,260),(236,1135,260),(584,1135,260)]
    for j,(sx,sy,sw) in enumerate(world):
     e=byid(root,f'formation-{j}');
     if float(e.get('opacity'))<=0:continue
     self.assertGreaterEqual(540+(sx-3-fx)*z,68-1e-6)
     self.assertLessEqual(540+(sx+sw+3-fx)*z,1012+1e-6)
     self.assertGreaterEqual(970+(sy-20*sw/800-4-fy)*z,610-1e-6)
     self.assertLessEqual(970+(sy+276*sw/800+4-fy)*z,1330+1e-6)
  self.assertEqual(n,3300)
 def test_camera_keyframes(self):
  self.assertEqual(r.ship_camera(0),(1,540,920));self.assertEqual(r.ship_camera(3),(1.95,255,990));self.assertEqual(r.ship_camera(6.6),(1.95,825,990));self.assertEqual(r.ship_camera(9),(1,540,920))
  self.assertEqual(r.map_camera(2),(2.35,*r.MUMBAI));self.assertEqual(r.map_camera(4.5),(2.35,*r.KOLKATA));self.assertEqual(r.map_camera(6.8),(1.08,540,920));self.assertEqual(r.fleet_camera(0)[0],2.95);self.assertEqual(r.fleet_camera(7)[0],1)
 def test_ruler_direction_and_label_final(self):
  for i in range(180,396):self.assertLessEqual(r.ship_camera(i/60)[1],r.ship_camera((i+1)/60)[1])
  for j in range(2):self.assertAlmostEqual(r.map_label_state(j,6.75)[2],1)
  for dt,j in [(2.65,0),(5.35,1)]:
   sx,sy,op,b=r.map_label_state(j,dt);self.assertAlmostEqual(sx,540);self.assertAlmostEqual(sy,920);self.assertEqual(op,1)
 def test_map_callout_clearance(self):
  from shapely.geometry import box, LineString, Point
  min_clear=999
  for f in range(420):
   t=f/60;z,fx,fy=r.map_camera(t);root=ET.fromstring(r.frame(20+t));visible=[]
   for j in range(2):
    sx,sy,op,b=r.map_label_state(j,t)
    if not op:continue
    l,top,rt,bt=b;wbox=box(fx+(l-540)/z,fy+(top-920)/z,fx+(rt-540)/z,fy+(bt-920)/z)
    clearance=r.LAND.distance(wbox)*z-2*z;min_clear=min(min_clear,clearance)
    self.assertGreaterEqual(clearance,12,(f,j,clearance))
    leader=LineString(r.leader_points(j,b,sx,sy));self.assertGreaterEqual(leader.distance(box(*b)),11.9)
    self.assertGreaterEqual(leader.distance(Point(sx,sy)),10.9)
    g=byid(root,f'geo-label{j}');glyphs=[]
    for e in g.iter('{http://www.w3.org/2000/svg}text'):
     font=r.ImageFont.truetype(r.FONTS+('Inter-Bold.otf' if int(e.get('font-weight'))>=700 else 'Inter-Medium.otf'),int(e.get('font-size')))
     a,b0,c,d=font.getbbox(e.text or '',anchor='ls');x=sx+float(e.get('x'));y=sy+float(e.get('y'));bb=box(x+a,y+b0,x+c,y+d)
     self.assertTrue(box(l-2,top-2,rt+2,bt+2).covers(bb),(f,j,e.text,bb.bounds))
     self.assertGreaterEqual(leader.distance(bb),8)
     for prev in glyphs:self.assertGreaterEqual(bb.distance(prev),2,(f,j,e.text))
     glyphs.append(bb)
    visible.append((box(l,top,rt,bt),leader))
   if len(visible)==2:
    (a,la),(b,lb)=visible;self.assertGreaterEqual(a.distance(b),12);self.assertGreaterEqual(la.distance(b),8);self.assertGreaterEqual(lb.distance(a),8)
  print(f'Minimum map-to-callout clearance across visible states: {min_clear:.2f}px')
 def test_map_source(self):
  self.assertIn('geoBoundaries',r.MAP['source']);self.assertGreater(len(r.MAP['path']),4000)
  for pt,lon,lat in [(r.MUMBAI,72.8777,19.076),(r.KOLKATA,88.3639,22.5726)]:
   self.assertAlmostEqual(pt[0],540+(lon-82)*16.5,4);self.assertAlmostEqual(pt[1],920+(22-lat)*18,4)
if __name__=='__main__':unittest.main()
