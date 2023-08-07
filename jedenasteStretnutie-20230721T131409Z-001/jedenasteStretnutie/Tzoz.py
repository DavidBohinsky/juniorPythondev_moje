class TelefonnyZoznam:
    def __init__(self):
        self.zoznam = []

    def pridaj(self, meno, telCislo):
        for i in range(len(self.zoznam)):
            if self.zoznam[i][0] == meno:
                self.zoznam[i] = (meno, telCislo)
                return
        self.zoznam.append((meno, telCislo))

    def vypis(self):
        for meno, telcislo in self.zoznam:
            print(meno, ":", telcislo)


zoznamCisel = TelefonnyZoznam()
zoznamCisel.pridaj("Jana", "0901020304")

zoznamCisel.vypis()