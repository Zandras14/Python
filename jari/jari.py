from os import linesep
from jaribt import Jaribt


class Cars:
    def read_file(self):
        fp = open('jari/jaribt.txt', 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()

        self.cars = []
        
        for line in lines[0::]:
            (plate , brand, year , fuel, price , ac , hun ) = line.split(':')
            car = Jaribt(plate , brand, year , fuel, price , ac , hun)
            self.cars.append(car)


    def kiBenzines(self):
        for car in self.cars:
            if car.fuel == 'benzin':
                benzines = car 
                kuka = benzines.plate , benzines.brand, benzines.year,benzines.fuel,benzines.price,benzines.ac,benzines.hun    
                print('A benzines autók adatai:',kuka)

    def millioAlatti(self):
        misi = 1000000
        for car in self.cars:
            if car.price < misi:
                millio = car
                kuka = millio.plate , millio.brand, millio.year,millio.fuel,millio.price,millio.ac,millio.hun
        print('Millio allati autók adatai:',kuka)
                
        




cars = Cars()
cars.read_file()
cars.kiBenzines()
cars.millioAlatti()