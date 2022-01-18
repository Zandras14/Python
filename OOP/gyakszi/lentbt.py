from lentbtModel import Workers
from typing import List



class Lentbt:
    def __init__(self):
        self.workers: List[Workers] = []
    def read_content(self):
        fp = open('OOP/gyakszi/lentbt.txt', 'r',encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()

    def convert_content(self):
        for line in self.lines[0]:            
            (id, name, area, local,salary,birth) = line.split(':')
            worker = Workers(int(id), name, area, local,int(salary),birth)
            self.workers.append(worker)

    def twoMillio(self):
        counter = 0
        for twomil in self.workers:
            if twomil.salary > 2000000:
                counter += 1
        print('Ennyi dolgozó keres többet mint 2 millió:',counter)








lentbt = Lentbt()
lentbt.read_content()
lentbt.convert_content()
lentbt.twoMillio()