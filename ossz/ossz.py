tomb = [1, 2, 3, 4, 5, 6, 7, 8]
hossz  =len(tomb)
osszeg = 0 
for i in range(0, hossz):
    #print(tomb[i], end=' ')
    osszeg = osszeg + tomb[i]
print("Összeg: ",osszeg)