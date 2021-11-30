class Tama:
    def __init__(self):
        self.nev = 'Névtelen'
        self.kor = 0
        self.eletero = 20
   
    def allitEletero(self, eletero):
        self.eletero = eletero
    
    def etet(self):
        self.allitEletero(self.eletero + 10)



        
pad = Tama()

adat = ''
while adat != 'vege':
    adat = input('Adatot kérek> ')
    pad.allitEletero(pad.eletero - 1)

    if adat == 'etet':
        pad.etet()

    if pad.eletero < 6:
        print('Etetésre van szükségem')

    if pad.eletero < 1:
        print('Meghaltam')
        quit()
        
