# 08. skuste vytvorit funkciu, ktorej na vstupe zadame pocet riadkov ,
# pocet stlpco, znak/cislo a vo vysledku nam tato funkcia vygeneruje maticu,
# ktora bude naplnena len tym znakom/cislom a bude mat zodpovedajuci pocet riadkov
# a stlpcov tym ktore sme zadali v parametroch

def vytvorMaticu(pocetRiadkov, pocetStlpcov, znak):
    vyslednaMatica = []
    for i in range(pocetRiadkov):
        vyslednaMatica.append([znak] * pocetStlpcov)
    return vyslednaMatica

# 09. vygenerujte/zadefinujte si maticu z realnych celych cicsel. urobte program/funkciu,
# ktora zvysi obsah vsetkych prvkov o 1
def zvysOJedno(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = mat[i][j] + 1
    return mat

# 10. definujte maticu roznych kladnych cisiel, a napiste funkciu, ktora
# vrati vyskyt konkretneho cisla v matici
def najdiHodnotu(mat, hodnotu):
    pocet = 0
    for riadok in mat:
        for prvok in riadok:
            if prvok == hodnotu:
                pocet += 1
    return pocet

def najdiHodnotuFn(mat, hodnota):
    pocet = 0
    for riadok in mat:
        pocet += riadok.count(hodnota)
    return pocet

# 11. Napíš funkciu zoznam_suctov(tab) počíta súčty prvkov v jednotlivých riadkoch tabuľky
# a ukladá ich do výsledného zoznamu. Všetky hodnoty v riadkoch tabuľky sú nejaké čísla.
def zoznamSuctov(mat):
    vysl = []
    for i in range(len(mat)):
        medzisucet = 0
        for j in range(len(mat[i])):
            medzisucet += mat[i][j]
        vysl.append(medzisucet)
    return vysl

# 12. ocisluj prvky v matici od 1,2,3…
def ocisluj(mat):
    poc = 1
    for riadok in mat:
        for j in range(len(riadok)):
            riadok[j] = poc
            poc += 1
    return mat

# ------------------------------------------
matica = [[3,4,5],[5,5,5],[3,2,1]]

print(ocisluj(matica))
