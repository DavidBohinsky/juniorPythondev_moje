#Napíšte program, ktorý na vstupe dostane zadaný ľubovoľný reťazec,
# úvodný a konečný index a na výstupe vypíše najskôr celý reťazec
# a do ďalšieho riadku definovaný podreťazec.
retazec = input('Zadaj retazec: ')
prvy = int(input('zadaj index od: '))
posledny = int(input('zadaj index po: '))

print(retazec[prvy-1:posledny])