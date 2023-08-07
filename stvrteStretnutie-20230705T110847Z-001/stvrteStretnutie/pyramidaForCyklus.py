# naprogramujte:
# zadaj n: 3
# *
# **
# ***

n = int(input("Zadaj číslo: "))

for i in range(1, n+1):
    print("*" * i)

print()
# opacna piramida
for i in range(n, 0, -1):
    print("*" * i)