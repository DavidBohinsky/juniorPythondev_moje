def vypocitajProspech(priemer, jePatka):
    if jePatka:
        return 'Neprospel'
    elif priemer <= 1.5:
        return 'Prospel s vyznamenanim'
    elif priemer <= 2:
        return 'Prospel velmi dobre'
    else:
        return 'Prospel'

subor = open('znamky.txt', 'r')
sucet = 0
pocet = 0
jePatka = False

riadok = subor.readline()
while riadok != '':
    znamka = int(riadok)
    print(znamka, end=', ')
    pocet += 1
    sucet += znamka
    if znamka == 5:
        jePatka = True
    riadok = subor.readline()

prospech = vypocitajProspech((sucet/pocet), jePatka)
print(prospech)

subor.close()