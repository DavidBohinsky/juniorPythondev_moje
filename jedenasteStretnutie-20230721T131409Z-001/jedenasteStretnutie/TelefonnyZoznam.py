# 02. Zadefinuj triedu TelefonnyZoznam, ktorá bude udržiavať informácie o telefónnych
# číslach (ako zoznam list dvojíc tuple).
class TelefonnyZoznam:
    zoznam = []
    subor = ''

    # metóda __init__(meno_suboru) si zapamätá meno súboru (nič ešte nezapisuje ani nečíta)
    def __init__(self, menoSuboru):
        self.zoznam = []
        self.subor = menoSuboru

    def setSubor(self, nazSuboru):
        self.subor = nazSuboru

    def getSubor(self):
        return self.subor

    # metóda pridaj(meno, telefon) pridá do zoznamu dvojicu (meno, telefon)
    # ak takéto meno v zozname už existovalo, nepridáva novú dvojicu,
    # ale nahradí len telefónne číslo
    def pridaj(self, meno, telefon):
        prvok = (meno, telefon)
        existuje = False
        for i in range(len(self.zoznam)):
            if self.zoznam[i][0] == meno:
                pom = list(self.zoznam[i])
                pom[1] = telefon
                pomTuple = tuple(pom)
                self.zoznam.pop(i)
                self.zoznam.append(pomTuple)
                existuje = True
                break
        if existuje == False:
            self.zoznam.append(prvok)

    # metóda vypis() vypíše celý telefónny zoznam.
    def vypis(self):
        for prvok in self.zoznam:
            print(prvok[0],prvok[1])

    # metóda zapis() momentálny obsah telefónneho zoznamu zapíše do súboru: v každom riadku
    # bude jedna dvojica hodnôt meno a číslo, pričom budú navzájom oddelené znakom ';'
    # (v jednom riadku súboru môže byť, napríklad Jana;0999020304)
    def zapis(self):
        subor = open(self.subor, 'a', encoding='UTF-8')
        for prvok in self.zoznam:
            subor.write(prvok[0] + ';' + prvok[1] + '\n')
        subor.close()

    # metóda citaj() prečíta zadaný súbor a vyrobí z neho zoznam dvojíc (list s prvkami tuple)
    # - starý obsah zoznamu v pamäti sa zruší a nahradí novým
    def citaj(self):
        self.zoznam = []
        subor = open(self.subor, 'r', encoding='UTF-8')
        riadok = subor.readline()
        while riadok != '':
            pom = riadok.split(';')
            self.zoznam.append(tuple(pom))
            riadok = subor.readline()
        subor.close()
        return riadok

mojZoznam = TelefonnyZoznam('telzoz.txt')

mojZoznam.pridaj('Lucia', '09458435340')
mojZoznam.pridaj('Marek', '09458435340')
mojZoznam.pridaj('Ignac', '09458435340')

mojZoznam.zapis()
mojZoznam.citaj()

mojZoznam.vypis()
