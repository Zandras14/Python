import random

lottoNumbers = []
winNumbers = []

for i in range(1, 91):
    lottoNumbers.append(i)

# print(len(lottoNumbers))

pool = 90

for i in range(0 , 5):
    
    choose = random.randrange(0 , pool)
    winNumbers.append(lottoNumbers[choose])
    #lottoNumbers.remove(choose)
    del(lottoNumbers[choose])
    pool -= 1
    print(pool)

print(winNumbers)
print(len(lottoNumbers))
