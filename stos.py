class stos:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

x=stos()
print("Czy pusty?",x.isEmpty())
x.push(5)
x.push("cat")
print("Wierzchołek = ",x.peek())
print("Ilość elementów: ",x.size())
print("Zdejmowane ze stosu: ",x.pop())
print("Zdejmowane ze stosu: ",x.pop())
print("Ilość elementów: ",x.size())


x=[]
print("Czy pusta?",not x)
x.append('dog')
print(x)
print(x[-1])
print(len(x))

def zad1(nawiasy):
    s=stos()
    ok=True
    n=0
    while n < len(nawiasy) and ok:
        znak=nawiasy[n]
        if znak=='(':
            s.push(znak)
        else:
            if s.isEmpty():
                ok=False
            else:
                s.pop()
        n+=1
    if ok and s.isEmpty():
        return True
    else:
        return False

print("Poprawnosc nawiasow: ",zad1("((()))"))
print("Poprawnosc nawiasow: ",zad1("((())))"))

def zad2(liczba):
    z=stos()
    h=""
    while liczba>0:
        x=liczba%2
        liczba=liczba//2
        z.push(str(x))
    while not z.isEmpty():
        h+=(z.pop())
    print(h)

zad2(100)





