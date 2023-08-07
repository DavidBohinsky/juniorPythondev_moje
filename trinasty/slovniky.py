telzoznam = {
    "Lucia" : 9458435340,
    "Jozef" : 9458435340,
    "Emil" : 9458435340,
    "Janka": 9458435340,
    "Ignac": 9458435340,
    "David": 9458435340,

}

print(telzoznam)

def vypis(mojDict):
    for i in mojDict:
        print(i, ":", mojDict[i])

vypis(telzoznam)

def zmena(kluc, hodnota, dict):
    dict[kluc] = hodnota

print("-------")
# nejde !!!  mojazmena = zmena(Emil, 4444, telzoznam)
#  print(mojazmena)


menoVek = {
    "Lucia" : 10,
    "Jozef" : 20,
    "Emil" : 30,
    "Janka": 40,
    "Ignac": 50,
    "David": 51,
}

for i in menoVek:
    menoVek[i] += 1

print(menoVek)

05. urobte algoritmus, ktory pre danu premennu typu dict prida novu hodnotu a kluc do tohto dict