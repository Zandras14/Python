
ureslista = []

print(ureslista)

ureslista.append(35)
ureslista.append(48)
print(ureslista)
ureslista[0] = 107
print(ureslista)
print(ureslista[0])

masik = [107, 48]
harmadik = masik

print(ureslista == masik)
print(ureslista is masik)
print(harmadik is masik)
print(len(harmadik))

szamok = []
szamok.extend(range(50 ,100))
print(szamok)

egyList = [30, 41, 27, 19, 45, 35, 87, 53, 17]
for elem in egyList:
    print(elem , end=' ')
print()
egyList.insert(1, 20)
for elem in egyList:
    print(elem , end=' ')
print()
print(egyList.index(41))
egyList.clear()
print(egyList)



