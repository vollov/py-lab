# -*- coding: utf-8 -*-

import ConfigParser,ast,os

class Configuration:
    
    def __init__(self, config):
        self.config = config

    def getOptions(self, section):
        return self.config.options(section)
        
    def get(self, section,option):
        if self.config.has_section(section) and self.config.has_option(section,option) :
            return self.config.get(section, option)
        else:
            return None
    
    def getCollection(self, section,option):
        '''dict example: {1:'aaa',2:'bbb'}'''
        value = self.get(section, option)
        if value is not None:
            return ast.literal_eval(value)
        else:
            return value
        
class ProductionConfiguration(Configuration):
    def __init__(self):
        Configuration.__init__(self, ConfigParser.ConfigParser())
        current_directory = os.path.dirname(os.path.abspath(__file__))
        etc_directory = os.path.join(current_directory, '../../etc')
        ini_file_path = os.path.join(etc_directory,'config.ini')
        self.config.read(ini_file_path)
        
configuration=ProductionConfiguration()