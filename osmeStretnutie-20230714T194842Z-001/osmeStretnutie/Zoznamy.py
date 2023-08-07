# zakladne typy : int, float, bool
# postupnosti: znakov str, riadkov subor, cisel range()
# -------
# datova struktura ZOZNAM : list
# postupnost hodnot lubovolnych typov
# == tabulka, pole
prazdnyZoznam = []
zoznamTeplot = [15, 25, 35, 14, 12, 21, 13]
zoznamNakupny = ['chlieb', 'maslo', 'jablka']
zoznamZvierat = ['pes', 'macka', 'rybicka']

# 01. vytvorte program, v ktorom si nadefinujete zoznamTeplot,
# a program vam vypocita priemernu teplotu
sucet = 0
pocet = 0
for prvok in zoznamTeplot:
    sucet += prvok
    pocet += 1
priemer = sucet / pocet
print('Priemerna teplota je', round(priemer, 2))

# 02. zo zoznamu teplot vypiste maximalnu teplotu
max = zoznamTeplot[0]
for prvok in zoznamTeplot:
    if max < prvok:
        max = prvok
print('Najteplejsie bolo',max,'stupnov')

# 03. vypiste prvky lubovolneho zoznamu do jedneho riadku
zviera = ['pes', 'Dunco', 2011, 35.7, 'hneda']
print('prvky zoznamu:', end=' ')
for prvok in zviera:
    print(prvok, end=' ')

print()

# ------
zviera = ['pes', 'Dunco', 2011, 35.7, 'hneda']
print(zviera[0])
zviera[0] = 'macka'
print(zviera[0])

teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(len(teploty)):
    teploty[i] = teploty[i] + 2
print(teploty)

# len(teploty) # dlzka zoznamu - pocet prvkov
# sum(teploty) # vypocita ciselny sucet prvkov
# max(teploty) # vrati max prvok
# min(teploty) # vrati min prvok
# list(hodnota)

zoznam = list()
zoznam = list('Python')
print(zoznam)
zoznam = list(range(5, 16))
print(zoznam)
print(zoznam[3:6])

# zoznam.funkcia(parameter)
zoznam.count(5)
zoznam.index(5)
# append dava vzdy na koniec
zoznam.append(4) # zoznam.append(hodnota)

a = [2, 3, 6, 7]
a.append(23)
print(a)

# insert(index, hodnota)
a.insert(2,111)
print(a)

# pop() - odoberie posledny prvok
# pop(index) - odoberie prislusny prvok na danom indexe
# remove(hodnota) - odoberie zo zoznamu prvý výskyt prvku s danou hodnotou

# sort() - zmení poradie prvkov zoznamu tak, aby boli usporiadané vzostupne

