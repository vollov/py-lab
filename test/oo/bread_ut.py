# -*- coding: utf-8 -*-
import unittest

from oo.bread import Bread
from utils.test_config import configuration

class BreadUt(unittest.TestCase):
    '''Bread Unit Test'''

    def test_config(self):
        b = Bread('test bread', configuration)
#         print "c.config = ", b.config.getCollection('car', 'parts')
        expected = ['t1', 't2', 't3']
        actual = b.config.getCollection('car', 'parts')
        self.assertEqual(actual,expected,'config not match')