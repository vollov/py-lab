# -*- coding: utf-8 -*-

class Vehicle:
    '''demo class for an OO design'''
    
    def __init__(self, name):
        self.name = name
        self.power = 100
        
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, ": base destroyed"
   
    def display(self):
        print "Vehicle display name : ", self.name
        
    def show(self):
        print "Vehicle show self name : ", self._name
        print self._config