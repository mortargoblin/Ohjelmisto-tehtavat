# Auto.py
from random import randint

def main():
    tesla = Sahkoauto("ABC-15", 180, 52.5)
    ford = Polttoauto("ACD-123", 165, 32.3)
    for _ in range(3):
        for auto in (tesla, ford):
            auto.kiihdyta(randint(-15,15))
            auto.kulje()
    for auto in (tesla, ford):
        print(f"{auto.rekkari}: {auto.kulj_matka}km")

class Auto:
    def __init__(self, rekkari, huip_nopeus):
        self.rekkari = rekkari
        self.huip_nopeus = huip_nopeus
        self.nyk_nopeus = 50
        self.kulj_matka = 0

    def kiihdyta(self, muutos_nopeus):
        self.nyk_nopeus += muutos_nopeus
        if not self.nyk_nopeus <= self.huip_nopeus:
            self.nyk_nopeus = self.huip_nopeus
        elif self.nyk_nopeus <= 0:
            self.nyk_nopeus = 0

    def kulje(self, tunnit=1):
        self.kulj_matka += self.nyk_nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekkari, huip_nopeus, akkukap):
        self.akkukap = akkukap
        super().__init__(rekkari, huip_nopeus)

class Polttoauto(Auto):
    def __init__(self, rekkari, huip_nopeus, tankki):
        self.tankki = tankki
        super().__init__(rekkari, huip_nopeus)


main()
