# auto.py

class Auto:
    def __init__(self, rekkari, huip_nopeus, nyk_nopeus=0, kulj_matka=0):
        self.rekkari = rekkari
        self.huip_nopeus = huip_nopeus
        self.nyk_nopeus = nyk_nopeus
        self.kulj_matka = kulj_matka

fiat_punto = Auto("ABC-123", 142)
print(f"Rekkari: {fiat_punto.rekkari}\nHuippunopeus: {fiat_punto.huip_nopeus}kmh")