# --- zapisujeme importy roznych kniznic

# --- definujeme funkcie
def vizualnyPredelovac ():
    print('--------------------------')

def spocitanie(a, b):
    vysledok = a + b
    return vysledok

def nasobenie(a,b):
    vysledok = a * b
    return vysledok

def pozdrav(meno):
    print('Ahoj',meno)

#napiste funkciu, ktora bude vracat retazec na zaklade parametra,
# ktory dostane s tym ze bude dostavat cislo
#0  - cervena, 1 - zlta, inak vypise zelena
def vypisFarbu(cislo):
    vysledok = ''
    if cislo == 0:
        return 'cervena'
    elif cislo == 1:
        return 'zlta'
    else:
        return 'zelena'
# Napíš funkciu obdlznik(sirka, znak='*'),
# ktorá z daného znaku znak vypíše do troch riadkov výstupu obdĺžnik zadanej šírky.
def obdlznik(cislo,znak):
    print(znak * cislo)
    print(znak, ' ' * (cislo-4),znak)
    print(znak * cislo)

# naprogramuj funkciu, ktora na vstupe dostane hmotnost v kg a vypise hmotnost v gramoch
def prevodKgNaG(hmotnostVKg):
    return hmotnostVKg * 1000

# naprogramuj funkciu, ktora načíta stranu kocky a vrati veľkosť jej povrchu.
def povrchKocky(stranaKocky):
    return 6*(stranaKocky*stranaKocky)

# naprogramuj funkciu, ktorá načíta koľko banánov zje opičia rodina za jeden deň
# a počet banánov, ktoré chovateľ priviezol a vypíše, či bude stačiť toľko banánov
# na jeden týždeň
def banany(spotrebaNaDen, kapital):
    spotreba = spotrebaNaDen * 7
    if spotreba < kapital:
        print('bananov bude dost')
    else:
        print('bananov bude malo')


# --- mame hlavnu cast kodu, ktora sa vykonava, vola funkcie a pod
banany(54, 345)
