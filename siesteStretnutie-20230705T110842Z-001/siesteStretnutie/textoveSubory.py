subor = open('skuska.txt', 'r')

# ------ nacitanie riadku po riadku zo suboru
#riadok = subor.readline()
#while riadok != '':
#    print(riadok, end='')
#    riadok = subor.readline()

#for riadok in subor:
#    print(riadok, end='')

# ------ nacitanie celeho subor do premennej
#celySubor = ''
#for riadok in subor:
#    celySubor = celySubor + riadok
celySubor = subor.read()

subor.close()
