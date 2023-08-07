#Vytvorte program, ktorý bude počítať výsledný prospech na vysvedčení.
# Vstupné údaje – známky načíta zo vstupného súboru.
# Výsledné údaje: známky a prospech vypíše na obrazovku.

#priemer <= 1,5 – prospel s vyznamenaním priemer <= 2 prospel veľmi dobre
#priemer > 2 prospel
#ak je medzi známkami 5 - neprospel

def vypisZnamok():
    subor = open("znamky", "r+")
    for i in subor:
        print(i.strip())
    subor.close()

def prospech():
    subor = open("znamky.txt", "r+")
    for i in subor:
        znamky = subor.readline()
        pocetznamok = len(znamky)
        print(pocetznamok)
    subor.close()



prospech()

