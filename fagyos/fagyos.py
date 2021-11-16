fokok = [-3,2,-6,0,-1,-2,0]
szamlalo = 0
hossz = len(fokok)
for i in range(0,hossz):
    if fokok[i] <= 0 :
        szamlalo = szamlalo + 1
print(szamlalo)