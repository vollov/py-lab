#!/usr/bin/python
import unittest

from oo.line import Line
from oo.point import Point

class LineUt(unittest.TestCase):
    '''Line Unit Test'''

    def setUp(self):
        "Create test points"
        start=Point(1,1)
        end=Point(4,5)
        self.line=Line(start,end)        

    def test_distance(self):
        self.assertEqual(5,self.line.distance(),'distance shoud be 5')
        
    def test_in_list(self):
        x = ['aa','xx','yy']
        if 'xx' in x:
            print 'ok in!'

if __name__=='__main__': unittest.main()
