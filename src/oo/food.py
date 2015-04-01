# -*- coding: utf-8 -*-

class Food:
    '''demo class for an OO design'''
    
    def __init__(self, name, config):
        self.name = name
        self.config = config
        
    def display(self):
        print "Food display p.name : ", self.name
        
    def show(self):
        print "Food show c.name : ", self._name