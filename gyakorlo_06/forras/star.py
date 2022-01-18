from starModel import StarModel
from typing import List

# File: star.py
# Author: Zachar András
# Copyright: 2022, Zachar András
# Group: IFRA I/N
# Date: 2022-01-17
# Github: https://github.com/zandras14/
# Licenc: GNU GPL


class Star:
    def __init__(self):
        self.file_name = 'gyakorlo_06/forras/stars.txt'
        self.lines = []
        self.stars: List[StarModel] = []
        self.sepa = '----------------------------'
    
    def read_content(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()
        
    
    def convert_content(self):
        for line in self.lines[1::]:
            (name, constellation, 
            distance, mass, temperature, age) = line.split(':')
            
            starModel = StarModel(
                name, constellation, 
                float(distance.replace(',', '.')), 
                float(mass.replace(',', '.')), 
                int(temperature), 
                float(age.replace(',', '.')))

            self.stars.append(starModel)
    
    def print_out(self):
        print(self.sepa)
        for star in self.stars:
            print(f'{star.name} | {star.constellation}')
    

    # Van-e csillag a Göncöl csillagképben
    def star_in_goncol(self):
        print(self.sepa)
        i = 0
        n = len(self.stars)
        while i < n and self.stars[i].constellation.find('Göncöl') != -1:
            i += 1
        if i < n:
            print('Van')
        else:
            print('Nincs')


    # Legtávolabbi csillag neve, távolsága
    def farthest_star(self):
        print(self.sepa)
        max_far = self.stars[0]
        for star in self.stars:
            if star.distance > max_far.distance:
                max_far = star
        print(f'Legtávolabbi csillag {max_far.name} | {max_far.distance} ly')


    # Legalacsonyabb hőmérsékletű csillag
    def lowest_temperature_star(self):
        print(self.sepa)
        lowest = self.stars[0]
        for star in self.stars:
            if star.temperature < lowest.temperature:
                lowest = star
        print(f'Legalacsonyabb hőmérsékletű csillag {lowest.name} | {lowest.temperature} K')


    # A Csillagok átlagéletkor
    def average_age_of_stars(self):
        print(self.sepa)
        counter = 0
        age = 0
        for star in self.stars:
            counter += 1 
            age  = age + star.age
            atlag = age / counter
        print(f'A csillagok átlag életkora: {atlag} ly')


    # a Kepler-18 hány kiloggram tömegű
    def weight_of_kepler18(self):
        print(self.sepa)
        sun_mass = 1.989E30
        for star in self.stars:
            if star.name == 'Kepler-18':
                kepler_mass = star.mass * sun_mass
        print(f'A Kepler-18 súlya {kepler_mass} kg')
                
            
    # 150 fényévnél közelbbi bolygók neve és távolsága
    def close_stars(self):
        print(self.sepa)
        for star in self.stars:
            if star.distance < 150:
                print(f'150 fényévnél közelbbi bolygók: {star.name} | {star.distance} ly')
                


    # A Szextánok csillagképben található csillagok adatai
    def szextan_datas(self):
        print(self.sepa)
        for star in self.stars:
            if star.constellation == 'Szextánok':
                print(f'A Szextánok csillagképben található csillagok adatai: {star.name} | {star.distance} ly | {star.mass} M | {star.temperature} K | {star.age} Ga')
                


    # A 2 M-nél kisebb tömegű csillagok neve és tömege
    def less_than_two_mass_stars(self):
        print(self.sepa)
        for star in self.stars:
            if star.mass < 2:
                print(f'A 2 M-nél kisebb tömegű csillagok: {star.name} | {star.mass} M')


star = Star()
star.read_content()
star.convert_content()
star.print_out()
star.star_in_goncol()
star.farthest_star()
star.lowest_temperature_star()
star.average_age_of_stars()
star.weight_of_kepler18()
star.close_stars()
star.szextan_datas()
star.less_than_two_mass_stars()