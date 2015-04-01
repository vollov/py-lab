# -*- coding: utf-8 -*-

import os

class TestConfig():
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        base_directory = os.path.join(current_directory, '..')
        self.data_path = os.path.join(base_directory, 'data/')
        self.output_path = os.path.join(base_directory, 'output/')
        #print 'setup()'
    
    def get_data_path(self):
        return self.data_path

    def get_output_path(self):
        return self.output_path