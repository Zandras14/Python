# File:  maganhangzo.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-30
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

print('Zachar András, 2021-11-30, Ifra IN')
print('Feladat 1056')
print('Kiirja a maganhangzokat')
print('-----------------------\n')

magan = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']

string1  = input('Kérek egy karakterláncot:')

darab = 0

for kar in string1:
    if kar in magan:
        darab += 1

print('Magánhangzók száma:',darab)