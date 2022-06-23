from random import randint
from math import *

a = int(input())
b = int(input())
fullsum = 0


class calc:
    def summ(a,b):
        global fullsum
        print('summ =', a+b)
        fullsum += a+b
        
    def minus(a,b):
        global fullsum
        print('minus =', a-b)
        fullsum += a-b
        
    summ(a,b)
    minus(a,b)

class stepen:
    def stp(a):
        print('Корень ='sqrt(a))
    stp(5)
    