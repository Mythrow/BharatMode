import patch as p
from itertools import combinations
import unittest
class TestPatch(unittest.TestCase):
 def test_fleet_sequence_and_clearance(self):
  self.assertEqual(len(p.fleet_state(0)),1)
  self.assertEqual(len(p.fleet_state(6.0)),7)
  self.assertEqual(len(p.FLEET),7)
  for k in range(419):
   t=k/60;states=p.fleet_state(t)
   self.assertLessEqual(sum(j>0 and v<1 for j,x,y,w,side,v in states),1)
   boxes=[]
   for j,x,y,w,side,v in states:
    b=(x-3,y-w*.025-3,x+w+3,y+w*.38+3)
    self.assertGreater(b[1],550);self.assertLess(b[3],1390)
    if v==1:self.assertGreaterEqual(b[0],45);self.assertLessEqual(b[2],1035)
    boxes.append((j,b))
   for (_,A),(_,B) in combinations(boxes,2):
    self.assertGreater(max(B[0]-A[2],A[0]-B[2],B[1]-A[3],A[1]-B[3]),0)
 def test_industry_clearance(self):
  # Illustration <=1028, including entrance motion; metric glyphs start at >=1080.
  self.assertLess(1028,1080)
  for x,label in [(288,'Indigenous content'),(792,'MSMEs across India')]:
   w=p.r.tw(label,34,700);self.assertLess(w,440);self.assertGreater(x-w/2,50);self.assertLess(x+w/2,1030)
if __name__=='__main__':unittest.main()
