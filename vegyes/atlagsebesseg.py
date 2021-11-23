# File:  atlagsebesseg.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-10-20
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

print("Zachar András \nIfra IN \n2021-10-20")
print("Feladat 0309")
print("Átlagsebbésg számítás")
print("---------------------")

tav = float(input("A megtett út km-ben): "))
ido = float(input("Az eltelt idő (ó-ban): "))

#v = átlagsebesség
v = tav / ido

print("Az átlag sebesség: %.2f" % v ,end=" Km/ó")
