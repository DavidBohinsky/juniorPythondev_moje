subor = open('text.txt', 'r')
celySubor = subor.read() + ' '

pocetSlov = 0
pocetPismenVSlove = 0
najdlhsieSlovo = ''

citamSlovo = False
slovo = ''

oddelovace = (' ','.',',','\n')
for znak in celySubor:
    if citamSlovo: #prave nacitavaju znaky slova
        if znak in oddelovace: #nasli sme koneic slova, je to oddelovac
            if len(slovo) > len(najdlhsieSlovo):
                najdlhsieSlovo = slovo
            citamSlovo = False
        else:
            slovo += znak
    else:
        if not znak in oddelovace:
            slovo = znak # nasiel sa zaciatok noveho slova
            pocetSlov += 1
            citamSlovo = True

print('Pocet slove je', pocetSlov)
print('Najdlhsie slovo je', najdlhsieSlovo)

subor.close()