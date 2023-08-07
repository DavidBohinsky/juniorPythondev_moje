def zobrazMenu():
    print('-------- menu z ktoreho si mozes vybrat --------')
    print('1 - zobrazit zostatok na ucte')
    print('2 - vklad na ucet')
    print('3 - vyber z uctu')
    print('4 - koniec programu')
    print('5 - zobrazenie menu')
    print('-------- menu z ktoreho si mozes vybrat --------')

def zostatokNaUcte():
    subor = open('zostatok.txt', 'r')
    riadok = subor.readline()
    subor.close()
    return riadok

def vkladNaUcet(sumaVkladu):
    aktualnyStav = int(zostatokNaUcte())
    novyStav = aktualnyStav + sumaVkladu
    subor = open('zostatok.txt', 'w')
    subor.write(str(novyStav))
    subor.close()

def vyberZUctu(sumaVyberu):
    aktualnyStav = int(zostatokNaUcte())
    novyStav = aktualnyStav - sumaVyberu
    subor = open('zostatok.txt', 'w')
    subor.write(str(novyStav))
    subor.close()

# ----- hlavna cast programu
zobrazMenu()
operacia = int(input('Vyber si operaciu zo zobrazeneho menu: '))

while operacia != 4:
    if operacia == 1:
        #zostatok na ucte
        print('Aktualny zostatok na ucte je:', zostatokNaUcte(), 'eur')
    elif operacia == 2:
        #vklad na ucet
        vklad = int(input('Zadaj sumu, ktoru chces vlozit na ucet: '))
        vkladNaUcet(vklad)
        print('Aktualny zostatok po vklade je:', zostatokNaUcte(), 'eur')
    elif operacia == 3:
        #vyber z uctu
        vyber = int(input('Zadaj sumu, ktoru chces vybrat z uctu: '))
        vyberZUctu(vyber)
        print('Aktualny zostatok po vybere je:', zostatokNaUcte(), 'eur')
    elif operacia == 5:
        # zobraz menu
        zobrazMenu()
    else:
        print('Takato operacia nie je definovana')
    print()
    operacia = int(input('Vyber si operaciu zo zobrazeneho menu: '))