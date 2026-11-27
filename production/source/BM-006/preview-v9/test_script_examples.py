import unittest,xml.etree.ElementTree as ET
import preview as p
import render_storyboard as r
class ScriptExamples(unittest.TestCase):
 def test_exact_documented_examples_and_hold(self):
  expected={'Devanagari','Bengali-Assamese','Gurmukhi','Gujarati','Odia','Tamil','Telugu','Kannada','Malayalam','Meitei Mayek'}
  observed=set()
  for n in range(596):
   root=ET.fromstring('<svg>'+r.hero(2,n/60,n/60,False)+'</svg>')
   names={e.text for e in root.iter('text')}
   self.assertFalse({'Ol Chiki','Warang Citi'}&names)
   observed|=expected&names
   self.assertLessEqual(len(expected&names),4)
   if n>=310:self.assertEqual(expected&names,{'Malayalam','Meitei Mayek'})
  self.assertEqual(observed,expected)
