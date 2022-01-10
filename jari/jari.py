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
                adatok = benzines.plate , benzines.brand, benzines.year,benzines.fuel,benzines.price,benzines.ac,benzines.hun    
                print('A benzines autók adatai:',adatok)

    def millioAlatti(self):
        misi = 1000000
        for car in self.cars:
            if car.price < misi:
                millio = car
                adatok = millio.plate , millio.brand, millio.year,millio.fuel,millio.price,millio.ac,millio.hun
                print('Millio allati autók adatai:',adatok)
                
    def hondaData(self):
        for car in self.cars:
            if car.brand == 'Honda':
                honda = car
                adatok = honda.plate, honda.brand , honda.year, honda.fuel, honda.price, honda.ac, honda.hun
                print('A Hondák adatai:',adatok)
                
    def timeornot(self):
        for car in self.cars:
            db  = car.hun.split('-')
            if db[0] > '2023' and db[1] > '01' and db[2] > '10':
                print('yes')
                    
                
    
    
    
        




cars = Cars()
cars.read_file()
cars.kiBenzines()
cars.millioAlatti()
cars.hondaData()
cars.timeornot()