# -*- coding: utf-8 -*-
#!/usr/bin/python

import logging.config
import yaml,os

class Logger:
    '''Configuration file Loader'''
    
    def __init__(self):
        #File config
        #logging.config.fileConfig('/opt/esm/etc/logging.conf')
        current_directory = os.path.dirname(os.path.abspath(__file__))
        log_config_path = os.path.join(current_directory, 'logger.yaml')
        log_config = yaml.load(open(log_config_path, 'r'))
        log_config.setdefault('version', 1)
        logging.config.dictConfig(log_config)
        
    def getLogger(self, name):
        return logging.getLogger(name)

def test():
    logger = Logger().getLogger("Logger test")
    logger.debug("1")
    logger.info("2")
    logger.warn("3")
    logger.error("4")
    logger.critical("5")
    
if __name__ == "__main__":test()

#import yaml
#import logging.config
##singleton logger implementation 
#D = yaml.load(open('logger.yaml', 'r'))
##print D
#D.setdefault('version', 1)
#logging.config.dictConfig(D)
#
#logger = logging.getLogger("SIEM-INSTALLER")
#
#if __name__ == "__main__":
#    logger.debug("1")
#    logger.info("2")
#    logger.warn("3")
#    logger.error("4")
#    logger.critical("5")