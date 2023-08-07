# 01. upravte si textovy subor tak, aby obsahoval aspon 5 riadkov.
# A naprogramujte algoritmost , ktora vypise prve tri riadky zo suboru
def zadanie01():
    subor = open('skuska.txt', 'r')
    for i in range(3):
        riadok = subor.readline()
    print(riadok, end='')
    subor.close()

# 02. naprogramujte funkciu, ktora bude pracovat so suborom a ako vstupny
# parameter dostane cislo riadku, ktory ma vypisat.
def vypisRiadku(cisloRiadku):
    subor = open('skuska.txt', 'r')
    i = 1
    riadok = subor.readline()
    while riadok !='':
        if i == cisloRiadku:
            print(riadok)
            break
        riadok = subor.readline()
        i += 1
    subor.close()

# 04. Napíš program, ktorý si vypýta meno súboru a z tohto súboru vypíše druhý riadok.
# Z tohto riadku ešte vypíše počet výskytov medzier v tomto riadku.
def zadanie04(nazovSuboru):
    subor = open(nazovSuboru, 'r')
    i = 1
    riadok = subor.readline()
    while riadok != '':
        if i == 2:
            print(riadok)
            print('pocet medzier je', riadok.count(' '))
            break
        riadok = subor.readline()
        i += 1
    subor.close()

# 05. Napíš funkciu sirka(meno_suboru), ktorá pre zadaný súbor zistí dĺžku najdlhšieho riadku.
def zadanie05(nazovSuboru):
    subor = open(nazovSuboru, 'r')
    najdlhsi = 0
    riadok = subor.readline()
    while riadok != '':
        if len(riadok) > najdlhsi:
            najdlhsi = len(riadok)
        riadok = subor.readline()
    subor.close()
    print('dlzka najdlhsieho riadku je', najdlhsi)

zadanie05('skuska.txt')