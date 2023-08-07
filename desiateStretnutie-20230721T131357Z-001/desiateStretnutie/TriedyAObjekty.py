# triedy == class
# objekt == instancia triedy
# nazov triedy zacina velkym pismenom
class Student:
    # init metoda sluzi na inicializovanie atributov daneho objektu
    def __init__(self, meno, priezvisko, hoby = ''):
        self.meno = meno
        self.priezvisko = priezvisko
        self.hobby = hoby
    def vypis(self):
        print('Moje meno je', self.meno, self.priezvisko)

    def nastavHobyy(self, text):
        self.hobby = text
        print(self.meno, self.priezvisko, 'ma hobby', self.hobby)

# ----- hlavna cast:
ignac = Student('Ignac', 'Nahoda')
ignac.vypis()
# volanie metody instancia.metoda(parametre)

