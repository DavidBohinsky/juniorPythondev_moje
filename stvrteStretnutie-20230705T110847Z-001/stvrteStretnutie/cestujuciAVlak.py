# Vo vlaku sa vezie 100 cestujúcich. V každej stanici, v ktorej zastane,
# niekoľko ľudí vystúpi a niekoľko nastúpi. Napíš program, ktorý odsimuluje
# n takýchto staníc s vystupovaním a nastupovaním cestujúcich. Predpokladáme,
# že v každej stanici vystúpi aj nastúpi náhodný počet cestujúcich z intervalu <0, 9>.

# vystup pre n=3
#Vo vlaku bolo 100 ľudí, 0 nastúpilo, 7 vystúpilo. Zostalo 93.
#Vo vlaku bolo 93 ľudí, 4 nastúpilo, 0 vystúpilo. Zostalo 97.
#Vo vlaku bolo 97 ľudí, 9 nastúpilo, 5 vystúpilo. Zostalo 101.
import random

pocetCestujucich = 100
vystupuju = 0
nastupuju = 0

n = int(input('Zadaj pocet stanic: '))
for i in range(n):
    vystupuju = random.randint(0,9)
    nastupuju = random.randint(0,9)
    novyPocetCestujucich = pocetCestujucich - vystupuju + nastupuju
    print('Vo vlaku bolo,',pocetCestujucich,'ludi,',nastupuju,'nastupilo,', vystupuju,
    'vystupilo. Zostalo',novyPocetCestujucich,'.')
    pocetCestujucich = novyPocetCestujucich