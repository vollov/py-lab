#!/usr/bin/python

import math
from point import Point

class Line:
    '''Line class'''
    
    def __init__(self, start, end):
        '''Initialize Line'''
        self.start=start
        self.end=end

    def distance(self):
        '''Calculate distance between points'''
        return math.sqrt(
            (self.end.x - self.start.x)**2 +
            (self.end.y - self.start.y)**2)

def test():
    pt1 = Point(1,1)
    pt2 = Point(4,5)
    line1 = Line(pt1,pt2)
    
    print line1.distance()

if __name__=='__main__':
    '''python example.py -v'''
    import doctest
    doctest.testmod()
    test()
