#
#  Les 7 - Huiswerkopgaven 7.15 - vraag 5
#
# Terminal scherm leeg maken
import os
os.system('cls')
print()             # Lege regel

prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = prijzen["vanille"] * 0.8

# reclame_tekst = f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

#
# Als ik 4 * 0.8 uitvoer kom ik op 3.2
# Ik begrijp dat je met 2 cijfers achter de komma wilt werken daarom heb in onderstaande gemaakt
#
TestGetal = 2.41234000000004
testGetal1 = round(TestGetal, 2)
testGetal2 = f"{TestGetal}"[:4]

reclame_tekst2 = f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {testGetal2}"

reclame_tekst3 = reclame_tekst2.upper()

reclame_tekst4 = reclame_tekst3.split(" ")

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())

    if len(el) <= 4:
        print(el.lower())


print()
print()
print()
