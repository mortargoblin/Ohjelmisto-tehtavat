# Nimiä

def main():
    print("Kirjoita nimiä")
    nimet = set()
    while True:
        set_len = len(nimet)
        user_input = input("> ").title()
        if user_input == "":
            break
        else:
            nimet.add(user_input)
            # Tässä uniikki ratkaisu
            if len(nimet) > set_len:
                print("Uusi nimi")
            else:
                print("Aiemmin syötetty nimi")
    for nimi in nimet:
        print(nimi, end=", ")
    
main()