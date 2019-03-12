def zad3b():
    liczbaprogow=0
    a=[2,2,2,3,1,1,3,3,1,10,11,7,7,6,7,7,8,9,9,7]
    print(a)
    for n in range(0,19):
        if a[n+1] < a[n]:
            print("Progi: ",a[n],a[n+1])
            liczbaprogow=liczbaprogow+1
        ##else:
            ##print(a[n],"i",a[n+1],"nie jest progiem")
    print("Liczba progow: ",liczbaprogow)

zad3b()

def zad3c():
    a=[5,4,3,2,1]
    print(a)
    schody=[5,4,3,2,1]
    for n in range(0,4):
        if a[n+1]<a[n]:
            n=n+1
    print("Najwieksza liczba progow w schodach do dolu(",schody,")=",n)


zad3c()




