# File:  darab.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

janos = 'Nagy János:Szolnok:2850000'

tomb = janos.split(':')

print(tomb[0])
print(tomb[1])
print(tomb[2])
print('--------')

for i in range(0, 2):
    print(tomb[i])



nev, telepules, fizetes = janos.split(':')

print("Név: ", nev)
print("Település: ", telepules)
print("Fizetés: ", fizetes)
