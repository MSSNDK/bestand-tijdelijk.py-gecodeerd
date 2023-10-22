def mijn_functie_2():
    uitvoer_lijst = []
    uitvoer_lijst.append(12+3)
    uitvoer_lijst.append(12-3)
    uitvoer_lijst.append(12*3)
    uitvoer_lijst.append(12/3)
def aanbieding_1():
    smaak = "aardbei"
    prijs = 4.00
    korting = 0.1
    return f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-prijs*korting}'
print(aanbieding_1())
def inkomsten_totaal(a,b,c,d,e,f,g,):
    return a+b+c+d+e+f+g
totaal = inkomsten_totaal(220,430,125,160,205,90,345)
print(totaal)   
btw = 0.09
print(f'Het totaal van alle inkomsten van deze week is € {totaal} euro, waarover € {totaal*btw} euro btw betaald dient te worden.')
def laag_en_hoog():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    max(mijn_lijst)
    min(mijn_lijst)
    return max(mijn_lijst), min(mijn_lijst)
print(laag_en_hoog())
def gemiddelde():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    return sum(mijn_lijst) / len(mijn_lijst)
print(f' De gemiddelde inkomsten deze week zijn {gemiddelde()} euro.')
def meervoudig():
    invoer_lijst = [10,5,3,2,1,2,9]
    max(invoer_lijst)
    min(invoer_lijst)
    return max(invoer_lijst), min(invoer_lijst)
print(meervoudig())
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie())
