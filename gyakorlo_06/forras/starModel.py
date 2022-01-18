# File: starModel.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-17
# Github: https://github.com/zandras14/
# Licenc: GNU GPL

class StarModel:
    def __init__(self, name, constellation, 
            distance, mass, temperature, age):
        self.name = name
        self.constellation = constellation
        self.distance: float = distance
        self.mass = mass
        self.temperature = temperature
        self.age = age

