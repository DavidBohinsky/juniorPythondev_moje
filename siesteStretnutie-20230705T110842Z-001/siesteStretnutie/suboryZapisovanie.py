# subor = open('skuska.txt', 'w') --- len na citanie
subor = open('skuska.txt', 'a')

subor.write('retazec\n')
subor.write('retazec2\n')
subor.write('retazec3\n')

print('toto vkladam pomocou printu', end='\n', file=subor)


subor.close()