class Macska:
    nev = 'Névtelen'
    kor = 0
    def hangadas(self):
        print('miau')
        print(self.nev + ' vagyok')
    def allitKor(self, atvettKor):
        self.kor = atvettKor
    def kerKor(self):
        return self.kor



cirmi = Macska()
cirmi.nev = 'Cirmi'
cirmi.kor = 5
print(cirmi.kor, cirmi.nev)
cirmi.hangadas()
cirmi.allitKor(8)
print(cirmi.kor)