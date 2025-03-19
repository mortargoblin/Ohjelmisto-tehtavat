# kilpailu.py
from random import randint

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

autot = []
for i in range(10):
    uusi_auto = Auto(f"ABC-{i+1}", randint(100, 200))
    autot.append(uusi_auto)

# Kilpailu alkaa
maali_saavutettu = False
while maali_saavutettu == False:
    for auto in autot:
        auto.kiihdytä(randint(-15,15))
        auto.kulje(1)
        if auto.kulj_matka >= 10000:
            maali_saavutettu = True

# Selkeä taulukko:
print(f"""+-----------+--------------+------------------+
| Rekkari   | Huippunopeus | Kuljettu matka   |""")
for auto in autot:
    print(f"""+-----------+--------------+------------------+
| {auto.rekkari.ljust(6)}    | {auto.huip_nopeus}          | {(str(auto.kulj_matka)+"km").ljust(17)}|""")