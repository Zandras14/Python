deli_lista = ['narancs','citrom','banán','kivi']

fp = open('gyumi/gyumi.txt', 'r', encoding='utf-8')
lines = fp.readlines()
fp.close()
for line in lines:
    gyumolcs = line.rstrip()
    if gyumolcs in deli_lista:
        print(gyumolcs.rstrip())



#print(lines)