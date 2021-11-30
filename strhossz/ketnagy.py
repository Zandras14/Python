# File:  ketnagy.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-30
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

print('Zachar András, 2021-11-30,Ifra IN')
print('Feladat 1052')
print('Hosszab karakterlánc ki')
print('-----------------------\n')


string1  = input('Kérek egy karakterláncot:')
hossz1 = len(string1)

string2  = input('Kérek még egy karakterláncot:')
hossz2 = len(string2)

if hossz1 > hossz2:
    print(string1)
else:
    print(string2)