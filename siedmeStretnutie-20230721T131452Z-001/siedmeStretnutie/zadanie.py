def zobrazMenu():
    print('-------- menu z ktoreho si mozes vybrat --------')
    print('0 - koniec programu')
    print('1 - zobrazit list prihlasenych kapiel')
    print('2 - pridat kapelu do listu prihlasenych kapiel')
    print('3 - odobrat kapelu zo zoznamu')
    print('4 - zaregistrovat ucastnika')
    print('5 - zobrazit pocet aktualne registrovanych ucastnikov na festivale')
    print('6 - vypisat pocet zostavajucich miest na ubytovanie ucastnikov v ubytovni a v stanovom mestecku')
    print('7 - vypisat aktualny pocet registrovanych ucastnikov celkovo')
    print('-------- menu z ktoreho si mozes vybrat --------')

def zobrazList(nazovSuboru):
    subor = open(nazovSuboru, 'r', encoding='UTF-8')
    riadok = subor.readline()
    while riadok != '':
       print(riadok, end='')
       riadok = subor.readline()
    subor.close()
    return riadok

def vlozZaznam(nazov, nazovSuboru):
    subor = open(nazovSuboru, 'a', encoding='UTF-8')
    subor.write('\n'+nazov)
    subor.close()

def odoberKapelu(nazov):
    with open("kapely.txt", "r") as f:
        riadky = f.readlines()
    with open("kapely.txt", "w") as f:
        for riadok in riadky:
            if riadok.strip("\n") != nazov:
                f.write(riadok)
def validaciaPoctuKapiel():
    with open("kapely.txt", "r") as f:
        riadky = f.readlines()
    if len(riadky) >= 10:
        return False
    else:
        return True

def vratPocet(nazovSuboru):
    with open(nazovSuboru, "r") as f:
        riadky = f.readlines()
    return len(riadky)

#----- hlavna cast programu
zobrazMenu()
operacia = int(input('Vyber si operaciu zo zobrazeneho menu: '))

while operacia != 0:
    if operacia == 1:
        zobrazList('kapely.txt')
        print('\n')
    elif operacia == 2:
        if validaciaPoctuKapiel():
            nazovKapely = input('Zadaj nazov kapely: ')
            vlozZaznam(nazovKapely, 'kapely.txt')
        else:
            print('Pocet kapiel je naplneny')
        print('\n')
    elif operacia == 3:
        nazovKapely = input('Zadaj nazov kapely, ktoru chces odobrat zo zoznamu: ')
        odoberKapelu(nazovKapely)
        print('\n')
    elif operacia == 4:
        if (vratPocet('ubytovanieCamp.txt')+vratPocet('ubytovaniePenzion.txt')) < 1300:
            kam = input('Ak chces registrovat do campu, zadaj C, ak do penzionu, zadaj P')
            if kam == 'C':
                if vratPocet('ubytovanieCamp.txt') < 300:
                    meno = input('Zadaj meno ucastnika')
                    vlozZaznam(meno, 'ubytovanieCamp.txt')
                else:
                    print('Je nam luto, ale v campe uz nie je miesto')
            elif kam == 'P':
                if vratPocet('ubytovanieCamp.txt') < 1000:
                    meno = input('Zadaj meno ucastnika')
                    vlozZaznam(meno, 'ubytovaniePenzion.txt')
                else:
                    print('Je nam luto, ale v penzione uz nie je miesto')
            else:
                print('Zadana volba bola neplatna')
        else:
            print('Kapacity festivalu su naplnene')
        print('\n')
    elif operacia == 5:
        print('----- Ucastnici ubytovani v campe:')
        zobrazList('ubytovanieCamp.txt')
        print('\n')
        print('----- Ucastnici ubytovani v Penzione:')
        zobrazList('ubytovaniePenzion.txt')
        print('\n')
    elif operacia == 6:
        print('V campe nam ostava: ', (1000 - vratPocet('ubytovanieCamp.txt')), 'miest')
        print('V penzione nam ostava: ', (300 - vratPocet('ubytovaniePenzion.txt')), 'miest')
        print('\n')
    elif operacia == 7:
        camp = vratPocet('ubytovanieCamp.txt')
        penzion = vratPocet('ubytovaniePenzion.txt')
        print('V campe mame ubytovanych: ', camp,'ucastnikov')
        print('V penzione mame ubytovanych: ', penzion,'ucastnikov')
        print('Pocet registsrovanych ucastnikov celkovo je:', (camp+penzion))
        print('\n')
    operacia = int(input('Vyber si operaciu zo zobrazeneho menu: '))