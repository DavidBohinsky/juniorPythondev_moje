""""#Zadefinuj triedu Ucet s týmito metódami:

#__init__(meno, suma). - meno účty a počiatočná suma, napríklad Ucet('mbank', 100)   - ok
# __str__() retazec v tvare 'ucet mbank > 108 euro'                                  - ok
#stav() vráti momentálny stav účtu (vráti sumu na ucte)                              - ok
# vklad(suma) - danú sumu pripočíta k účtu                                           - ok
#vyber(suma) vyberie sumu z účtu (len ak je to kladné číslo),
# ak je na účte menej ako požadovaná suma, vyberie len toľko koľko sa len dá
# metóda vráti (return) vybranú sumu

class Ucet():
    stav = 100
    vlozene = 0

    def __int__(self, meno, suma):
        self.meno = meno
        self.suma = suma

    def __str__(self):
        return print("Ucet -> ", Ucet(),"eur")

    def stavUctu(self):
        return print("stav uctu: stav")

    def vklad(self):
        vlozene = int(input("Zadaj kolko eur chces vlozit: "))
        stav = stav + vlozene
        print("Ostatok na ucte je: ", stav)

mojUcet = Ucet()
mojUcet.vklad()

"""

# 05.  Zadefinuj triedu Ucet
class Ucet:
    # __init__(meno, suma) - meno účtu a počiatočná suma, napríklad Ucet('mbank', 100)
    def __init__(self, meno, suma):
        self.meno = meno
        self.suma = suma
    # __str__() - reťazec v tvare 'ucet mbank -> 100 euro'
    def __str__(self):
        return 'ucet ' + self.meno + ' -> ' + self.suma + 'euro'
    # stav() - vráti momentálny stav účtu (vráti sumu na účte)
    def stav(self):
        return self.suma
    # vklad(suma) - danú sumu pripočíta k účtu
    def vklad(self, suma):
        self.suma += suma
    # vyber(suma) - vyberie sumu z účtu (len ak je to kladné číslo),
    # ak je na účte menej ako požadovaná suma, vyberie len toľko koľko sa dá,
    # metóda vráti (return) vybranú sumu
    def vyber(self, suma):
        if suma > 0:
            if suma <= self.suma:
                self.suma = self.suma - suma
                return suma
            else:
                print('nedostatok penazi na ucte pre vyber zadanej hodnoty')
                self.suma = 0
                return self.suma
        else:
            print('vybrat sa da len kladna hodnota')


mojUcet = Ucet("Mbank", 100)
print(mojUcet)


