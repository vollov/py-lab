class InvalidTokenError(Exception): pass

mapx = {'a':3,'b':4}
def print_key(x):
    if not mapx.has_key(x):
        raise InvalidTokenError('print_key():' + x + ' is not available in the token')
    else:
        print mapx[x]
        
def test_all():
    item_list = ['a','c']
    try:
        for item in item_list:
            print_key(item)
    except InvalidTokenError, e:
        print 'Error: Invalid Token, please check config file'
        print e
        
test_all()

