# File:  kisse.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL
# Task: 1003/4

jo = False
while  jo == False:
    kar = input("Kérek egy naygbetűt: ")
    ordkar = ord(kar)
    if not (ordkar < 65 or ordkar > 90):
        jo = True
    else:
        print('Rossz karakter! Csak nagybető!')
ujkar = ord(kar) + 32
print(chr(ujkar))
print(kar.lower())