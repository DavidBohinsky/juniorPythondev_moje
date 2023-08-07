# pomocou príkazu input('?') najprv prečíta nejaký reťazec
retazec = input('Zadaj retazec: ')

# vypíše jeho dĺžku (počet znakov reťazca) pomocou print('dlzka =', dlzka_retazca)
dlzka_retazca = len(retazec)
print('dlzka =', dlzka_retazca)

# vypíše prevrátený reťazec pomocou print('prevrat =', iny_retazec)
#iny_retazec = retazec[::-1]
iny_retazec = ''
lenght = len(retazec) - 1
while lenght >= 0:
    iny_retazec = iny_retazec + retazec[lenght]
    lenght = lenght - 1

print('prevrat =', iny_retazec)

# vypíše šachovnicu (pomocou print()) zo znakov reťazca a znakov '*' a ' '
for j in range(len(retazec)*2):
    for i in range(len(retazec)):
        print(retazec[i],'*', end =' ')
    print()
    for i in range(len(retazec)):
        print('*',retazec[i], end =' ')
    print()