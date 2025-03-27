# Kirja.py

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja: {self.kirjoittaja}")
        print(f"sivumäärä: {self.sivumaara}")
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja: {self.paatoimittaja}")

akkari = Lehti("Aku Ankka", "Aki Hyyppiä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

akkari.tulosta_tiedot()
hytti.tulosta_tiedot()
