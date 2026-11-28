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
   key={1:'ship-camera',2:'map-camera',5:'fleet-camera'}[scene];x,y,w,h=cliprect(root,key);self.assertLessEqual(y+h,1330);self.assertGreaterEqual(x,68);self.assertLessEqual(x+w,1012)
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
  self.assertEqual(r.ship_camera(0),(1,540,920));self.assertEqual(r.ship_camera(3),(1.95,825,990));self.assertEqual(r.ship_camera(6.6),(1.95,255,990));self.assertEqual(r.ship_camera(9),(1,540,920))
  self.assertEqual(r.map_camera(2),(2.35,*r.MUMBAI));self.assertEqual(r.map_camera(4.5),(2.35,*r.KOLKATA));self.assertEqual(r.map_camera(6.8),(1,540,920));self.assertEqual(r.fleet_camera(0)[0],2.95);self.assertEqual(r.fleet_camera(7)[0],1)
 def test_map_source(self):
  self.assertIn('geoBoundaries',r.MAP['source']);self.assertGreater(len(r.MAP['path']),4000)
  for pt,lon,lat in [(r.MUMBAI,72.8777,19.076),(r.KOLKATA,88.3639,22.5726)]:
   self.assertAlmostEqual(pt[0],540+(lon-82)*16.5,4);self.assertAlmostEqual(pt[1],920+(22-lat)*18,4)
if __name__=='__main__':unittest.main()
