#skuste vytvorit funkciu, ktorej na vstupe zadame pocet riadkov ,
# pocet stlpco, znak/cislo a vo vysledku nam tato funkcia vygeneruje maticu,
# ktora bude naplnena len tym znakom/cislom a bude mat zodpovedajuci pocet
# riadkov a stlpcov tym ktore sme zadali v parametroch



def vypis():
    riadok = input("Zadaj pocet riadkv: ")
    stlpec = input("Zadaj pocet stlpcov: ")
    for i in len(riadok):
        print(znak[i] * riadok)
vypis()