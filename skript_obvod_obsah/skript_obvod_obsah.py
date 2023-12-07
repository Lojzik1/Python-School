import math

class Trojúhelník:

    def __init__(self, a=0, b=0, c=0):
        self.wall_a = a
        self.wall_b = b
        self.wall_c = c

    def obvod(self):
        return self.wall_a + self.wall_b + self.wall_c

    def obsah(self):
        h_a = float(input("Zadej výšku na stranu a (v cm): "))
        return 0.5 * self.wall_a * h_a

class Čtverec:

    def __init__(self, a=0):
        self.wall_a = a

    def obvod(self):
        return 4 * self.wall_a

    def obsah(self):
        return self.wall_a ** 2

class Obdelník:

    def __init__(self, a=0, b=0):
        self.wall_a = a
        self.wall_b = b

    def obvod(self):
        return 2 * (self.wall_a + self.wall_b)

    def obsah(self):
        return self.wall_a * self.wall_b
    
class Kruh:

    def __init__(self, r=0):
        self.radius = r

    def obvod(self):
        return 2 * math.pi * self.radius

    def obsah(self):
        return math.pi * self.radius ** 2

def main():
    tvar = input("Vyber tvar (trojúhelník/čtverec/obdelník/kruh): ")

    if tvar == "trojúhelník":
        a = float(input("Zadej délku strany a (v cm): "))
        b = float(input("Zadej délku strany b (v cm): "))
        c = float(input("Zadej délku strany c (v cm): "))

        volba = input("Co chcete vypočítat? (obvod/obsah)\n")

        trojuhelnik = Trojúhelník(a, b, c)

        if volba == "obvod":
            print("Obvod trojúhelníka:", trojuhelnik.obvod(), "cm")
        elif volba == "obsah":
            print("Obsah trojúhelníka:", trojuhelnik.obsah(), "cm^2")

    elif tvar == "čtverec":
        a = float(input("Zadej délku strany a (v cm): "))
        ctverec = Čtverec(a)
        volba = input("Co chcete vypočítat? (obvod/obsah)\n")

        if volba == "obvod":
            print("Obvod čtverce:", ctverec.obvod(), "cm")
        elif volba == "obsah":
            print("Obsah čtverce:", ctverec.obsah(), "cm^2")

    elif tvar == "obdelník":
        a = float(input("Zadej délku strany a (v cm): "))
        b = float(input("Zadej délku strany b (v cm): "))
        obdelnik = Obdelník(a, b)
        volba = input("Co chcete vypočítat? (obvod/obsah)\n")

        if volba == "obvod":
            print("Obvod obdelníku:", obdelnik.obvod(), "cm")
        elif volba == "obsah":
            print("Obsah obdelníku:", obdelnik.obsah(), "cm^2")

    elif tvar == "kruh":
        r = float(input("Zadej poloměr kruhu (v cm): "))
        kruh = Kruh(r)
        volba = input("Co chcete vypočítat? (obvod/obsah)\n")

        if volba == "obvod":
            print("Obvod kruhu:", kruh.obvod(), "cm")
        elif volba == "obsah":
            print("Obsah kruhu:", kruh.obsah(), "cm^2")

    else:
        print("Neplatný tvar.")

if __name__ == "__main__":
    main()
