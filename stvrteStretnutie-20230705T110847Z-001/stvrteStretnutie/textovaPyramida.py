# zadaj slovo: PYTHON
# P
# YY
# TTT
# HHHH
# OOOOO
# NNNNNN
n = input("Zadaj slovo: ")

for i in range(1, len(n)+1):
    print(n[i-1] * i)