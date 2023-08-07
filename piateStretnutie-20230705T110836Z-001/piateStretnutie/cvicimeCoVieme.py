# naprogramuj funkciu, ktorá načíta rýchlosť v kilometroch za hodinu
# a vypíše ju v metroch za sekundu.
def kmNaSec(rychlostVKm):
    rychlostVSec = rychlostVKm / 3.6
    return rychlostVSec

# 02. naprogramuj funkciu, ktorá načíta vzdialenosť v kilometroch a vypíše ju
# v námorných míľach, ak vieme, že 1 námorná míľa je 1850 metrov.
# Vysledok vrati pomocou navratovej hodnoty (pouzi return)
def prevodMil(vzdialenostVKm):
    vzdialenostVNm = (vzdialenostVKm * 1000) / 1850
    return vzdialenostVNm

povodnaHodnota = float(input('zadaj povodnu hodnotu: '))
premenenaRychlost = kmNaSec(povodnaHodnota)
premenenaVzdialenost = prevodMil(povodnaHodnota)

print('Zadana rychlost po prevode je v m/s: ', round(premenenaRychlost,2))
print('Zadana vzdialenost po prevode je v Nm: ', round(premenenaVzdialenost,2))