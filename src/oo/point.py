#!/usr/bin/python

#http://www.tutorialspoint.com/python/python_classes_objects.htm

class Point:
    '''demo class for point'''
    
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
   
    def display(self):
        print "x : ", self.x,  ", y: ", self.y

    def length(self):
        return (self.x+self.y)*2
    
def test():
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    pt4 = Point(2,3)
    pt4.display()
    
    print id(pt1), id(pt2), id(pt3), id(pt4) # prints the ids of the obejcts
    del pt1
    del pt2
    del pt3
    del pt4

if __name__ == '__main__':test()