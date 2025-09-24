"""
OOP 3.1 – Advanced Exceptions
This is a program that is letting a customer check out bananas at a store. 
The bananas are out of stock, so first an OutOfStockError happens. 
Then that error is turned into a bigger CheckoutError to show that the whole checkout failed. 
At the end, the program prints both the main error and the smaller error that caused it.
"""


class FruitError(Exception):
    pass

class OutOfStockError(FruitError):
    pass

class CheckOutError(FruitError):
    pass

try:
    try:
        bananas_in_stock = 0
        if bananas_in_stock == 0:
            raise OutOfStockError(" bananas are out of stock")
    
    # if customer still tries to check out
    except OutOfStockError as e:
        raise CheckOutError(" cannot check out")
    
except CheckOutError as e:
    print("caught:",e) # cannot check out
    print("Cause (__cause__):",e.__cause__) # bananas are out of stock
    print("Context (__context__):",e.__context__)