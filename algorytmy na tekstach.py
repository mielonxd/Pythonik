

#tekst="Python - programming language - Python"
#print("Sprawdzanie, czy jest podciąg: ", "tho" in tekst)
#print("Ilość wystąpień podciągu - tho: ",tekst.count('tho'))
#print("Wszystkie wystąpienia podciągu")
#dl, dl_podciagu =  len(tekst), len("Python")
#i=0
#while i  < dl - dl_podciagu:
#    where = tekst.find("Python", i)
#    print("Wystąpienie podciągu - indeks: ", where)
#    i += where + dl_podciagu

def szukaj(tekst,wzorzec):
    dlT=len(tekst)
    dlW=len(wzorzec)
    T=[]
    if dlW>dlT:
        return False
    n=0
    for i in range(0,dlT-dlW+1):
        for j in range(i,i+dlW):
            if tekst[j] != wzorzec[j - i]:
                break
        if j+1 == i+dlW :
            T.append(i)
            n+=1
    if n==0:
        return False
    return n,T

tekst="INFORMACJA"
wzorzec="MA"
print(szukaj(tekst,wzorzec))

def literki(slowo1,slowo2):
    if len(slowo1)!=len(slowo2):
        print("Wyrazy nie sa anagramami")
    licz=[0 for row in range(128)]
    for i in range(0,len(slowo1)-1):
        licz[ord(slowo1[i])]
    for i in range(0,len(slowo2)-1):
        licz[ord(slowo2[i])]
    for i in range(0,128):
        if licz[i]==0:
            return True
        else:
            return False



slowo1="las"
slowo2="als"
print(literki(slowo1,slowo2))



