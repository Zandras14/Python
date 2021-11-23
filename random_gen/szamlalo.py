import random

numbers01 = []

for i in range(0,500):    
    numberRand = random.randrange( 1, 500 )
    numbers01.append( numberRand )

szamlalo = 0
hossz = (len(numbers01))

for i in range(0, hossz):
    if numbers01[i] > 255 :
        szamlalo = szamlalo + 1

print(szamlalo) 