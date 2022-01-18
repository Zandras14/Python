# File: cropModel.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-18
# Github: https://github.com/zandras14/
# Licenc: GNU GPL

class CropModel:
    def __init__(self, id, name, place, size, cropyield, year):
        self.id = id
        self.name = name
        self.place = place
        self.size = size
        self.cropyield = cropyield
        self.year = year