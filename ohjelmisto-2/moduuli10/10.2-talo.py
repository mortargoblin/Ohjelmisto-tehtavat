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

class Talo:
    def __init__(self, alin, ylin, hissit_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit_lkm = hissit_lkm

    def aja_hissia(self, hissi, kohde):
        self.hissit_lst = []
        Hissi(self.alin, self.ylin).siirry_kerrokseen(kohde)

# Pääohjelma

t = Talo(0, 6, 3)

t.aja_hissia(1, 4)
