# 04. Zadefinuj metódy triedy TelefonnyZoznam
# Metódy:
# __init__(meno_suboru=None) inicializuje self.zoznam a zavolá self.citaj(meno_suboru), prípadnú výnimku bude teraz ignorovať
#
# pridaj(meno, telefon) pridá dvojicu (tuple) do zoznamu alebo nahradí, ak už také meno bolo v zozname
# ak meno alebo telefon nie je reťazec, vyvolá výnimku TypeError
#
# zisti(meno) vráti príslušné telefónne číslo alebo vyvolá výnimku KeyError
#
# citaj(meno_suboru) prečíta obsah súboru (v každom riadku dva reťazce oddelené medzerou), pri chybe vyvolá ValueError
#
# zapis(meno_suboru) do každého riadka zapíše meno a telefón, oddelí medzerou
#
# vypis() vypíše do textovej plochy

class TelefonnyZoznam():
    zoznam = []
    subor = ''

    def __int__(self, menosuboru):
        self.zoznam = []
        self.subor = menoSuboru

    def pridaj(self, meno, telefon):
        try:
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
        except TypeError:
            print("Meno alebo telefon nieje reťazec")

    def zisti(meno):

        try:
        return meno
        except KeyError:
        print("Key Error")


    def citaj(self):
        self.zoznam = []
        subor = open(self.subor, 'r', encoding='UTF-8')
        riadok = subor.readline()
        try:
        while riadok != '':
            pom = riadok.split(';')
            self.zoznam.append(tuple(pom))
            riadok = subor.readline()
        subor.close()
        return riadok
        except ValueError:
            print("Value Error")


    def zapis(self):
        subor = open(self.subor, 'a', encoding='UTF-8')
        try:
        for prvok in self.zoznam:
            subor.write(prvok[0] + ';' + prvok[1] + '\n')
        except
        subor.close()
