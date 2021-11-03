# File:  bennevan.py
# Author: Zachar András
# Copyright: 2021, Zachar András
# Group: Ifra I / N
# Date: 2021-11-02
# Github: https://github.com/Zandras14/
# Licenc: GNU GPL


vers = "Még nyílnak a völgyben a kerti virágok"

if 'völgy' in vers:
    print('Van völgy')
else:
    print('Nincs völgy')


print(vers.find('völgy'))

valami = 'Alma körte'
print(valami.isdigit())
print(valami.isnumeric())
print(valami.isalnum())
print(valami.isalpha())
print(valami.istitle())

#### csere ####



ip_cim = input('Ip cím: ')
eredmeny = ip_cim.replace('.',' ')
print('Eredmény:' , eredmeny)