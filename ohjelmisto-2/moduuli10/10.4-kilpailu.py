# kilpailu.py
from random import randint

class Auto:
    def __init__(self, rekkari, huip_nopeus, nyk_nopeus=0, kulj_matka=0):
        self.rekkari = rekkari
        self.huip_nopeus = huip_nopeus
        self.nyk_nopeus = nyk_nopeus
        self.kulj_matka = kulj_matka

    def kiihdyta(self, muutos_nopeus):
        self.nyk_nopeus += muutos_nopeus
        if not self.nyk_nopeus <= self.huip_nopeus:
            self.nyk_nopeus = self.huip_nopeus
        elif self.nyk_nopeus <= 0:
            self.nyk_nopeus = 0
        # Autot ovat aika hitaita sillä vain tunnin välein muutetaan
        # nopeutta +- 15 kmh ja autot alottavat nollasta...
        # Tämä johtaa myös valtavaan määrään tulostaulukkoja.
        # print(self.nyk_nopeus)

    def kulje(self, tunnit):
        self.kulj_matka += self.nyk_nopeus * tunnit

class Kilpailu:
    
    tunnit_kulunut = 0

    def __init__(self, nimi, pituus, auto_lst):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_lst = auto_lst

    def tunti_kuluu(self, tunnit=1):
        for auto in self.auto_lst:
            auto.kiihdyta(randint(-15,15))
            auto.kulje(tunnit)
            self.tunnit_kulunut += tunnit

    def tulosta_tilanne(self):
        auto_lst_sorted = sorted(self.auto_lst, key=lambda a: a.kulj_matka, reverse=True)
        print(f"""+-----------+--------------+------------------+
| Rekkari   | Huippunopeus | Kuljettu matka   |""")
        for auto in auto_lst_sorted:
            print(f"""+-----------+--------------+------------------+
| {auto.rekkari.ljust(6)}    | {auto.huip_nopeus}          | """
f"{(str(auto.kulj_matka)+"km").ljust(17)}|")
        print("+-----------+--------------+------------------+")

    def kilpailu_ohi(self):
        for auto in self.auto_lst:
            if auto.kulj_matka >= self.pituus:
                return True

# Pääohjelma

# Autot määritetään
autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", randint(100, 200)))

# Kilpailu
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while kilpailu.kilpailu_ohi() != True:
    kilpailu.tunti_kuluu()
    if kilpailu.tunnit_kulunut % 10 == 0:
        print("Tunnit kulunut:",kilpailu.tunnit_kulunut)
        kilpailu.tulosta_tilanne()

print(f"{kilpailu.nimi} \nlopputulos:")
kilpailu.tulosta_tilanne()

