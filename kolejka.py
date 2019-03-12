from queue import *
from random import *
from time import *
class Kolejka:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


def ziemniak(TablicaZImionami,liczba):
    kolej=Kolejka()
    for i in TablicaZImionami:
        kolej.enqueue(i)
    while kolej.size()>1:
        for i in range(liczba):
            kolej.enqueue(kolej.dequeue())
        print(kolej.dequeue())
    return kolej.dequeue()


print("Wyrzucony: ",ziemniak(["Bill","David","Susan","Jane","Kent","Brad"],5))
print("Wyrzucony: ",ziemniak(["Bill","David","Susan","Jane","Kent","Brad"],7))
print("Wyrzucony: ",ziemniak(["Bill","David","Susan","Jane","Kent","Brad"],3))

def symulacja_kolejki(czas_do_seansu,max_czas_zakupu):
    kolejka=Kolejka()
    sprzedane_bilety=[]
    for i in range(100):
        kolejka.enqueue('Osoba'+str(i))
    czas_koncowy=time()+czas_do_seansu
    czas_teraz=time()
    while czas_teraz<czas_koncowy and kolejka.isEmpty()==False:
        czas_teraz=time()
        liczba=randint(0,max_czas_zakupu)
        czas_snu=liczba
        sleep(czas_snu)
        l=kolejka.dequeue()
        print(l)
        sprzedane_bilety.append(l)
    return sprzedane_bilety

print(symulacja_kolejki(5,3))



