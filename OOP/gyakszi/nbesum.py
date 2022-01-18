counter,n,i  = 0,0,0
lista = []

n = int(input('Kérek egy n számot: '))

while counter != n:
    counter += 1
    i = int(input('Kérek még egy számot: '))
    lista.append(i)

print('A számok összege: ',sum(lista))