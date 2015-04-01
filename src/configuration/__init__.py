# -*- coding: utf-8 -*-

#!/usr/bin/python
import ConfigParser,ast,os
from utils.logger import Logger

class Configuration:
    
    def __init__(self, config_file = 'planner.ini'):
        self.logger = Logger().getLogger("configuration.Configuration")
        self._config_file = config_file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(current_directory, '../etc/' + config_file)
        self.logger.debug('Initialize Configuration with ' + self._config_file_path)
        
        self.config = ConfigParser.ConfigParser()
        self.config.read(self._config_file_path)
    
    def get(self, section,option):
        if self.config.has_section(section) and self.config.has_option(section,option) :
            return self.config.get(section, option)
        else:
            return None
    
    def getDict(self, section,option):
        '''dict example: {1:'aaa',2:'bbb'}'''
        value = self.get(section, option)
        if value is not None:
            return ast.literal_eval(value)
        else:
            return value
        
configuration = Configuration()