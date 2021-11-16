import random
import math

numbers01 = []
numbers02 = []

for i in range(0,5000):

    numberRand = random.randrange( 1, 101 )
    numbers01.append( numberRand )

print(len(numbers01))
print(numbers01[6])

for number in numbers01:
    powered = math.pow(number, 3)
    numbers02.append(powered)

print(numbers02[6])
    
numbers01Sum = 0
numbers02Sum = 0

for number in numbers01:
    numbers01Sum += number

for number in numbers02:
    numbers02Sum += number

print("1. lista összeg ",numbers01Sum)
print("2. lista összeg ",numbers02Sum)
