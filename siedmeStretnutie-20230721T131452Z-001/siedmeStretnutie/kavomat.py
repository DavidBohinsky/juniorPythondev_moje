def menu():
    print('############################')
    print('###     KAVOMAT         ####')
    print('############################')
    print('# PONUKA :                 #')
    print('# 12 - mala kava - 2,5e    #')
    print('# 22 - velka kava - 5e     #')
    print('# 32 - spesl kava - 7,4e   #')
    print('############################')
    print('# Povolene mince:          #')
    print('# 1, 2, 5, 10, 20, 50      #')
    print('############################')
    print('')

def zaplatKavu(cenaKavy):
    sum = 0
    povoleneMince = (1, 2, 5, 0.1, 0.2, 0.5)
    while sum < cenaKavy:
        print('AKtualny kredit:',sum)
        minca = float(input('Nedostatok na ucte, vhod dalsiu mincu: '))
        if minca in povoleneMince:
            sum += minca # sum = sum + minca
        else:
            print('Vhodili ste nespravnu mincu, skuste znova!')
    print('Nech sa paci, vas napoj je hotovy')
    vydavok = sum - cenaKavy
    if vydavok > 0:
        print('Vas vydavok je:', round(vydavok, 2))


# -------------
menu()
operacia = int(input('Vyber si svoju volbu: '))

if operacia == 12:
    zaplatKavu(2.5)
elif operacia == 22:
    zaplatKavu(5)
elif operacia == 32:
    zaplatKavu(7.4)
else:
    print('Zadana operacia nie je platna')