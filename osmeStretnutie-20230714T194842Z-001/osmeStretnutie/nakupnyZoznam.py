# 06. Napíš funkciu nakup(zoznam), ktorá spracuje nákupný zoznam a vráti jeho
# celkovú cenu. Vstupný zoznam obsahuje dvojice čísel v tvare [koľko, cena, koľko, cena, ...],
# ktorý pre každý nakúpený tovar označuje jeho množstvo (koľko) a jednotkovú cenu (cena).
# [3, 2.5, 0.5, 10, 1.2, 1.2]
# 13.94
def nakup(zoznam):
    sucet = 0
    i = 0
    while i < len(zoznam):
        sucet = sucet + (zoznam[i] * zoznam[i + 1])
        i += 2
    return sucet

nakupnyZoznam = [3, 2.5, 0.5, 10, 1.2, 1.2]
print(nakup(nakupnyZoznam))