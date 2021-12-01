
def countWorker(): 
    file = open('feherbt/feherBt.txt', 'r' , encoding='utf-8')
    row = file.readline()
    
    counter = 0
    
    while( file.readline() ):
        if (len(row) != 0):
            counter += 1
        
    print("A dolgozók száma: ",counter)
    file.close()

def sumMiskolcs():
    file = open('feherbt/feherBt.txt', 'r' , encoding='utf-8')
    row = file.readline()
    miskolcSalary = 0
    
    while( row ):
        row = file.readline()

        if (len(row) != 0):

            rowSpt = row.split(':')

            if (rowSpt[1] == 'Miskolc'):
                
                miskolcSalary  += int( rowSpt[3] )

    print("A Miskolciak össz fizetése:", f"{miskolcSalary:,d}","Ft")   
    file.close()

def sumLajos():
    file = open('feherbt/feherBt.txt', 'r' , encoding='utf-8')
    row = file.readline()
    Lajossum = 0
    
    while( row ):
        row = file.readline()

        if (len(row) != 0):

            rowSpt = row.split(':')
            nameSpt = rowSpt[0].split(' ')

            if (nameSpt[1] == 'Lajos'):
                        
                Lajossum  += 1
    if Lajossum > 0:
        print("Jelenleg ennyi Lajos dolgozik a cégnél:", Lajossum)
    else:
        print("Nincs Lajos nevű dolgozó")
    file.close()

def start():
    countWorker()
    sumMiskolcs()
    sumLajos()

start()


