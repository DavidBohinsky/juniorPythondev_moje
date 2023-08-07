# 04. naprogramujte program, ktory nacita od uzivatela hodnotu a prida ju do zoznamu,
# s tym ze uzivatel zada ci na koniec, alebo na konkretny index
zoznam = ['Lucia', 'Marek', 'Martin']

meno = input('Zadaj meno, ktore chces pridat do zoznamu: ')
index = int(input('Zadaj index na ktory chces pridat meno, alebo -1 ak chces na koniec:'))

if index == -1:
    zoznam.append(meno)
else:
    if index < len(zoznam):
        zoznam.insert(index, meno)
    else:
        print('nevhodna operacia')

print(zoznam)