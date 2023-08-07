# 08. Zadefinuj triedu Body, ktorá si bude uchovávať momentálny stav bodov
# (napríklad získané body v nejakej hre). Trieda bude mať tieto metódy:
#
# metóda pridaj() k momentálnemu stavu pridá 1 bod
# metóda uber() od momentálneho stavu odoberie 1 bod;
# metóda kolko() vráti celé číslo - momentálny bodový stav
class Body:
    stavBodov = 0

    def __init__(self, body):
        self.stavBodov = body

    def pridaj(self):
        self.stavBodov += 1

    def uber(self):
        self.stavBodov -= 1

    def kolko(self):
        return self.stavBodov


karty = Body(30)
karty.pridaj()
print(karty.kolko())
karty.uber()
print(karty.kolko())