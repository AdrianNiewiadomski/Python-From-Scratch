#Mamy obiekt listy
my_list = [1,2,3]
#wywołujemy jego metodę
my_list.append(4)
print("my_list = ",my_list)
#jest to obiekt należący do klasy list
print(type(my_list))




#Możemy też tworzyć własne obiekty
#definicja klasy i jej metod
class Auto:
    def zatrab(self):
        # Każdy obiekt jest widziany sam przez siebie pod nazwą self.
        # Nazwy tej używa się wewnątrz klasy w tych miejscach,
        # w których potrzebne jest odwołanie obiektu do niego samego.
        # Nazwa self winna być pierwszym argumentem wszystkich deklarowanych metod.
        # W wywołanej metodzie reprezentuje ona aktualnie użyty obiekt.
        print("pip pip!")

#tworzymy obiekt klasy auto
fiat = Auto()
print(type(fiat))
#wywołujemy metodę obiektu fiat
fiat.zatrab()




#Klasy mogą być bardzo różne:
class Prostokat:

    #konstruktor - funkcja tworzaca obiekt
    def __init__(self, a, b):
        print(f"tworze obiekt klasy Prostokat o polach a={a} i b={b}")
        self.a = a
        self.b = b

    def wyznacz_pole(self):
        print("pole = ", self.a * self.b)

    def wyznacz_obwod(self):
        print("obwod = ", 2*(self.a + self.b))

#tworzymy obiekt klasy Prostokat (wywolujemy konstruktor)
prostokacik = Prostokat(2,3)
#zmienne należące do obiektów to pola lub inaczej atrybuty.
# Dostęp do pól możemy uzyskać przez:
print("prostokacik.a = ", prostokacik.a)
#wywolujemy metody prostokacika
prostokacik.wyznacz_obwod()
prostokacik.wyznacz_pole()



