# Nimiä

def main():
    print("Syötä nimiä. Syötä tyhjä, kun valmiina")
    nimet = set()
    while True:
        set_len = len(nimet)
        user_input = input("> ").title()
        if user_input == "":
            break
        else:
            if user_input not in nimet:
                print("Uusi nimi")
                nimet.add(user_input)
            else:
                print("Aiemmin syötetty nimi")
    for nimi in nimet:
        print(nimi, end="  ")
    
main()