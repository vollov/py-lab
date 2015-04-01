#!/usr/bin/python
import utils

class Container:
    
    
    def __init__(self):
        
        component_args = ('AA','BB')
        args = [arg for arg in component_args]
        print args
        
        self.dispatcher = {'foobar': self.f1, 'bazcat': self.f2}
        
    def chk(self):
        for k in self.dispatcher.keys():
            #print 'calling ' + k
            self.dispatcher[k](k)
    
    def f1(self, n):
        print n+' -> in f1()'
        
    def f2(self,n):
        print n+' -> in f2()'

def testArgLists_1(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs

def testArgLists_2(arg0, *args, **kwargs):
    print 'arg0: "%s"' % arg0
    print 'args:', args
    print 'kwargs:', kwargs

def test():
    c = Container()
    print '=' * 40
    testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')
    print '=' * 40
    testArgLists_2('a first argument', 'aaa', 'bbb', arg1='ccc', arg2='ddd')
    print '=' * 40
    c.chk()
    
test()