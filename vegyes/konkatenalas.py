# File:  konkatenalas.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL


vnev = input("Vezetéknév: ")
knev = input("Keresztnév: ")

teljesnev = vnev.rstrip() + ' ' + knev

print("Teljesnév", teljesnev)

print("A teljesnév hossza: ",len(teljesnev))

print("Első karakter: ", teljesnev[0])
print("Utolsó karakter: ", teljesnev[-1])