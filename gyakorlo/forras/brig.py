from bridgeModel import BridgeModel


class Brig:
    def read_file(self):
        fp = open('gyakorlo/forras/hidak.txt', 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()

        self.bridges = []

        for line in lines[1::]:
            (id, name, place, length, year) = line.split(':')
            bridge = BridgeModel(id, name, place, int(length), int(year))
            self.bridges.append(bridge)


    # Leghosszabb híd
    def longest(self):
        n = len(self.bridges)
        max_bridge = self.bridges[0]
        for bridge in self.bridges[1::]:
            if bridge.length > max_bridge.length:
                max_bridge = bridge
        print(
            max_bridge.name,      
            max_bridge.length,
            'méter'
            )


    # A Megyeri híd szerepel a listában?
    def isHaveMegyeri(self):
        n = len(self.bridges)
        ker = 'Megyeri'
        i = 0 

        while i < n and self.bridges[i].name.find(ker) == -1:
            i += 1
        
        if i < n:
            print('Van ilyen')
        else:
            print('Nincs ilyen')


    # A nem budapesti hidak nobp.txt fájlba
    def select_nobp(self):
        for bridge in self.bridges:
            if bridge.place != 'Budapest':
                self.write_bridge(bridge)
        print('Kiírva')
        

    # Híd kiírása
    def write_bridge(self, bridge):
        fp = open('gyakorlo/forras/nobp.txt', 'a',encoding='utf-8')
        fp.write(bridge.id)
        fp.write(';')
        fp.write(bridge.name)
        fp.write(';')
        fp.write(bridge.place)
        fp.write(';')
        fp.write(str(bridge.length))
        fp.write('\n')
        fp.close()


brig = Brig()
brig.read_file()
brig.longest()
brig.isHaveMegyeri()
brig.select_nobp()

