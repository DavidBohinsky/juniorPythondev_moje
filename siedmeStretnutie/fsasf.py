def prospech():
    suma = 0
    # Zadajte celú cestu k súboru
    subor = open("znamky.txt", "r")
    # Prejdite cez všetky riadky v súbore
    for i in subor:
        # Pripočítajte známku k súčtu
        suma += int(i.strip())
    # Získajte počet známok
    pocetznamok = len(subor.readlines())
    # Skontrolujte, či počet známok je väčší ako nula
    if pocetznamok > 0:
        # Vypočítajte priemer
        priemer = suma / pocetznamok
        # Vytlačte výsledok
        print(f"Priemer je: {priemer}")
    else:
        # Vytlačte chybové hlásenie
        print("Súbor neobsahuje žiadne známky")
    # Zatvorte súbor
    subor.close()

prospech()