# -*- coding: utf-8 -*-
from vehicle import Vehicle
from configuration import configuration

class Truck(Vehicle):
    def __init__(self, name):
        self._name = name
        self._config = configuration
    
    def display(self):
        print "Truck display self name : ", self._name
        print self._config
        
        
def test():
    car = Truck('GMC')
    car.display()
    
if __name__ == '__main__':test()