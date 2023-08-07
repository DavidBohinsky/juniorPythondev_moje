# 08. Napíš funkciu zoznam_cifier(cislo), ktorá z daného nezáporného celého čísla
# vytvorí zoznam jeho cifier. Funkcia nič nevypisuje, len vráti (return) nejaký
# zoznam čísel.
def zoznamCifier(cislo):
    vyslednyZoznam = list(str(cislo))
    for i in range(len(vyslednyZoznam)):
        vyslednyZoznam[i] = int(vyslednyZoznam[i])
    return vyslednyZoznam

print(zoznamCifier(343423))