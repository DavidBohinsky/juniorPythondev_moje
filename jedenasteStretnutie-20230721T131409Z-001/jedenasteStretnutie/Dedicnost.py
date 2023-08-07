class Zviera:
    def __init__(self, meno):
        self.meno = meno
    def __str__(self):
        return 'Zviera je typu ' + self.typ + ' vola sa ' + self.meno + ' vydava zvuk ' \
            + self.zvuk

class Pes(Zviera):
    typ = 'pes'
    zvuk = 'haf-haf'

class Macka(Zviera):
    typ = 'macka'
    zvuk = 'mnau-mnau'

zviera1 = Pes('dunco')
zviera2 = Macka('minerva')
zviera3 = Pes('ignac')
zviera4 = Macka('micka')

zviera4.zvuk = 'vrrr'

for zviera in zviera1, zviera2, zviera3, zviera4:
    print(zviera)