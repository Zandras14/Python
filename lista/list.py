numbers = []

for i in range(0,5):
    number  = int(input('Szam: '))
    numbers.append(number)

print(numbers)

check = False

find = int(input('Keresett szám: '))

for number in numbers:
    if number == find:
        check = True

if check:
    print('Van ilyen')
else:
    print('Nincs ilyen')