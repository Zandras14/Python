from typing import Sized


#tomb = [18,26,3,21,5,6,7] 
tomb = [18,26.8,3,21.2,5,6,7] 
#print(max(tomb))
hossz = len(tomb)
max = tomb[0]
for i in range(0, hossz):
    if tomb[i] > max:
        max = tomb[i]

print('Legnagyobb ', max)