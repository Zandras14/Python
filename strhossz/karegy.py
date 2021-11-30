# File:  karegy.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-30
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

print('Zachar András, 2021-11-30,Ifra IN')
print('Feladat 1053')
print('Bekér karakterlánc, karaktereit egymás alá')
print('------------------------------------------\n')


string1  = input('Kérek egy karakterláncot:')
hossz1 = len(string1)

for i in range(hossz1):
    print('%c' % string1[i])
for kar in string1:
    print(kar)