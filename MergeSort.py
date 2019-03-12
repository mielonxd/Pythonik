import random

def losuj(ilosc):
    random.seed()
    liczby = []
    for i in range(ilosc):
        liczby.append(random.randint(1,10))
    return liczby

#sortowanie - operacja scalania
def merge(L,start,center,finish):
    i=start
    j=center+1

    L2=[] #lista pomocnicza
    #wybieraj odpowiednie elementy z dwóch tablic
    while(i<=center) and (j<=finish):
        if L[j]<L[i]:
            L2.append(L[j])
            j=j+1
        else:
            L2.append(L[i])
            i=i+1
    #jedna z tablic skonczyla sie przepisz reszte z pozostalej
    if i<=center:
        while i<=center:
            L2.append(L[i])
            i=i+1
    else:
        while j<=finish:
            L2.append(L[j])
            j=j+1
    #przepisz wyniki z tablicy tymczasowej
    s=finish-start+1
    i=0
    while i<s:
        L[start+i]=L2[i]
        i=i+1

    return L

def merge_sort(L,start,finish):
    if start != finish:
        #dzielimy tablice
        center=(start+finish)//2
        #na lewo
        merge_sort(L,start,center)
        #na prawo
        merge_sort(L,center+1,finish)
        #operacja scalania
        merge(L,start,center,finish)
    return L

def quicksort(x):
    n = len(x)
    if n == 1 or n == 0:
        return x
    else:
        pivot = x[n-1]
        i = 0
        for j in range(n-1):
            if x[j] < pivot:
                x[j],x[i] = x[i], x[j]
                i += 1
        x[n-1],x[i] = x[i],x[n-1]
        left_part = quicksort(x[:i])
        right_part = quicksort(x[i+1:])
        left_part.append(x[i])
        return left_part + right_part

L=losuj(10)
print('Tablica',L)
L=merge_sort(L,0,len(L)-1)
print('MergeSort',L)

print('Tablica',L)
print('QuickSort',quicksort(L))

plik = open('plik.txt', 'w')
plik.write(str(L))
plik.close()



