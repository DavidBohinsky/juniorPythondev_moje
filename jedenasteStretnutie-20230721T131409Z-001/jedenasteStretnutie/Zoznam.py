# 01. Zadefinuj triedu Zoznam, pomocou ktorej si budeme vedieť udržiavať zoznam svojich
# záväzkov (sľubov, povinností, …). Tieto budeš uchovávať v atribúte zoznam typu list.
class Zoznam:
    zavazky = []

    def __init__(self):
        self.zavazky = []

    # metóda pridaj(prvok), ak sa tam takýto záväzok ešte nenachádza, pridá ho na koniec
    def pridaj(self, prvok):
        if self.jeVZozname(prvok) == False:
            self.zavazky.append(prvok)
        else:
            print('Dany zavazok sa uz v zozname nachadza.')

    # metóda vyhod(prvok), ak sa tam takýto záväzok nachádzal, vyhodí ho
    def vyhod(self, prvok):
        if self.jeVZozname(prvok) == True:
            self.zavazky.remove(prvok)

    # metóda je_v_zozname(prvok) vráti True alebo False podľa toho, či sa tam tento záväzok
    # nachádza
    def jeVZozname(self,prvok):
        existuje = False
        for prv in self.zavazky:
            if prv == prvok:
                existuje = True
                break
        return existuje

    # metóda vypis() vypíše všetky záväzky v tvare zoznam: záväzok, záväzok, záväzok
    def vypis(self):
        for prvok in self.zavazky:
            print(prvok, end=', ')
        print()


toDoList = Zoznam()
toDoList.pridaj('a')
toDoList.pridaj('b')
toDoList.pridaj('c')
toDoList.pridaj('d')
toDoList.pridaj('e')

toDoList.vypis()

print(toDoList.jeVZozname('w'))

toDoList.vyhod('d')
toDoList.vypis()