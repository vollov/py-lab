#!/usr/bin/python

class Computer:
    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu
        
    def setCpu(self,cpu):
        self.cpu = cpu
    
    def getCpu(self):
        return self.cpu
        
class Cpu:

    def setSpeed(self, speed):
        self.speed = speed
    
    def getSpeed(self):
        return self.speed
    
    def getName(self):
        return self.name
    
class AMDCpu(Cpu):
    def __init__(self):
        self.name = "AMD"
        
class IntelCpu(Cpu):
    def __init__(self):
        self.name = "Intel"
    
class Memory:
    
    @property
    def name(self):
        return self.name
    
    def setSize(self,size):
        self.size = size
        
    def getSize(self):
        return self.size;
    
class KingStoneMem(Memory):
    
    def getName(self):
        return 'KingStone'
    
class SamsungMem(Memory):
    
    def getName(self):
        return 'Samsung'
    
def test():
    k = KingStoneMem()
    k.setSize(1000)
    print k.getName() + ',' + str(k.getSize())
    
    c = AMDCpu()
    print c.getName()
    
if __name__ == '__main__':test()