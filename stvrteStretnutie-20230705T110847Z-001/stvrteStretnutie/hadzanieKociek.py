# Budeme simulovať hádzanie dvomi hracími kockami.
# Zakaždým vypíšeme aj ich súčet. Napíš program, ktorý to simuluje n-krát.
import random

kocka01 = 0
kocka02 = 0

n = int(input('Zadaj pocet hodov: '))
print()
for i in range(n):
    kocka01 = random.randint(1,6)
    kocka02 = random.randint(1,6)
    sucet = kocka01 + kocka02

    print('V hode cislo',(i+1),'boli hody nasledovne:')
    print('Kocka jedna = ', kocka01)
    print('Kocka dva = ', kocka02)
    print('Sucet hodu je = ', sucet)
    print('-------------')