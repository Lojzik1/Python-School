class Produkt:
    def __init__(self, nazev):
        self.nazev = nazev

class Pocitac(Produkt):
    def __init__(self, nazev, processor, ram):
        super().__init__(nazev)
        self.ram = ram
        self.processor = processor

class Monitor(Produkt):
    def __init__(self, nazev, uhlopricka, rozliseni):
        super().__init__(nazev)
        self.uhlopricka = uhlopricka
        self.rozliseni = rozliseni

class Klavesnice(Produkt):
    def __init__(self, nazev, typ):
        super().__init__(nazev)
        self.typ = typ

class Mys(Produkt):
    def __init__(self, nazev, typ):
        super().__init__(nazev)
        self.typ = typ

class Factory:
    def __init__(self):
        self.vyrobeno = []

    def vyrob_pocitac(self, nazev, processor, ram):
        pocitac = Pocitac(nazev, processor, ram)
        self.vyrobeno.append(pocitac)
        return pocitac
    
    def vyrob_monitor(self, nazev, uhlopricka, rozliseni):
        monitor = Monitor(nazev, uhlopricka, rozliseni)
        self.vyrobeno.append(monitor)
        return monitor
    
    def vyrob_klavesnice(self, nazev, typ):
        klavesnice = Klavesnice(nazev,typ)
        self.vyrobeno.append(klavesnice)
        return klavesnice
    
    def vyrob_mys(self, nazev, typ):
        mys = Mys(nazev, typ)
        self.vyrobeno.append(mys)
        return mys
    
factory = Factory()

pocitac = factory.vyrob_pocitac("HP", "AMD Ryzen 7", "32GB")
print(f"PC: {pocitac.nazev}\nProcessor: {pocitac.processor}\nRAM: {pocitac.ram}\n")

monitor = factory.vyrob_monitor("Samsung", "27 palců", "1920x1080")
print(f"Monitor: {monitor.nazev}\nÚhlopříčka: {monitor.uhlopricka}\nRozlišení: {monitor.rozliseni}\n")

klavesnice = factory.vyrob_klavesnice("HyperX", "Mechanická")
print(f"Klávesnice: {klavesnice.nazev}\nTyp: {klavesnice.typ}\n")

mys = factory.vyrob_mys("Logitech", "Bezdrátová")
print(f"Myš: {mys.nazev}\nTyp: {mys.typ}\n")
