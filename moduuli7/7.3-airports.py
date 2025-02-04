# Airport data

def main():
    airports = {"EFHK": "Helsinki-Vantaa Airport"}
    while True:
        print("Lisää uusi lentokenttä [L] tai hae olemassaoleva [H]. Kirjoita [Q] poistuaksesi")
        valinta = input("> ")
        if valinta.upper() == "L":
            #Lisää
            print("Lisää lentokentän ICAO-Koodi")
            uusi_icao = input("> ").upper()
            print("Lisää lentokentän nimi")
            uusi_nimi = input("> ")
            airports.update({uusi_icao: uusi_nimi})
        elif valinta.upper() == "H":
            #Hae
            print("Kirjoita haettavan lentokentän ICAO-koodi")
            haettava_icao = input("> ").upper()
            if haettava_icao in airports:
                print(airports[haettava_icao])
            else: print("ICAO ei tuttu")
        elif valinta.upper() == "Q":
            break
        else:
            print("Valinta ei 'L', 'H' tai 'Q'")

main()