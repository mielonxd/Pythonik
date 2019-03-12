def zad3b():
    a=[5,4,3,2,1]
    for n in range(0,4):
        if a[n+1] < a[n]:
            print("Progi: ",a[n],a[n+1])
        else:
            print(a[n],"i",a[n+1],"nie jest progiem")

zad3b()

def zad3c():
    a=[5,4,3,2,1]
    for n in range(0,4):
        if a[n]>a[n+1]:
            print("Schody do dołu: ",(a[1]))


zad3c()




