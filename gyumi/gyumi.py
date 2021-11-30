
file_name = 'gyumi/files/gyumi.txt'




def fajbaIras(gyumi):
    fp = open(file_name, 'a', encoding='utf-8')
    fp.write(gyumi + '\n')
    fp.close()

gyumi = ''
while gyumi != 'vege':
    gyumi = input('Gyümölcs: ')
    if gyumi != 'vege':
        fajbaIras(gyumi)