# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Importeren software, enz
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os


# Terminal scherm leeg maken
os.system('cls')


from helper import onderstreep

uitvoer = onderstreep("AANBIEDINGEN")

uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for woord in uitvoer:
    print(woord)

print()
print()
