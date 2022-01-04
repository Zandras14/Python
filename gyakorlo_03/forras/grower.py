from product import Product


class Grower:
    def read_file(self):
        fp = open('gyakorlo_03/forras/products.txt', 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)
    
    # legdrágább zöldség
    def larger(self):
        max_product = self.products[0]
        for product in self.products:
            if product.price > max_product.price:
                max_product = product
        print('Legdrágább:', 
                max_product.name,
                max_product.price)



    # Az összes paprika ára
    def calcPepperPrice(self):
        count_product = self.products[0]
        for product in self.products:
            if product.name == 'paprika':
                count_product = product
        print('A paprika készleten ár alapján:',
        int(count_product.price) * int(count_product.weight))
            

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        for product in self.products:
            if product.name == 'karalábé':
                mass1_product = product
            if product.name == 'vöröshagyma':
                mass2_product = product
        print('A karalábé és a vöröshagyma össze készlete:',
        mass1_product.weight + mass2_product.weight)


    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        max_weight = self.products[0]
        for product in self.products:
            if product.weight > max_weight.weight:
                max_weight = product
        print('A legnagyobb tömegő zöldség:',
        max_weight.name)

    #JÓ DE LASSÚ
    # Van karalábé?
    def isHaveKohlrabi(self):
        for product in self.products:
            if product.name == 'karalábé':
                product_true = True
        if product_true == True:
            print('Van karalábé')
        else:
            print('Nincs karalábé')

    #JOBB MEGOLDÁS
    #def isHaveKohlrabi(self):
    #   ker = 'karalábé'
    #    n = len(self.products)
    #    i = 0
    #    product = Product()
    #    product = self.products[0]
    #    while i<n and self.products[i].name != ker:
    #        i += 1        
    #    if i<n:
    #        print('Van')
    #    else:
    #        print('Nincs')

    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        darab = 0
        for product in self.products:
            if product.price > 700:
                darab += 1
        print('Ennyi zöldség drágább mint 700 Ft:', darab)
        


grower = Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()