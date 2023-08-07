# n-tice (tuple)
# nemenitelne (immutable) zoznamy
# operacie: +, *, in, [i], [i:j:k], ( ==, !=, <, <=, >, >=),
#       count(), index(), for cyklus, len(), sum(), min(), max()
zviera = ('slon', 2013, 'siva')
print(zviera)
print(len(zviera))

nic = ()
print(len(nic))

# n-tica s jednou hodnotou
p = (12,)
print(type(p))

# ---------------------------
print()
stred = (150,100)
print(zviera + stred)
print(zviera * 5)

# -------------------------
# tuple()
print(tuple('Python'))
print(tuple(range(3,10)))

# for cyklus s n-ticami
cisla = (2,4,5,1,6,7)
for prvok in cisla:
    print(prvok)