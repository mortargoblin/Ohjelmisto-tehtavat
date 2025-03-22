# palohaly.py

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
        print(self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros)

class Talo:
    hissit_lst = []
    def __init__(self, alin, ylin, hissit_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit_lkm = hissit_lkm
        
        for i in range(hissit_lkm):
            self.hissit_lst.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, hissi, kohde):
        self.hissit_lst[hissi-1].siirry_kerrokseen(kohde)

    def palohalytys(self):
        print("Palohalytys")
        for hissi in self.hissit_lst:
            hissi.siirry_kerrokseen(self.alin)

# Pääohjelma

t = Talo(0, 6, 3)

t.aja_hissia(1, 4)

index = 1
for hissi in Talo.hissit_lst:
    print(f"Hissi {index} - kerros: {hissi.kerros}")
    index += 1

t.palohalytys()

for hissi in Talo.hissit_lst:
    print(f"Hissi {index} - kerros: {hissi.kerros}")
    index += 1

