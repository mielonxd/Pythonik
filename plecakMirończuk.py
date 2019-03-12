

def plecak(n,W,C,waga):
    wynik=0
    K=[]
    i=1
    for i in range(1,n):
        K.append(waga//C[i])
        waga=waga-(K[i-1]*C[i])
        wynik=wynik+(K[i-1]*W[i])
    print(wynik)
    print(K)


plecak(6,[0,8,3,1,2,1],[0,4,2,1,3,7],11)

def plecakDecyzyjny(n,W,C,waga):
    wynik=0
    K=[]
    for i in range(1,n):
        if C[i]<waga:
            K.append(1)
            waga=waga-C[i]
            wynik=wynik+W[i]
        else:
            K.append(0)
    print(wynik)
    print(K)

plecakDecyzyjny(6,[0,8,3,1,2,1],[0,4,2,1,3,7],11)

def plecakDynamiczny(n,W,C,waga):
    Wartosci=[0,n][0,waga]
    Numery=[0,n][0,waga]
    for i in range(1,n):
        for j in range(1,waga):
            if j<C[i] and Wartosci[i-1][j] < Wartosci[i][j-C[i]+W[i]]:
                Wartosci[i][j]=Wartosci[i][j-C[i]+W[i]]
                Numery[i][j]=i
            else:
                Wartosci[i][j]=Wartosci[i-1][j]
                Numery[i][j]=Numery[i-1][j]
    print(max(Wartosci[1,n][1,waga]))
    print(Numery[1,n][1,waga])

plecakDynamiczny(6,[0,8,3,1,2,1],[0,4,2,1,3,7],11)




