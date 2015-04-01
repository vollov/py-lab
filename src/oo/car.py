# -*- coding: utf-8 -*-
from vehicle import Vehicle
from vehicle.truck import Truck
from configuration import configuration

class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, "Honda")
        self._name = name
        self._config = configuration
    
    def display(self):
        Vehicle.display(self)
        print 'Car display parent name:', self.name
        print "Car display self name : ", self._name
        print self._config
        
def test():
    car = Car('Accrod')
    print car, car.power
    car.display()
    car.show()
    
    truck = Truck('GMC')
    truck.display()
    
#    x = {u'depth': 0, u'right': 2, u'name': u'ROOT', u'left': 1}
#    print 'right=' , x.right
    
if __name__ == '__main__':test()