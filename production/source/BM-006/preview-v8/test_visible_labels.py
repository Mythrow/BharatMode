import unittest,re,xml.etree.ElementTree as ET
import preview as p
import render_storyboard as r
class TestViewerText(unittest.TestCase):
 def test_reject_internal_even_when_partially_typed(self):
  for s in ('Illustrative pronunciation','reference text','source note','QA note','placeholder','internal note','helper text','storyboard only'):
   with self.assertRaises(ValueError):r.typed(0,0,s,30,r.INK,0,0,'test')
 def test_keep_factual_qualifiers(self):
  self.assertEqual(r.viewer_text('Potential applications'),'Potential applications')
  self.assertEqual(r.viewer_text('Up to 60% fewer tokens · reported'),'Up to 60% fewer tokens · reported')
 def test_all_storyboard_and_acoustic_svg_states(self):
  for i,d in enumerate(p.D):
   for j in range(int(d*5)+1):
    dt=j/5;svg=p.full_svg(i,dt,r.BOUNDS[i]+dt)
    root=ET.fromstring(svg)
    for e in root.iter('{http://www.w3.org/2000/svg}text'):
     r.viewer_text(e.text or '')
 def test_scene_4_clearance(self):
  # Include complete pin extents, chip reveal drift and text ascent.
  self.assertGreaterEqual(910-38-(735+80+24+15),18)
  self.assertGreaterEqual(1325-53-(1140+82+24+12),14)
 def test_scene_6_clearance(self):
  # The label begins 0.985 seconds after the chip (0.65 second entrance).
  self.assertGreaterEqual(r.CUE_MAP[5]["core-label"]-r.CUE_MAP[5]["core"],.65)
  self.assertGreaterEqual(940-40-(765+80+24),30)
  self.assertGreaterEqual(1345-29-(1279-18+12),40)
if __name__=='__main__':unittest.main()
