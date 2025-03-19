# auto.py

class Auto:
    def __init__(self, rekkari, huip_nopeus, nyk_nopeus=0, kulj_matka=0):
        self.rekkari = rekkari
        self.huip_nopeus = huip_nopeus
        self.nyk_nopeus = nyk_nopeus
        self.kulj_matka = kulj_matka

    def kiihdytä(self, muutos_nopeus):
        self.nyk_nopeus += muutos_nopeus
        if not self.nyk_nopeus <= self.huip_nopeus:
            self.nyk_nopeus = self.huip_nopeus
        elif self.nyk_nopeus <= 0:
            self.nyk_nopeus = 0

def ajelu(auto, kiihdytys):
    # Kiihdytys
    for kiihdytys in kiihdytys:
        auto.kiihdytä(kiihdytys)
    print(auto.nyk_nopeus)
    # Hätäjarrutus
    auto.kiihdytä(-200)
    print(auto.nyk_nopeus)

fiat_punto = Auto("ABC-123", 142)
ajelu(fiat_punto, (30, 70, 50))