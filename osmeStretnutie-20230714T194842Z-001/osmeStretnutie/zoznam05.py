# 05. Napíš funkciu sucin(zoznam), ktorá vráti (return) súčin prvkov zoznamu
# (zoznam obsahuje len čísla). Ak je zoznam prázdny, funkcia vráti 1
def sucin(zoznam):
    if len(zoznam) == 0:
        return 1
    else:
        sucin = 1
        for prvok in zoznam:
            sucin = sucin * prvok
        return sucin

# ----- hlavna cast:
zoznamCisel = [3, 5, 6, 1]
print(sucin(zoznamCisel))