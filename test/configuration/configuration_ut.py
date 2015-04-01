# -*- coding: utf-8 -*-

'''
Created on Feb 26, 2013

@author: zhangdu
'''
import unittest,os
from common import TestConfig
from configuration import Configuration

class ConfigurationUT(unittest.TestCase):
    def setUp(self):
        test_config = TestConfig()
        self.data_path = test_config.get_data_path()
        self.output_path = test_config.get_output_path()
        
    def testDict(self):
        config = Configuration(os.path.join(self.data_path,'build.ini'))
        print config.getDict('IntelligentForms','other_project')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()