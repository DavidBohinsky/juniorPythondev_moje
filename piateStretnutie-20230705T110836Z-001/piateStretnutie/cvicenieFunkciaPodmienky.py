# 03. Potrebujeme oplotiť záhradu obdĺžnikového tvaru. Zostav funkciu,
# ktorá načíta rozmery záhrady a dĺžku pletiva, ktoré máme kúpené a vypíše,
# či treba ešte pletivo dokúpiť alebo nie.
def overPletivo(sirku, dlzku, dlzkaPletiva):
    obvod = 2 * (sirku + dlzku)
    if obvod > dlzkaPletiva:
        print('Pletiva mame malo, treba dokupit')
    else:
        print('Pletiva mame dost.')

# 04. Zostav funkciu, ktorá načíta teplotu vody a teplotu, od ktorej považuješ vodu
# za teplú a vypíše, či je táto voda teplá alebo nie.
def teplotaVody(teplota, hranicu):
    if teplota < hranicu:
        print('voda je studena')
    else:
        print('voda je tepla')

# 05. Zostav funkciu, ktorá načíta počet dievčat a počet chlapcov,
# ktorí prišli na tanecny kurz a vypíše, či každé dievča bude mať par.
def tanecnyKurz(pocetChl, pocetD):
    if pocetChl == pocetD:
        print('vsetci si zatancuju')
    elif pocetD > pocetChl:
        print('bez paru ostane', (pocetD-pocetChl),'dievcat')
    else:
        print('bez paru ostane', (pocetChl-pocetD),'chlapcov')

# 06. Vytvor funkciu, ktorá načíta počet ľudí v autobuse so 45 miestami na sedenie,
# počet vystupujúcich a nastupujúcich na zastávke a zistí a vypíše, či bude niekto
# v autobuse stáť alebo nie.
def autobus(pocetLudiVAutobuse, vystupujuci, nastupujuci):
    aktualnyPocet = pocetLudiVAutobuse + nastupujuci - vystupujuci
    if aktualnyPocet > 45:
        print('Pocet ludi, ktori budu musiet stat je:', (aktualnyPocet-45))
    else:
        print('Stat nebude musiet nikto')

# 07. Vytvor funkciu, ktorá načíta cenu automobilu a priemerú výšku sumy,
# ktorú môžeme mesačne na auto odložiť. Aplikácia vypíše, že je auto lacné,
# ak si naň dokážeme našetriť do roka a pol vrátane. Inak vypíše, že je auto drahé.
def nakupAuta(cenaAutomobilu, suma):
    if (18 * suma) >= cenaAutomobilu:
        print('Auto je lacne, mozme si ho dovolit.')
    else:
        print('Auto je drahe')

# 08. Urobte funkciu, ktora zobrazí k číslu mesiaca, ktore dostane ako paramter,
# jeho slovný ekvivalent.
def detekujMesiac(cislo):
    if cislo == 1:
        print('januar')
    elif cislo == 2:
        print('februar')
    elif cislo == 3:
        print('marec')
    elif cislo == 4:
        print('april')
    elif cislo == 5:
        print('maj')
    elif cislo == 6:
        print('jun')
    elif cislo == 7:
        print('jul')
    elif cislo == 8:
        print('august')
    elif cislo == 9:
        print('september')
    elif cislo == 10:
        print('oktober')
    elif cislo == 11:
        print('november')
    elif cislo == 12:
        print('december')
    else:
        print('takyto mesiac nepoznam')

# ----------------------------------------------------------------------------
