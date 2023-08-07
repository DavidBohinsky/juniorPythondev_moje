# 01. Napíš funkciu zostupne(zoznam), ktorá zistí, či sú prvky vstupného zoznamu
# usporiadané zostupne (každý prvok v zozname nie je väčší ako jeho predchádzajúci).
# Funkcia vráti (return) True alebo False, nemodifikuje vstupný zoznam a nič nevypisuje.
# Nepoužívaj sort ani sorted.
def zostupne(zoznam):
    isSorted = False

    for i in range(len(zoznam)-1):
        if zoznam[i] >= zoznam[i+1]:
            isSorted = True
        else:
            isSorted = False
            break

    return isSorted

# 02. Napíš funkciu sucet(zoznam1, zoznam2), ktorá sčíta/zlepí dva zoznamy čísel/reťazcov
# po prvkoch. Tieto zoznamy budu rovnako dlhe.
def sucet(zoznam1, zoznam2):
    zoznamVysledny = zoznam1
    for i in range(len(zoznam2)):
        zoznamVysledny[i] = zoznam1[i] + zoznam2[i]
    return zoznamVysledny

# --------------------------
zoz = [5, 5, 4, 1, 2, 1]
print(zostupne(zoz))

print(sucet([1, 20, 3, 40], [10, 2, 30, 4]))
print(sucet(['p','k','l','k'], ['o','i','u','o']))