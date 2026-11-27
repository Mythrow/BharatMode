import unittest
from unittest.mock import patch
import preview as p
import render_storyboard as r
from PIL import ImageFont

class ConnectorClearance(unittest.TestCase):
 def test_router_and_script_connectors(self):
  original=r.drawlink
  for i in (1,2):
   for n in range(round(p.D[i]*60)):
    dt=n/60; links=[]
    def capture(x,y,X,Y,v,c,w=4):
     if v>0: links.append((x,y,x+(X-x)*r.clip(v),y+(Y-y)*r.clip(v),w))
     return original(x,y,X,Y,v,c,w)
    with patch.object(r,'drawlink',capture):
     r.hero(i,dt,dt,False)
    if i==1:
     # Router label sits beside the chip and above all branching lines.
     for x,y,X,Y,w in links: self.assertGreater(min(y,Y)-w/2,1000)
    else:
     # All card-to-hub paths begin at least 32px below the animated label baseline.
     for x,y,X,Y,w in links: self.assertGreaterEqual(min(y,Y)-w/2,970)
     # Glyph names fit inside independent 260px slots, not touching adjacent cards.
     for name in ('Devanagari','Bengali-Assamese','Gurmukhi','Gujarati','Odia','Tamil','Telugu','Kannada','Malayalam','Meitei Mayek'):
      self.assertLess(r.tw(name,24,600),220)
if __name__=='__main__': unittest.main()
