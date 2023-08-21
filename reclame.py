# Terminal scherm leeg maken
import os
os.system('cls')
print()

from algemene_functies import mijn_fuctie_2


# # # # # # #   vraag 5
def aanbieding_1(Smaak, Prijs, Korting):
    BedragKorting = Prijs-(Prijs*Korting)
    Tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Smaak}, van {Prijs} euro voor {BedragKorting:.2f} euro."
    return Tekst

smaak = "aardbei"
prijs = 4
korting = 0.1

#print(aanbieding_1(smaak,prijs,korting))



# # # # # # #   vraag 6
def inkomsten_totaal(Inkomsten):
    TotaalInkomsten = 0

    for Teller in Inkomsten:
        TotaalInkomsten = TotaalInkomsten + Teller

    InkomstenTotaal = f"Inkomsten deze week: {TotaalInkomsten} euro."

    return InkomstenTotaal

#DagInkomstenWeek = [220, 430, 125, 160, 205, 90, 345]

#print(inkomsten_totaal(DagInkomstenWeek))


# # # # # # #   vraag 7
def inkomsten_totaal(Inkomsten, BTW):
    TotaalInkomsten = 0

    for Teller in Inkomsten:
        TotaalInkomsten = TotaalInkomsten + Teller

    BTWbedrag = TotaalInkomsten * BTW

    InkomstenTotaal = f"Het totaal van alle inkomsten van deze week is {TotaalInkomsten} euro, waarover {BTWbedrag:.2f} euro btw betaald dient te worden."

    return InkomstenTotaal

DagInkomstenWeek = [220, 430, 125, 160, 205, 90, 345]
BTW = 0.09

#print(inkomsten_totaal(DagInkomstenWeek, BTW))



# # # # # # #   vraag 8
def laag_en_hoog(mijn_lijst):
    MAXbedrag = max(mijn_lijst)
    MINbedrag = min(mijn_lijst)

    Melding = f"Hoogste bedrag: {MAXbedrag}  &  Laagste bedrag: {MINbedrag}"

    # return Melding                   deze hoort bij vraagt 8
    return MAXbedrag, MINbedrag       #deze hoort bij vraag 12

WeekDagInkomsten = [220, 430, 125, 160, 205, 90, 345]

#print(laag_en_hoog(WeekDagInkomsten))



# # # # # # #   vraag 9
def gemiddelde(mijn_lijst):
    TotaalInkomsten = 0
    
    AantalGetallen = len(mijn_lijst)
    TotaalInkomsten = sum(mijn_lijst)
    Gemiddelde = TotaalInkomsten / AantalGetallen

    Melding = Gemiddelde
    return Melding

WeekInkomstenDag = [220, 430, 125, 160, 205, 90, 345]

#print(gemiddelde(WeekInkomstenDag))



# # # # # # #   vraag 10
def gemiddelde(mijn_lijst):
    TotaalInkomsten = 0
    
    AantalGetallen = len(mijn_lijst)
    TotaalInkomsten = sum(mijn_lijst)
    Gemiddelde = TotaalInkomsten / AantalGetallen

    Melding = f"De gemiddelde inkomsten deze week zijn {Gemiddelde:.2f} euro."
    return Melding

WeekInkomstenDag = [220, 430, 125, 160, 205, 90, 345]

#print(gemiddelde(WeekInkomstenDag))



# # # # # # #   vraag 11
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

LijstData = [10, 5, 3, 2, 1, 2, 9]

#print(meervoudig(LijstData))


# # # # # # #   vraag 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_fuctie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer


Lijstvraag12 = [12, 55, 4, 88, 43, 67]

print(combinatie(Lijstvraag12))

print()
print()
print()

