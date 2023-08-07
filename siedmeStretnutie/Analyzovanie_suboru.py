subor = open("Slova.txt")

pocetslov = 0

for i in subor:
    print(i)
    slova = i.split()
    pocetslov += len(slova)

print("Pocet slov je: ", pocetslov)
subor.close()