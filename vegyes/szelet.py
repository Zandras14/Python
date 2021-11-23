# File:  szelet.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL


gyumolcs = 'narancs'
print(gyumolcs[3:len(gyumolcs)])

hossz = len(gyumolcs)
print(gyumolcs[3:hossz])



print(id(gyumolcs))
gy = gyumolcs[:]
print(id(gy))
gy = 'alma'
print(gyumolcs)
print(gy)
print(gy is gyumolcs)
