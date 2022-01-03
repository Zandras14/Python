def elet_Vizs(elettartam):
    if elettartam >= 50:
        return 'Állandó'
    else:
        return 'Rövid'
    
elettartam = -1
while elettartam != 0:
    elettartam = int(input('Élettartam: '))
    if elettartam != 0:
        print(elet_Vizs(elettartam))