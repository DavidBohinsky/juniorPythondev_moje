# 03. zadame uzivatelovi, aby zadal zoznam {nacitame zo vstupu},
# a nasledne ho vypiste tak, ze ku kazdemu prvku zoznamu, ktory zadal uzivaatel,
# pripocitate 10
#nacitajZoznam = input('zadaj zoznam cisel oddelenych ciarkov').split(',')

#for i in range(len(nacitajZoznam)):
#    nacitajZoznam[i] = int(nacitajZoznam[i]) + 10

#print(nacitajZoznam)

# 04.Napíš funkciu posun(zoznam), ktorá posunie prvky v danom zozname tak,
# že prvý sa presťahuje na koniec. Funkcia nič nevracia, len zmení obsah pôvodného zoznamu.
# [2, 3, '5', 7, 11] >>> [3, '5', 7, 11, 2]
def posun(list):
    list.append(list[0])
    list.pop(0)
    print(list)

ciselnyZoznam = [2, 3, '5', 7, 11]
#posun(ciselnyZoznam)

# 05. Napíš funkciu vsetky_rozne(zoznam), ktorá zistí (vráti True alebo False),
# či sú všetky prvky zoznamu rôzne. Najprv si vyrob utriedený pomocný zoznam (nepokaz pôvodný)
# a v ňom zisťuj, či sa nenachádzajú dve rovnaké hodnoty za sebou.
def vsetkyRozne(zoznam):
    suRovnake = False
    zoz = list(zoznam)
    zoz.sort()
    for i in range(len(zoz)-1):
        if zoz[i] == zoz[i+1]:
            suRovnake = True
            break
    return suRovnake

zoznamVstupny = [2, 7, 11, 53, 4, 9, 2]
print(vsetkyRozne(zoznamVstupny))