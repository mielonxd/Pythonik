import math

def zad1(x,y):
    d=math.fabs(3*x+4*y-4)/math.sqrt(3.0*3.0+4.0*4.0)
    if d==0:
        print("Punkt (",x,",",y,") Lezy na prostej")
    else:
        print("Punkt (", x, ",", y, ") nie lezy na prostej")

print("Zad1:")
zad1(0,1)
zad1(2.5,3)

def zad2():
    ##Dane:Liczby rzeczywiste: x, y (współrzędne punktu P), A,B,C(wspolczynniki prostej)
    ##Wynik: Odleglosc punktu P od prostej
    A = float(input("Podaj A: "))
    B = float(input("Podaj B: "))
    C = float(input("Podaj C: "))
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    d = math.fabs(A*x+B*y+C) / math.sqrt(A * A + B * B)
    print("Odleglosc punktu P od prostej wynosi: ",d)

print("Zad2:")
zad2()

def zad3():
    ##Dane:Liczby rzeczywiste: x1, y1, x2,y2 (współrzędne punktu A i B), A,B,C(wspolczynniki prostej)
    ##Wynik: Komunikat informujący, czy odcinek AB leży na prostej Ax+By+C = 0.
    x1=float(input("Podaj x1: "))
    y1=float(input("Podaj y1: "))
    x2=float(input("Podaj x2: "))
    y2=float(input("Podaj y2: "))
    A=float(input("Podaj A: "))
    B=float(input("Podaj B: "))
    C=float(input("Podaj C: "))
    d = math.fabs(A * x1 + B * y1 + C) / math.sqrt(A * A + B * B)
    e = math.fabs(A * x2 + B * y2 + C) / math.sqrt(A * A + B * B)
    if d == 0 and d == e:
        print("Odcinek lezy na prostej")
    else:
        print("Odcinek nie lezy na prostej")

print("Zad3:")
zad3()

def zad4():
    x1 = float(input("Podaj x1: "))
    y1 = float(input("Podaj y1: "))
    x2 = float(input("Podaj x2: "))
    y2 = float(input("Podaj y2: "))
    AB=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    AP = math.sqrt(((3 - x1)**2) + ((-2 - y1)**2))
    PB = math.sqrt(((x2 - 3)**2) + ((y2 +2)**2))
    if AP+PB==AB:
        print("Punkt nalezy do odcinka")
    if not AP+PB==AB:
        print("Punkt nie nalezy do odcinka")

print("Zad4")
zad4()

def zad5():
    ##Dane: Liczby rzeczywiste x,y,x1,y1,x2,y2(wspolrzedne punktow P,A,B)
    ##Wynik: Komunikat czy punkt P jest srodkiem odcinka AB
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    x1 = float(input("Podaj x1: "))
    y1 = float(input("Podaj y1: "))
    x2 = float(input("Podaj x2: "))
    y2 = float(input("Podaj y2: "))
    AB=math.sqrt((x2-x1)**2+(y2-y1)**2)
    PA=math.sqrt((x1-x)**2+(y1-y)**2)
    PB=math.sqrt((x2-x)**2+(y2-y)**2)
    if PA==PB and AB==PA+PB:
        print("Punkt P jest srodkiem odcinka AB")
    else:
        print("Punkt P nie jest srodkiem odcinka AB")

print("Zad5:")
zad5()

def zad6():
    ##Wspolrzedne punktu P
    x0 = float(input("Podaj x0: "))
    y0 = float(input("Podaj y0: "))
    ##Wspolrzedne srodka S
    x1 = float(input("Podaj x1: "))
    y1 = float(input("Podaj y1: "))
    r=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    print("Promien wynosi: ",r)
    ##Wspolrzedne punktu T
    x2 = float(input("Podaj x2: "))
    y2 = float(input("Podaj y2: "))
    d=math.sqrt((x2-x1)**2+(y2-y1)**2) ##odleglosc punktu T(x2,y2) od srodka S(x1,y1)
    if r<=d:
        print("Punkt T nalezy do okregu")
    else:
        print("Punkt T nie nalezy do okregu")



print("Zad6:")
zad6()

