#!/usr/bin/python
import unittest
from vehicle import Vehicle

class UtDemo(unittest.TestCase):
    '''A Unit Test Demo'''

    def setUp(self):
        "Create a list of test files"
        self.time_list=['20120912072912','20120913072230',20120912073312]
        for f in self.time_list:
            print f

    def test_int(self):
        self.assertEquals(2,2,'number not equals')
        
    def test_vehicle(self):
        v = Vehicle('Corolla')
        v.display()

if __name__=='__main__': unittest.main()
