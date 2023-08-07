# 1 2 3
# 4 5 7
# 5 6 7
riadok01 = [1, 2, 3]
riadok02 = [4, 5, 6]
riadok03 = [5, 6, 7]
m = [riadok01, riadok02, riadok03]

m = [[1, 2, 3], [4, 5, 6], [5, 6, 7]]

# 07. vypiste riadky zoznamu m pod seba - do riadkov
for riadok in m:
    print(riadok)

print('------------------')
# ako budeme pouzivat castejsie
def vypis(tabulka):
    for riadok in tabulka:
        for prvok in riadok:
            print(prvok, end=' ')
        print()

def vypisIndex(tabulka):
    for i in range(len(tabulka)):
        for j in range(len(tabulka[i])):
            print(tabulka[i][j], end=' ')
        print()

vypisIndex(m)
print('------------------')
# --------------------------------------
matica = []
for i in range(3):
    matica.append([0,0,0])

print(matica)
vypis(matica)
print()
matica[0][1] = 9
vypis(matica)
