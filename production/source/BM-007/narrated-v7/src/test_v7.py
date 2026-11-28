import unittest,xml.etree.ElementTree as ET
from shapely.geometry import box
import build_v5 as v
from test_v5 import texts,NS
import render_storyboard as r
class Revised(unittest.TestCase):
 def test_map_hold(self):
  # At least 0.65 s at full opacity after both labels and headline have settled.
  count=0
  for k in range(1023,1388):
   t=k/60;i,dt,bg,op=v.state(t)
   if i!=2:continue
   local=v.n.vt(i,dt);root=ET.fromstring(v.frame_svg(k));g=next(e for e in root.iter() if e.get('id')=='scene-content')
   if local>=7 and dt<=v.D[2]-v.WIPE:
    self.assertEqual(r.map_camera(local),(1.08,540,920));self.assertTrue(all(r.map_label_state(j,local)[2]>.999 for j in range(2)));self.assertEqual(float(g.get('opacity')),1);self.assertEqual(bg,r.IV);count+=1
  self.assertGreaterEqual(count,39);print('Map fully settled frames:',count,'seconds:',count/60)
 def test_icons(self):
  self.assertGreater(v.ICON_START,2.13);self.assertLessEqual(v.ICON_ENTRY,v.ICON_STEP)
  for k in range(1925,2434):
   t=k/60;i,dt,bg,op=v.state(t)
   if i!=4:continue
   root=ET.fromstring(v.frame_svg(k));units=[e for e in root.iter() if (e.get('id') or '').startswith('msme-unit-')]
   for e in units:
    j=int(e.get('id').split('-')[-1]);x=592+j%8*54;y=(1072,1125,1324)[j//8];b=box(x,y,x+37,y+44)
    self.assertGreater(y,1028);self.assertLess(x+37,1030)
    for text,tb in texts(root):self.assertLessEqual(b.intersection(tb).area,.1,(k,j,text,b.bounds,tb.bounds))
   if dt>=v.ICON_START+23*v.ICON_STEP+v.ICON_ENTRY:self.assertEqual(len(units),24)
if __name__=='__main__':unittest.main()
