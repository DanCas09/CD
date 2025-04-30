from EuclidesAlgorithm import MDC
import math

def Test1():
    D = 348
    d = 156
    mdc = MDC(D,d)
    if(mdc != math.gcd(D,d)):
        print('Test1 Failed!')
        return
    print('Test1 Succeeded!')

Test1()