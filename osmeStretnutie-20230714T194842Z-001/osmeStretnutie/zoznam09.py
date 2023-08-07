# 09. urobte program, ktory nacita index prvku ktory treba zo zoznamu vymazat
# a ten vymaze a vypise upraveny zoznam

index = int(input('Zadaj index prvku na vymaz: '))
zoznam = [4,5,3,2,5,4,54,54,5,3,2,4,45,5]

if index < len(zoznam)-1:
    zoznam.pop(index)
else:
    print('zadany index je mimo rozsah')

print(zoznam)