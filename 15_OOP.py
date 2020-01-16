#definicja klasy i jej metod
class Auto:
    def zatrab(self):
        print("pip pip!")

#tworzymy obiekt klasy auto
fiat = Auto()
#wywołujemy metodę obiektu fiat
fiat.zatrab()


class Prostokat:
    
    #konstruktor - funkcja tworzaca obiekt
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def wyznacz_pole(self):
        print("pole = ", self.a * self.b)

    def wyznacz_obwod(self):
        print("obwod = ", 2*(self.a + self.b))

prostokacik = Prostokat(2,3)
prostokacik.wyznacz_obwod()
prostokacik.wyznacz_pole()