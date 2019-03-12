def F(x):
    return (x*x*x)+(x*5)-3
def F2(x):
    return x*((x*2)+3)-5

def polowienie(a,b,i):
    L=0
    if(F(a)==0):
        return a
    if(F(b)==0):
        return b
    while(L<i):
        s=(a+b)/2
        if(F(s)==0):
            return s
        if(F(a)*F(s)<0):
            b=s
        else:
            a=s
        L=L+1
    return (a+b)/2

def polowienie2(a,b,e):
    if(F2(a)==0):
        return a
    if(F2(b)==0):
        return b
    while(b-a>e):
        s=(a+b)/2
        if(F2(s)==0):
            return s
        if(F2(a)*F2(s)<0):
            b=s
        else:
            a=s
    return (a+b)/2

print("Znalezione miejsce zerowe",polowienie(-2,2,100))
print("Znalezione miejsce zerowe",polowienie2(-1,2,0.00001))

