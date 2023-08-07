zoznam = [1, 2, 5, 10, 11]
hodnota = input("vlož hodnotu: ")

while hodnota != "KONIEC":
    pozicia = input("zadaj pozíciu alebo ak na koniec, napíš KONIEC")

    if pozicia == "KONIEC":
        zoznam.append(hodnota)
    else:
        if pozicia != "KONIEC":
            index = int(pozicia)
            if index < len(zoznam):
                zoznam.insert(index, int(hodnota))
            else:
                print("neplatná pozícia")
    break

print("Zoznam: ", zoznam)