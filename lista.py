class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def listPrint(self):
        printVal = self.head
        while printVal is not None:
            print (printVal.data)
            printVal = printVal.next
    def search(self,item):
        current=self.head
        found=False
        while current is not None and not found:
            if current.getData()==item:
                found=True
            current=current.getNext()
        return found
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())



#mylist = LinkedList()
#mylist.add(31)
#mylist.add(77)
#mylist.add(17)
#mylist.add(93)
#mylist.add(26)
#mylist.add(54)
#mylist.listPrint()
#print("Rozmiar",mylist.size())
#print("Czy jest znaleziony?: ",mylist.search(93))
#print("Czy jest znaleziony?: ",mylist.search(100))
#mylist.remove(31)
#mylist.remove(54)
#mylist.listPrint()

menu=LinkedList()
menu.add("Pizza")
menu.add("Spaghetti")
menu.add("Lasagne")
menu.add("Ravioli")
menu.add("Risotto")
menu.add("Cannoli")
menu.add("Bruschetta")
menu.add("Panna Cotta")
menu.add("Tiramisu")
menu.listPrint()
print("\n")
print("1.Dodanie do menu")
print("2.Usunięcie z menu")
print("3.Wyjscie")

ans=True
while ans:
    opcja=input("Co chcesz zrobić?")
    if opcja=='2':
        usuwanie=input("Co usunąć z menu?: ")
        menu.remove(usuwanie)
    if opcja=='1':
        dodanie=input("Co dodać do menu?: ")
        menu.add(dodanie)
    print("\n")
    menu.listPrint()
    if opcja=='3':
        exit()
















