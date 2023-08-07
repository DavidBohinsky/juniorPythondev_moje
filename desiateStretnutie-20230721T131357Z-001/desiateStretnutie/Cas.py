# 01. Zadefinuj triedu Cas, ktorá bude mať dva celočíselné atribúty hodiny a minuty.
# Aj inicializácia (metóda __init__()) bude mať dva parametre hodiny a minuty.
# Metóda vypis() vypíše nastavený čas v tvare čas je 9:17
class Cas:
    hodiny = 0
    minuty = 0

    def __init__(self, hod, minut):
        self.hodiny = hod
        self.minuty = minut

    def vypis(self):
        print('Cas je', self.hodiny, ':', self.minuty)

    # 02. Do triedy Cas z úlohy (1) pridaj metódu toString(), ktorá nič nevypisuje,
    # ale namiesto toho vráti (return) znakový reťazec s hodinami a minútami v tvare '9:17'.
    def toString(self):
        return str(self.hodiny) + ':' + str(self.minuty)

    # 03. Do triedy Cas z úlohy dopíš metódu pridaj(), ktorá bude mať 2 parametre hodiny
    # a minuty. Metóda pridá k uloženému času zadané hodiny a minúty.
    def pridaj(self, hod, min):
        self.hodiny = self.hodiny + hod
        if (self.minuty + min) >= 60:
            pom = (self.minuty + min) // 60
            self.hodiny = self.hodiny + pom
            self.minuty = (self.minuty + min) - (60 * pom)
        else:
            self.minuty = self.minuty + min

# 04. Napíš globálnu funkciu (nie metódu) neskor(cas, hodiny, minuty), ktorá vytvorí (return) 
# novú inštanciu triedy Cas. Táto nová inštancia bude od zadaného času (parameter cas je tiež 
# inštancia triedy Cas) posunutá o zadaný počet hodín a minút. Využi metódu pridaj().
def neskor(cas, hod, minut):
    novyCas = Cas(cas.hodiny, cas.minuty)
    novyCas.pridaj(hod, minut)
    return novyCas

# 05. Vytvor pätnásť-prvkový zoznam inštancií triedy Cas, v ktorom prvý prvok reprezentuje
# 8:10 a každý ďalší je posunutý o 50 minút. Ďalšie časy v zozname vytváraj v cykle,
# využi funkciu neskor().
zoznamCas = []
prvyCas = Cas(8,10)
zoznamCas.append(prvyCas)

for i in range(1,15):
    pomCas = neskor(zoznamCas[i-1],0,50)
    zoznamCas.append(pomCas)

for prvok in zoznamCas:
    prvok.vypis()