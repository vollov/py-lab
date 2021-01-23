from dq.pos import *
from trans.log import *

# price, credit_card, description
def test():
    print("A coffee ($2), payment=${}".format(discount(2)))
    save_transaction(2, 1111222233334444, "COFFEE")
    
if __name__ == '__main__':test()