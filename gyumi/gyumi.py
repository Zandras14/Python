
def fajbaIras(gyumi):
    fp = open('gyumi/gyumi.txt', 'a', encoding='utf-8')
    fp.write(gyumi + '\n')
    fp.close()

gyumi = input('Gyümölcs: ')
fajbaIras(gyumi)