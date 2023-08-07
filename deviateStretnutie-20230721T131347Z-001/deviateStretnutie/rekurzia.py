# def nazov():
#    nazov()
# nazov()

def nazov():
    global pocet
    if pocet < 400:
        pocet += 1
        print(pocet)
        nazov()

pocet = 0
#nazov()

# ---------------------------- faktorial
# n * (n-1) * (n-2) * ... * 2 * 1 pre n >= 1
# 1 pre n=0
# ----
# n! = 1 pre n=0 (už vieme, že je to triviálny prípad)
# n! = (n-1)! * n (vidíme rekurzívne volanie)
def faktorial(n):
    if n == 0:
        return 1
    return faktorial(n-1) * n

print(faktorial(34))

# ------- fibonacciho cislo
# triviálny prípad: fibonacci(0) = 0
# triviálny prípad: fibonacci(1) = 1
# rekurzívny popis: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(15):
        print(fibonacci(i), end=', ')
