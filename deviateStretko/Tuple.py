# 05. Napíš funkciu vsetky_rozne(zoznam), ktorá zistí (vráti True alebo False),
# či sú všetky prvky zoznamu rôzne.
# Najprv si vyrob utriedený pomocný zoznam (nepokaz pôvodný) a v ňom zisťuj,
# či sa nenachádzajú dve rovnaké hodnoty za sebou.


list = [1,2,3,5,6,8,4,5,7,8]

def posun(list):
    list.append(list[0])
    list.pop(0)
    print(list)


ciselnyZoznam = [3, 5, 6, 7, 9, 11, 2, 13]

rozne = False
def vsetky_rozne(zoznam):
    for prvok in ciselnyZoznam:
        if prvok[n] == prvok[n]:
            rozne = True
        else:
            break


vsetky_rozne(ciselnyZoznam)