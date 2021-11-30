

def szamitKerulet(aOldal, bOldal, cOldal):
    return aOldal + bOldal +cOldal

def szamitTerulet(alap, magassag):
    return (alap * magassag) / 2

if __name__ == "__main__":
    print(szamitTerulet(30,35))
    print(szamitKerulet(30,35,40))