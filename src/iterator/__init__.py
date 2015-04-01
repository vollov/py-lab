
class User:
    '''demo class for an OO design'''
    
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        
u1 = User('Dustin','pwd1')
u2= User('Luke','pwd2')
u3= User('Annu','pwd3')
u4= User('Dave','pwd4')

users = [u1,u2,u3,u4]
        
my_dict={'1':'developer','2':'manager','3':'tester'}
my_list=['developer','manager','tester']
#print [ (key,value) for key,value in my_dict ]

print [ (u.name,u.passwd) for u in users]

print [ (key,my_dict[key]) for key in my_dict]
print [ key for key in my_list ]