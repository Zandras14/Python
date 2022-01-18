# File: bolygo.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-17
# Github: https://github.com/zandras14/
# Licenc: GNU GPL


bolygo_nev = input('Bolgó neve: ')
if bolygo_nev == '':
    exit()
torpe = ['Ceres', 'Haumea', 'Eris', 'Makemake']
if bolygo_nev in torpe:
    print('Törpebolygó')
else:
    print('Nem besorolt')
