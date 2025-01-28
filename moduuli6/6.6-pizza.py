# pizza price per surface unit calculator

from math import pi

def main():
    # halkaisija: cm, hinta: €
    print("Tämä ohjelma laskee pizzojen neliometrihinnat, vertaa")
    print("niitä keskenään, ja ilmoittaa kumpi pizza neliömetrihinnaltaan")
    print("edullisempi.")
    
    # pohdin tässä hetken että teenkö dictionaryn vai en..
    p1_halk = float(input("Pizza 1 halkaisija (cm): "))
    p1_hinta = float(input("Pizza 1 hinta (€): "))

    p2_halk = float(input("Pizza 2 halkaisija (cm): "))
    p2_hinta = float(input("Pizza 2 hinta (€): "))

    p1_price_per_m2 = pizza_price_calc(p1_halk, p1_hinta)
    p2_price_per_m2 = pizza_price_calc(p2_halk, p2_hinta)

    print(f"\nPizza 1 neliömetrihinta: {str(p1_price_per_m2)[0:5]} €/m²")
    print(f"Pizza 2 neliömetrihinta: {str(p2_price_per_m2)[0:5]} €/m²")
    if p1_price_per_m2 < p2_price_per_m2:
        print("Pizza 1 on halvempi per m²")
    elif p1_price_per_m2 == p2_price_per_m2:
        print("Pizzat ovat saman hintaisia per m²")
    else:
        print("Pizza 2 halvempi per m²")
    

def pizza_price_calc(halkaisija, hinta):
    # Ensiksi lasketaan pinta-ala
    pinta = ((pi / 4) * halkaisija**2) * 0.0001 # neliömetreinä
    return hinta / pinta

main()