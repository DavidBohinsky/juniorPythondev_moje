# Napíšte program, ktorý zo vstupu od užívateľa načíta ľubovoľný
# reťazec znakov a na výstupe vypíše dĺžku tohto reťazca.
retazec = input('Zadaj lubovolny retazec: ')
print('Dlzka zadaneho retazca je',len(retazec))

if ' ' in retazec:
    # bonus: vypíšte počet znakov reťazca s aj bez medzier
    pom = 0
    pocetBezMedzier = 0
    while pom < len(retazec):
        if retazec[pom] != ' ':
            pocetBezMedzier += 1
        pom += 1

    print('Dlzka zadaneho retazca bez medzier je', pocetBezMedzier)