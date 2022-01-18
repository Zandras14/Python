from typing import List
from cropModel import CropModel

# File: crop.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-18
# Github: https://github.com/zandras14/
# Licenc: GNU GPL


class Crop:
    def __init__(self):
        self.file_name = 'gyakorlo_07/termes.txt'
        self.crops: List[CropModel] = []
        self.sepa = '---------------------------'


    def read_concent(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()


    def convert_content(self):
        for line in self.lines[1::]:
            (id, name, place, size, cropyield, year) = line.split(':')
            cropModel = CropModel(
                id,
                name,
                place, 
                int(size), 
                float(cropyield.replace(',', '.')), 
                int(year))
            self.crops.append(cropModel)


    def sum_wheat(self):
        print(self.sepa)
        weight = 0
        for crop in self.crops:
            if crop.name == 'búza':
                weight  = weight + crop.cropyield
        print(f'A búza össz súlya {weight} tonna')


    def more_then_trhee_hundred(self):
        print(self.sepa)
        for crop in self.crops:
            if crop.cropyield > 300:
                print(f'A 300 tonnánál nagyobb termések nevei: {crop.name} {crop.cropyield} tonna')   


    def area_barley(self):
        print(self.sepa)
        counter = 0
        for crop in self.crops:
            if crop.name == 'árpa':
                counter += 1
        print(f'{counter} helyen termelenk árpát')


    def area_bigger_then_eighty(self):
        print(self.sepa)
        counter = 0
        for crop in self.crops:
            if crop.size > 80:
                counter += 1
        print(f'{counter} terület nagyobb mint 80 hektár')


    def which_crop_on_csendes(self):
        print(self.sepa)
        for crop in self.crops:
            if crop.place == 'Csendes':
                print(f'Csendesen {crop.name} termett')


    def which_place_wheat_min(self):
        print(self.sepa)
        temp_list: List[CropModel] = []
        for crop in self.crops:
            if crop.name == 'búza':
                temp_list.append(crop)

        min_wheat: CropModel= temp_list[0]
        for crop in temp_list[1::]:
            if min_wheat.cropyield > crop.cropyield:
                min_wheat = crop
        print(f'{min_wheat.place} termett a legkevesebb {min_wheat.name}')


crop = Crop()
crop.read_concent()
crop.convert_content()
crop.sum_wheat()
crop.more_then_trhee_hundred()
crop.area_barley()
crop.area_bigger_then_eighty()
crop.which_crop_on_csendes()
crop.which_place_wheat_min()

#finished at 15:53