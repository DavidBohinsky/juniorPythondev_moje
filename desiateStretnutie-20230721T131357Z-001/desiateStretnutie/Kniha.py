# 09. Zadefinuj triedu Kniha, ktorá bude udržiavať informácie o jednej knihe.
# Trieda bude mať tieto metódy:
#
# inicializácia __init__(autor, titul)
# metóda nastav_vydavatela(vydavatel) pridá informáciu o vydavateľovi
# metóda nnastav_rok(rok) pridá informáciu o roku vydania
# metóda vypis() vypíše informácie o knihe
class Kniha:
    autor = ''
    titul = ''
    rokVydania = 0
    vydavatel = ''

    def __init__(self, autor, titul):
        self.autor = autor
        self.titul = titul

    def nastavVydavatela(self,vydavatel):
        self.vydavatel = vydavatel

    def nastavRok(self, rok):
        self.rokVydania = rok

    def vypis(self):
        print('Informacie o knihe:')
        print('Titul:', self.titul)
        print('Autor:', self.autor)
        print('Rok vydania:', self.rokVydania)
        print('Vydavatel:', self.vydavatel)


mojaKniha = Kniha('Janko','Moja kniha')
mojaKniha.vypis()
print()
mojaKniha.nastavVydavatela('Vydavatel')
mojaKniha.vypis()