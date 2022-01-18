lista = []
listb = []

for i in range(1):
    a = int(input('Kérek egy értéket: '))
    b = int(input('Kérek egy értéket: '))
    listb.append(b)
    lista.append(a)

if listb > lista:
    listb[0] = lista[0]

print(listb)

