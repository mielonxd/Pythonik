import math

def trojkaty(a,b,c):
    if a+b>c:
        if a+c>b:
            if b+c>a:
                print("Mozna zbudować trojkąt")
                p= (a + b + c) / 2
                S=math.sqrt(p*(p - a)*(p - b)*(p - c))
                print("A jego pole wynosi: ",S)
                if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
                    print("Trojkat jest prostokatny")

    else:
        print("Nie mozna zbudowac trojkata")

trojkaty(3,4,5)