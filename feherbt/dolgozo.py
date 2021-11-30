
from os import read

def countWorkers():
    file = open('feherbt/feherBt.txt', 'r' , encoding='utf-8')

    row = file.readline()
    print(type(row))

    counter = 0
    while( row ):

        row = file.readline()
        if (len(row) != 0):
            counter += 1

    print(counter)

def gerCity():
    file = open('feherbt/feherBt.txt', 'r' , encoding='utf-8')
    row = file.readline()

    while(row):
        row  = file.readline()
        if (len(row)  != 0):
            rowSpt = row.split( ":" )
            print(rowSpt[1])


def start():
    countWorkers()
    gerCity()

start()