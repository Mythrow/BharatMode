import unittest,xml.etree.ElementTree as ET
import preview as p

class TestOpeningHero(unittest.TestCase):
 def test_visible_immediate_directional_entrance(self):
  states=[]
  for t in (0,.1,.2,.3,.48,1.):
   el=next(e for e in ET.fromstring(p.full_svg(0,t,t)).iter() if e.attrib.get('id')=='processor')
   states.append((float(el.attrib['opacity']),float(el.attrib['transform'].split()[1].rstrip(')'))))
  self.assertEqual(states[0],(.22,48.))
  for a,b in zip(states[:4],states[1:5]):
   self.assertLess(a[0],b[0]);self.assertGreater(a[1],b[1])
  self.assertEqual(states[4:],[(1.,0.),(1.,0.)])
if __name__=='__main__':unittest.main()
