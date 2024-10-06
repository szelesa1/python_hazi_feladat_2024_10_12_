"""
# 7.    Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!

def hetedik_feladat():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat - 1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat + 1, 1):
            print(i, end=" ")
"""

# 8.    Írd meg a fenti feladatot while és for ciklussal is!

def nyolcadik_feladat():
    szam1 = int(input("Kérlek, add meg az első számot: "))
    szam2 = int(input("Kérlek, add meg a második számot: "))
    szorzat = szam1 * szam2

    # Kiinduló érték.
    i = 0

    # Ha a szorzat negatív:
    if szorzat < 0:
        while i >= szorzat:
            print(i, end=" ")
            i -= 1 # Lépjünk visszafelé!

    # Ha a szorzat pozitív:
    else:
        while i <= szorzat:
            print(i, end=" ")
            i += 1  # Lépjünk előre!

    print() # Új sor a kiírás végén.

# 9.	Írasd ki az első 7 pozitív egész számot vesszővel elválasztva!

def kilencedik_feladat():
    for i in range(1, 8):
        print(i, end=", ")

# 9/a.	úgy, hogy a végén ne legyen vessző!

def kilencedik_a_feladat():
    for i in range(1, 8):
        if i < 7:
            print(i, end=", ")
        else:
            print(i)

# 11.	Írasd ki 2 bekért szám (x és y) alapján, hogy mennyi 3x+y2!

def tizenegyedik_feladat():
    x = int(input("Add meg az x értékét: "))
    y = int(input("Add meg az y értékét: "))
    eredmeny = 3 * x + y ** 2
    print(eredmeny)

# 12.	Számold meg 2 bekért szám közötti páros számokat! (pl. hány db páros szám van 4 és 31 között?)

def tizenkettedik_feladat():
    szam1 = int(input("Add meg az első számot: "))
    szam2 = int(input("Add meg a második számot: "))
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    paros_szamok = 0

    for i in range(szam1, szam2 + 1):
        if i % 2 == 0:  # Ha a szám páros
            paros_szamok += 1

    print("A két szám között " + str(paros_szamok) + " darab páros szám található.")
