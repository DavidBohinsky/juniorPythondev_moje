# Zadefinuj triedu Cas, ktorá bude mať dva celočíselné atribúty hodiny a minuty.
# Aj inicializácia (metóda __init__()) bude mať dva parametre hodiny a minuty.
# Metóda vypis() vypíše nastavený čas v tvare čas je 9:17

class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = input("Zadaj hodiny: ", hodiny)
        self.minuty = input("Zadaj minuty: ", minuty)
    def vypis(self):
        print("Čas je: ", self.hodiny,":", self.minuty)

    def toString(self):  #2. uloha
        return str(self.hodiny) + ":" + str(self.minuty)

    def pridaj(self, Zadanehodiny, Zadaneminuty):
        self.Zadanehodiny = input("Zadaj hodiny: ", Zadanehodiny)
        self.Zadaneminuty = input("Zadaj minuty: ", Zadaneminuty)


hodiny = Cas(9, 17)
hodiny.vypis()
ZadanyCas = Cas.pridaj()
print(ZadanyCas)


def pridaj(self, hod, min):
    self.hodiny = self.hodiny + hod
    if (self.minuty + min) >= 60:
        pom = (self.minuty + min) // 60
        self.hodiny = self.hodiny + pom
        self.minuty = (self.minuty + min) - (60 * pom)
    else:
        self.minuty = self.minuty + min

# Do triedy Cas z úlohy (1) pridaj metódu toString(), ktorá nič nevypisuje,
# ale namiesto toho vráti (return) znakový reťazec s hodinami a minútami v tvare '9:17'.

# Do triedy Cas z úlohy dopíš metódu pridaj(), ktorá bude mať 2 parametre hodiny a minuty.
# Metóda pridá k uloženému času zadané hodiny a minúty. - moje nefunguje

