# File:  haromter.py
# Author: Zachar András
# Copyright: 2021, Zachar András	
# Group: Ifra I / N
# Date: 2021-10-20
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

import math

print("Zachar András \nIfra IN \n2021-10-20")
print("Feladat 0308")
print("Háromszög T számítása 3 oldalból")
print("--------------------------------")

oldala  = 0.0
oldalb  = 0.0
oldalc  = 0.0

oldala = float(input("Az első oldal hossza: "))
oldalb = float(input("Az második oldal hossza: "))
oldalc = float(input("Az harmadik oldal hossza: "))

# s = a háromszög kerületének a fele
s = (oldala + oldalb + oldalc) / 2
 
T =math.sqrt( s * (s - oldala) * (s - oldalb) * (s - oldalc))

print("A háromszög T: %.2f" % T)







