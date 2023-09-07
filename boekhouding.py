import os
import csv                 # huiswerk 11



# Terminal scherm leeg maken
os.system('cls')

# import o.a. functies van uit andere bestand(en)
from helper import *                    # huiswerk 04
from presentatie import *               # huiswerk 09



# huiswerk 02
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}



# huiswerk 12
with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])




# huiswerk 05
#totaal_inkomen = som(inkomsten)

# huiswerk 10
totaal = 5250
print(presenteer(inkomsten.items(), totaal))



# huiswerk 13
# git add .
# git commit -m ""
# git push origin main



print()
print()
print()

