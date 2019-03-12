

def zad21():
    we = open("ciagi.txt")
    wy = open("wynik1.txt", "w")
    N=100
    ilearytm=0
    maxroznica=0
    roznica=0
    for q in range(N):
        dlugosc = int(we.readline())
        napis=we.readline()
        ciag=napis.split(' ')
        for i in range(dlugosc):
            ciag[i]=int(ciag[i])
    roznica=ciag[1]-ciag[0]
    arytm=True
    for i in range(dlugosc-1):
        if ciag[i+1]-ciag[i]!=roznica:
            arytm=False
            break
        if arytm:
            ilearytm += 1
            if roznica>maxroznica:
                maxroznica=roznica
    we.write("Ciagow arytmetycznych: "+str(ilearytm)+"\n")
    wy.write("Najwieksza roznica: "+str(maxroznica))


def czySzescian():
    for x in range(101):
        if x**3 == liczba:
            return True
    return False

def zad22():
    we = open("ciagi.txt")
    wy = open("wynik2.txt", "w")
    wy.write("Najwieksze szesciany: \n")
    N=100
    for q in range(N):
        dlugosc=int(we.readline())
        napis=we.readline()
        ciag=napis.readline()
        m=0
        for i in range(dlugosc):
            ciag[i]=int(ciag[i])

            if(czySzescian(ciag[i])):
                m=ciag[i]

        if(m>0):
            wy.write(str(m)+"\n")

def zad23():
    we = open("ciagi.txt")
    wy = open("wynik3.txt")
    N=20
    roznice=[0 for row in range(1000)]
    for q in range(N):
        dlugosc = int(we.readline())
        napis=we.readline()
        ciag=napis.split()
        for i in range(dlugosc):
            ciag[i]=int(ciag[i])
        for i in roznice:
            i=ciag[i+1]-ciag[i]
        if roznice[0]!=roznice[1] and roznice[1]==roznice[2]:
            wy.write(str(ciag[0])+"\n")
            continue
        if roznice[0]!=roznice[2] and roznice[1]!=roznice[2] and roznice[3]==roznice[2]:
            wy.write(str(ciag[1])+"\n")
            continue
        for i in range(dlugosc-1):
            if roznice[i]!=roznice[0]:
                wy.write(str(ciag[i+1])+"\n")


zad21()
zad22()
zad23()