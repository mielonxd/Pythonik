from math import *

def algorytm(p,E,L):
    a=p
    i=0
    while fabs(a-p/a)>E and i<L:
        a=((a+p/a)/2)
        i=i+1
    print(a)

algorytm(125,0.001,10)
algorytm(1048,0.001,10)
algorytm(2000,0.001,10)
