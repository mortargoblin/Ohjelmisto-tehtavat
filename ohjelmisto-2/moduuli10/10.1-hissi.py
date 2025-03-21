# Hissi.py

class Hissi:
    def __init__(self, alin, ylin, kerros=0):
        self.alin = alin
        self.ylin = ylin
        self.kerros = self.alin
    
    def siirry_kerrokseen(self, kohde):
        if kohde > self.kerros:
            for i in range(abs(kohde - self.kerros)):
                self.kerros_ylos()
        else:
            for i in range(abs(kohde - self.kerros)):
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1
        print(self.kerros, end=" ")

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros, end=" ")


# Pääohjelma

h = Hissi(0, 10)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(0)
