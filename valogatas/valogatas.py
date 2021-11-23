import random

numbers01 = []
numbPar = []
numbNeg  =[]


for i in range(0,10000):    
    numberRand = random.randrange( 0, 1000 )
    numbers01.append( numberRand )

for i in range(0 ,10000):
    if numbers01[i] % 2 == 0:
        numbPar.append(numbers01)
    else:
        numbNeg.append(numbers01)
        

print(len(numbers01))
print(len(numbPar))
print(len(numbNeg))


 