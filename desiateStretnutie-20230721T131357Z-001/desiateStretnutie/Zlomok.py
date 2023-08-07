# 06. Zapíš definíciu triedy Zlomok, ktorá v inicializácii vytvorí dva atribúty
# citatel a menovatel. Metóda vypis() vypíše pomocou print() tento zlomok v tvare
# zlomok je 3/8.
class Zlomok:
    citatel = 0
    menovatel = 0

    def __init__(self, cit, men):
        self.citatel = cit
        self.menovatel = men

    def vypis(self):
        print(str(self.citatel) + '/' + str(self.menovatel))

    # 07. Pridaj do triedy Zlomok z úlohy (6) dve metódy:
    # metóda toString() vráti (nič nevypisuje) reťazec v tvare 3/8
    def toString(self):
        return (str(self.citatel) + '/' + str(self.menovatel))
    # metóda toFloat() vráti (nič nevypisuje) desatinné číslo, ktoré reprezentuje daný zlomok
    def toFloat(self):
        return (self.citatel / self.menovatel)

# ----- hlavna cast ----
mojZlomok = Zlomok(3,8)
mojZlomok.vypis()