def vypisDvaZoznamy(zoznam):
    zoz1 ,zoz2 = [], []
    for prvok in zoznam:
        if prvok < 0:
            zoz1.append(prvok)
        else:
            zoz2.append(prvok)
    print('zaporne =',zoz1)
    print('kladne =',zoz2)

vypisDvaZoznamy([5, 7.3, 0, -3, 0.0, 1, -3.14])

# ----------------------------------------------
def zoznamBezRetazcov(zoznam):
    novy = []
    for prvok in zoznam:
        if type(prvok) != str:
            novy.append(prvok)
    return novy

zoznamPreFunkciu = [2, '+', 5, 'f', 'o', 9]
print(zoznamBezRetazcov(zoznamPreFunkciu))
print(zoznamPreFunkciu)

#  ----------------------------------------------
def vypis(zoznam, pocet):
    p = 0
    while zoznam:
        print(zoznam.pop(0), end = ' ')
        p += 1
        if p % pocet == 0:
            print()

a = [5,4,6,7,43,65,3,2,3,4,65,32,54,65,3]
vypis(a, 3)
print(a)

#  ----------------------------------------------
x = ['prvy', [2,3], 'styri']
y = x[1]

print(y)
y.append('tuSom')
print(y)
print(x)

#  ----------------------------------------------
# retazec.split()
ret = input('zadaj 2 cisla')
zoznamSplit = ret.split()
print('zo vstupu:', ret)
print('po split funkcii:', zoznamSplit)
print(zoznamSplit[0])

# retazec.split(',')
retazecSplit02 = input('zadaj cisla oddelene ciarkou').split(',')
print('po split funkcii:', retazecSplit02)
print(retazecSplit02[0])

#  ----------------------------------------------
# oddelovac.join(zoznam)
zozJoin = ['prvy', 'druhy', 'treti']
stringJoin = ','.join(zozJoin)
print(stringJoin)