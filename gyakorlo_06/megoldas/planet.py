# File: planet.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-17
# Github: https://github.com/zandras14/
# Licenc: GNU GPL

def check_planet(bolygo):
    torpek = ['Ceres', 'Haumea', 'Eris', 'Makemake', 'Pluto']
    bolygok = ['Merkúr', 'Vénusz', 'Mars', 'Jupiter', 'Szaturnusz', 'Uránusz' ,'Neptunusz',]
    if bolygo in torpek:
        return 'törpebolygó'
    elif bolygo in bolygok:
        return 'bolygó'
    else:
        return 'ismeretlen'
        

bolygo = ''
while bolygo != 'vege':
    bolygo = input('Bolygo neve: ')
    if bolygo != 'vege':
        uzenet = check_planet(bolygo)
        print(uzenet)