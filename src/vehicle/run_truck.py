from truck import Truck
from utils.setting import configuration

def test():
    car = Truck('GMC', configuration)
    car.display()
    print car.power
    
if __name__ == '__main__':test()