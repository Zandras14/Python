nevek = 'Béla , Imre , Gábor, Aladár, Imre, Dani, Béla, Gábor, Imre'

darab = nevek.count('Gábor')
print('Darab: ', darab)


#Bejárás:
nev = 'Béla'
for karakter in nev:
    print('karakter: ', karakter)

hossz = len(nev)
for i in range(0, hossz):
    print('Karakter: ',nev[i])


# Hogyan készítünk tömböt????
# Van egy karaktereket tartalmazó töm

lista1 = ['r','t','d']
szoveg1 = ':'.join(lista1)
print('Eredmény: ',szoveg1)

modnat = 'még nyílnak a völgyben'
print(modnat.capitalize())
print(modnat.title())
print(modnat.title())




