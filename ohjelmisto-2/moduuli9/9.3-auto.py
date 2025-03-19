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

    def kulje(self, tunnit):
        self.kulj_matka += self.nyk_nopeus * tunnit

def ajelu(auto, kiihdytykset):
    # Kiihdytys
    for kiihdytys in kiihdytykset:
        auto.kiihdytä(kiihdytys)
        auto.kulje(1)
    print("Nykyinen nopeus:", auto.nyk_nopeus, "km")
    # Hätäjarrutus
    auto.kiihdytä(-200)
    print("Hätäjarrutus!")
    print("Nykyinen nopeus:",auto.nyk_nopeus, "km")
    print("Kuljettu matka:", auto.kulj_matka, "km")

fiat_punto = Auto("ABC-123", 142)
ajelu(fiat_punto, (30, 70, 50))