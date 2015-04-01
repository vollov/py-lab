#!/usr/bin/python

from pc.computer import AMDCpu, IntelCpu

class CpuFactory:
    cpu_map={
             'AMD':AMDCpu(),
             'INTEL':IntelCpu()
             }
    
    def createCpu(self, cpuBrand):
        return self.cpu_map.get(cpuBrand)
    
def test():
    f = CpuFactory()
    c = f.createCpu('AMD')
    print c.getName()
    c.setSpeed(1000)
    print c.getName() + ',' + str(c.getSpeed())
    
if __name__ == '__main__':test()