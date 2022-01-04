



def jo_zolseg(nev):
    zoldsegek = ['cékla', 'vöröshagyma', 'karalábé', 'paprika']
    if nev in zoldsegek:
        return True
    else:    
        return False



darab_jo = 0
nev = ''
while nev != 'vege':
    nev = input('Kérek egy zölséget: ')
    if nev != 'vege':
        if jo_zolseg(nev):
            print('OK')
            darab_jo += 1
        else:
            print('Nem megfelelő zölség')   
        
print('Jó zöldségek darabszáma',darab_jo)