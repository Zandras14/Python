# File:  kisse.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL
# Task: 1005

kar  = input("Kérek egy karaktert:")
szam = ord(kar)
if szam < 110:
    print("Az n elött")
else:
    print("Az n után")