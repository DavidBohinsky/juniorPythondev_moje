def Menu():
    print("----------Hlavne menu----------")
    print(" 1 - ukoncenie programu")
    print(" 2 - zobrazenie listu kapiel")
    print(" 3 - pridat kapelu")
    print(" 4 - odobrať kapelu")
    print(" 5 - zaregistrovanie ucastnika festivalu")
    print(" 6 - zobrazenie poctu registrovanych ucastnikov na festivale")
    print(" 7 - vypisanie poctu zostavajucich miest na ubytovanie v ubytovni a v stanovom mestecku")
    print(" 8 - vypisanie aktualneho poctu registrovanych ucastnikov dokopy")
    print("----------Hlavne menu----------")



def ZobrazKapely():             # Zobrazenie kapiel
    subor = open("kapely.txt", "r")
    for i in subor:
        print(i.strip())
    subor.close()

def PridatKapelu():
    subor = open("kapely.txt", "r+")
    kapely = subor.readlines()
    pocetKapiel = len(kapely)
    if pocetKapiel <= 10:
        vlozenaKapela = input("Vlož kapelu: ")
        subor.writelines(vlozenaKapela + "\n  ")
    else:
        print("Viac kapiel už nemôžeš pridať")

    subor.close()



ZobrazKapely()
PridatKapelu()