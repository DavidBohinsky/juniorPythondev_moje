#naprogramujte algoritmus, ktory nacita cislo n, a vypise sucet 1+2+3…+n
# n=3  sucet=1+2+3
n = int(input('zadaj lubovolne cislo: '))
sucet = 0

for i in range(n):
    sucet += i + 1

print('sucet je: ', sucet)