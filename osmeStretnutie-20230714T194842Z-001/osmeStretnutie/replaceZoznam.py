# 07. Napíš funkciu replace_novy(zoznam, co, zaco), ktorá vráti nový zoznam:
# v tomto novom zozname budú všetky prvky s hodnotou co nahradené hodnotou zaco.
# Ostatné prvy sa prekopírujú.

def replaceNovy(zoznam, co, zaco):
    novyZoznam = zoznam

    for i in range(len(zoznam)):
        if zoznam[i] == co:
            novyZoznam[i] = zaco

    return novyZoznam

zoz = [1,2,3,2,1,3,2,1,2,3]
print(replaceNovy(zoz,2,0))