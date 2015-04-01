# -*- coding: utf-8 -*-
from food import Food
from utils.setting import configuration

class Bread(Food):
    def __init__(self, name, config):
        Food.__init__(self, name,config)
        self._name = name
    
    def display(self):
        print 'Bread display parent name:', self.name
        print "Bread display self name : ", self._name
        print "c.config = ", self.config.getCollection('car', 'parts')

def test():
    bread = Bread('Bread instance', configuration)
    bread.display()
    bread.show()

    
if __name__ == '__main__':test()