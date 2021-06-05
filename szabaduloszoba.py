import sys
vankard = False
vanbalta = False
vangyufa = False
vanfa = False
evett = False
indul = False
tavolsag = 3
evesproba = 0

print("""Kedves utazó!
Egy szabadulószobába fogsz érkezni pillanatok múlva. Van néhány tippem számodra:
    ¤ Ha kapsz információt, írd fel magadnak!
    ¤ Lehetnek csapdák, figyelj tetteid következményére!
    ¤ A végső lakatot maximum háromszor próbálhatod kinyitni, ha nem sikerül, vesztettél.
Ahol tárgyat szereztél meg, abba a szobába ne menj vissza, még nem csináltam meg, hogy ne lehessen újra felvenni.""")

while not indul == True:
    valasz = input("Mehet? (igen/nem)\n")
    if valasz == "igen":
        indul = True
    else:
         if valasz == "nem":
             sys.exit()



print("""___________________________________________________________________________________________________________

... Fáradt és éhes vagy. A sok harc és feladvány teljesen kimerített. Szörnyek követnek és tudod, hogy nem sok időd maradt hátra. Gyorsan 
ki kell jutnod innen. Elérkezel egy teremhez. A falak mentén 9 ajtó sorakozik. Egy táblát találsz a szoba közepén:
                         _______________________
                        | Az utolsó küldetés.   |
                        | Ez után szabadság vár.|
                        | Sok sikert.           |
                        |_______________________|
""")

while True:
    szobaszam = int(input("Melyik ajtón szeretnél bemenni? (1-9)\n"))



    if szobaszam == 1:
        print("Egy hideg, kissé nedves terembe érsz. Egy nagy szobrot látsz, aminek gyémánt szemei vannak.")
        valasz = input("Elveszed az ékköveket? (igen/nem)\n")
        if valasz == "igen":
            print("""Amint elveszed az első gyémántot, három szörny támad rád. Éles fogaikat csak úgy csikorgatják, ahogy egyre közelebb érnek hozzád.""")
            if vankard == True:
                print("""Mivel megszerezted a kardot, könnyedén elbánsz velük. Ez már semmi azokhoz képest amiket átéltél eddig.
Egyszercsak egy boszorkány mászik elő a falból. Egy gyufásdobozt ad a kezedbe.
- Amiért legyőzted őket. - mondja, majd köddé válik.""")
                vangyufa = True
            else:
                print("""Semmid nincs amivel védekezni tudnál. A szörnyek elkapnak és elsötétül a világ.
                Vesztettél.""")
                sys.exit()
        elif valasz == "nem":
            print("""Legyőzöd kapzsiságodat és otthagyod a gyémántokat. Épp lépnél ki az ajtón, amikor egy boszorkány mászik elő a falból. Egy gyufásdobozt ad a kezedbe.
- Az önuralmadért - mondja, majd köddé válik.""")
            vangyufa = True




    if szobaszam == 2:
        print("""Ahogy benyitsz, meglátod a feladványt. Az egész padlót homok borítja és mintha egy bottal írtak volna bele.
        ¤ + $ + $ = 28
        ¤ + ¤ + ¤ = 36
        $ - # = #
        ¤ + $ + # = ?""")




    if szobaszam == 3:
        print("""Egy nagyon különös terembe érsz. A falak olyan messze vannak, hogy a gyenge ködtől ami beborítja az egész helyet nem is lehet látni őket.
A szoba közepén egy fa áll.""")
        if vanbalta == True:
            print("A baltád tökéletes a fa kivágására. Nekiesel és hamar készen is vagy. Kis darabokra hasítod a rönköt és elrakod a táskádba.")
            vanfa = True
        else:
            print("Nem tudsz semmit kezdeni vele.")



    if szobaszam == 4:
        print("""Az ajtó mögött egy mégnagyobb kapu vár rád. Mellete egy tábla van, belevésve ez a mondat:
         ________________________________________
        | A továbbjutáshoz 2 kérdést kell        |
        | megválaszolnod. Ez a végső feladvány   |
        |________________________________________|""")
        valasz = input("Szeretnéd feloldani a lakatot? (igen/nem)\n")
        if valasz == "nem":
            print("Talán legközelebb.")
        elif valasz == "igen":
            if evett == False:
                print("Megpróbálnád feloldani a lakatot, de túl éhes vagy. Szerezned kell enni, így nem tudsz gondolkodni.")
                if tavolsag == 3:
                    print("A szörnyek akik követnek, egyre közelebb érnek. Már érzed lábaik dobogását. Sietned kell.")
                    tavolsag -= 1
                elif tavolsag == 2:
                    print("A téget követő szörnyeknek meghallod a lihegését. Tudod, hogy mindjárt ideérnek.")
                    tavolsag -= 1
                else:
                    print("""A szörnyek utolértek. 5 lény vetődik rád egyszerre. Esélyed sincs ellenük.
                    Vesztettél""")
                    sys.exit()
            else:
                print("""Megpróbálkozol a feladattal. A falon lévő táblan megjelenik az első kérdés:
                 ______________________
                | Számolásod eredménye |
                |______________________|""")
                valasz = input("Egy könyv jelenik meg előtted egy tollal. A válaszod: \n")
                if valasz == "24":
                    print("""Egy hangos csengő hangot hallassz. A válaszod helyes. A következő, egyben utolsó kérdés belevésődik a táblába:
                     _______________
                    | 'Szavak' sora |
                    |_______________|""")
                    valasz = input("A válaszod: (vesszőkkel és szóközzel elválasztva pl: alma, körte)\n")
                    if valasz == "aaghnr, abék, eékkr":
                        print("""Mégegy csilingelést hallassz és a lakat leszakad a kapuról. Kinyílik előtted és végre meglátod a napfényt.
                              Kijutottál""")
                        sys.exit()
                    else:
                        print("Búgó hang hallatszik és megremeg a föld. Rossz a válasz.")
                        if tavolsag == 3:
                            print(
                                "A szörnyek akik követnek, egyre közelebb érnek. Már érzed lábaik dobogását. Sietned kell.")
                            tavolsag -= 1
                        elif tavolsag == 2:
                            print("A téget követő szörnyeknek meghallod a lihegését. Tudod, hogy mindjárt ideérnek.")
                            tavolsag -= 1
                        else:
                            print("""A szörnyek utolértek. 5 lény vetődik rád egyszerre. Esélyed sincs ellenük.
                            Vesztettél""")
                            sys.exit()
                else:
                    print("Egy búgó hang jön a messzeségből és megremeg a föld. A válasz helytelen.")
                    if tavolsag == 3:
                        print(
                            "A szörnyek akik követnek, egyre közelebb érnek. Már érzed lábaik dobogását. Sietned kell.")
                        tavolsag -= 1
                    elif tavolsag == 2:
                        print("A téget követő szörnyeknek meghallod a lihegését. Tudod, hogy mindjárt ideérnek.")
                        tavolsag -= 1
                    else:
                        print("""A szörnyek utolértek. 5 lény vetődik rád egyszerre. Esélyed sincs ellenük.
                        Vesztettél""")
                        sys.exit()




    if szobaszam == 5:
        print("""A szoba közepén egy tűzrakóhelyet találsz.""")
        if vanfa == True and vangyufa == True:
            print("Mindened megvan ahhoz, hogy egyél. Találsz egy húst a szoba sarkában. Tüzet gyújtasz, megsütöd a húst, majd megeszed.")
            evett = True
        else:
            if evesproba <1:
                print("Sajnos nincs elég alapanyagod a tűzrakáshoz. Nagyon éhes vagy, gyorsan össze kéne szedned a dolgokat.")
                evesproba += 1
            else:
                print("""Rájössz, hogy nem sikerült összeszedned a tűzrakáshoz szükséges dolgokat. Nem bírod tovább az éhséget és összeesel.
                Vesztettél""")
                sys.exit()




    if szobaszam == 6:
        print("Egy szikla van a terem közepén, benne egy karddal.")
        valasz = input("Elveszed a kardot? (igen/nem)\n")
        if valasz == "igen":
            print("Könnyedén kihúzod a kardot a helyéről. Biztos hasznos lesz még.")
            vankard = True
        else:
            print("Inkább otthagyod a kardot a helyén, ki tudja mi történne, ha hozzányúlnál?")




    if szobaszam == 7:
        print("Egy szűk folyosóra érsz. A végére sétálsz és találsz egy baltát.")
        vanbalta = True




    if szobaszam == 8:
        print("""Ebben a teremben egy nagy táblát találsz.
         _____________________
        | harang, béka, kerék |
        |_____________________|""")


    if szobaszam == 9:
        print("""Egy nagy táblára ez van írva:
          _____________
         | alma = aalm |
         |_____________|""")
