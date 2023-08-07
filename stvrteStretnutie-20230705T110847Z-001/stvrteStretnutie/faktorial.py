# naprogramujte pomocou for cyklu algoritmus na vypocet faktorialu,
# pricom cislo, z ktoreho robit faktorial si nacitane na vstupe

# fakt 5 = 5*4*3*2*1
n = int(input('zadaj cislo: '))

faktorial = 1
for cislo in range(2, n+1):
    faktorial = faktorial * cislo
print(n, 'faktorial = ', faktorial)