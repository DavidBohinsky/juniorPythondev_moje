vstupnySubor = open('vstup.txt', 'r')
vystupnySubor = open('vystup.txt', 'w')

celySubor = vstupnySubor.read()

for znak in celySubor:
    if znak >= '0' and znak <= '9':
        znak = '_'
    vystupnySubor.write(znak)

vstupnySubor.close()
vystupnySubor.close()