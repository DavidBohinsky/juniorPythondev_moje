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

# 06. Zadefinuj triedu UcetHeslo, ktorá je odvodená z triedy Ucet
class UcetHeslo(Ucet):
    # __init__(meno, heslo, suma) - k účtu si zapamätá aj heslo
    def __init__(self, meno, heslo, suma):
        super().__init__(meno,suma)
        self.heslo = heslo
    # vklad(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje vklad
    def vklad(self, suma):
        heslo = input('zadaj heslo')
        if heslo == self.heslo:
            super().vklad(suma)
        else:
            print('heslo bolo nespravne')
    # vyber(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje výber,
    #  inak vráti None
    def vyber(self, suma):
        heslo = input('zadaj heslo')
        if heslo == self.heslo:
            super().vyber(suma)
        else:
            print('heslo bolo nespravne')