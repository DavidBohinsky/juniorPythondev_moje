# 01. Napíš funkciu cele(hodnota), ktorá pomocou int prevedie danú hodnotu na celé číslo.
# Ak sa to nedá, funkcia vráti 0. Nepoužívaj try-except bez vymenovaných typov chýb.

def cele(hodnota):
    try:
        return int(hodnota)
    except ValueError:
        print("zle zadana hodnota")
        return 0

# cele("sdfs")       volam

# 02. Napíš funkciu desatinne(retazec), ktorá zistí, či je daný reťazec desatinným číslom.
# Funkcia vráti True alebo False.

def desatinne(retazec):   # toto je moje a nejde
    i = True
    c = 0
    try:
        for i in retazec:
            if i == float:
                return True

    except ValueError:
        return False


# toto tu je od Cermaka
def desatinne(retazec):
    try:
        float(retazec)
        return True
    except ValueError:
        return False


# 03. Napíš funkciu sucet(post), ktorá vypočíta „súčet“ prvkov postupnosti post.
# Predpokladaj, že všetky prvky sú rovnakého typu ako prvý prvok postupnosti.
# Ak je niektorý prvok iného typu ako prvý prvok, tak sa ho funkcia snaží najprv prekonvertovať
# na tento typ, ak sa ani to nedá, tak tento jeden prvok odignoruje.

def sucet(post):
    suc = 0
    for i in post:
        suc += i
    try:
        return suc
    except TypeError:
            print("Prvok v zozname nieje cislo")


mojsucet = ("fds", 3, 4)
print(sucet(mojsucet))

# od Jozefa

def sucet(post):
    if not post:
        return False

    typPrvku = type(post[0])
    sucet = 0

    for prvok in post:
        try:
            rovnakyPrvok = typPrvku(prvok)
            sucet += rovnakyPrvok
        except (ValueError, TypeError):
            pass
    return sucet