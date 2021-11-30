# File:  tolto.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-30
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL

import random

print('Zachar András, 2021-11-30, Ifra IN')
print('Lista feltöltése')
print('----------------\n')




def feltoltBetuvel(lista):   
    for i in range(0,100):
        vel = random.randrange(97,123)
        lista.append(chr(vel))


betulista = []
feltoltBetuvel(betulista)
print(betulista)
