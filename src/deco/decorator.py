#!/usr/bin/python

def trace(traced_function):
    def inner(*args, **kwargs):
        print '>>'
        traced_function(*args, **kwargs)
        print '<<'
    
    return inner

@trace
def fun1(x, y):
    print 'x:', x, 'y:', y

@trace  
def fun2(x,y,z):
    print x + ',' + y + ',' + z
     
def test():
    fun1('aa', 'bb')
    fun2('er','st', 'lib')
    
if __name__ == '__main__':test()
