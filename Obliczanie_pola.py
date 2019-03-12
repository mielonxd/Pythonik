from math import *

def funkcja1(x):
    return (2*x*x)-(3*x)+5

def funkcja2(x):
    return (x*x)+x-10

def g(x):
    return -(x*x)-15

def pole(p,q,n):
    dl=(q-p)/n
    s=0
    i=0
    while(i<n):
        s+=fabs(funkcja1(p+dl*i+(dl/2)))
        i=i+1
    else:
        pole=dl*s
        print(pole)

pole(4,9,20)

def pole2(p,q,n):
    dl=(q-p)/n
    s=0
    i=1
    while(i<n):
        s+=fabs(funkcja2(p+i*dl))
        i=i+1
    else:
        pole=(dl/2)*(fabs(funkcja2(p))+fabs(funkcja2(q))+2*s)
        return pole

pole2(4,9,20)

def poleG(p,q,n):
    dl=(q-p)/n
    s=0
    i=1
    while(i<n):
        s+=fabs(g(p+i*dl))
        i=i+1
    else:
        pole=(dl/2)*(fabs(g(p))+fabs(g(q))+2*s)
        return pole

poleG(4,9,20)

print("Suma: ",pole2(4,9,20)+poleG(4,9,20))
