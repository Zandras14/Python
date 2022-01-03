
tipus = input('Híd típus: ')

if tipus == '':
    exit()

hid_tipus = ['gerenda', 'keret', 'konzolos']

if tipus in hid_tipus:
    print('Hajlító vagy nyíró igénybevételek alapján tipizált')
else:
    print('Ismeretlen típus')