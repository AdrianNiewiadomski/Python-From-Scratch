print('Let\'s create a list by declaring a variable: ')

my_list = [1, 2, 3]
print('my_list:', my_list)
print('It turns out we\'ve created an instance of class called list')
print('You may check this out by typing type(my_list). This returns: ')
print(type(my_list))

print('\nAn object is a data type with a state (a group of variables) '
      'and methods (functions) that this object may perform.')
print('For instance we may call a method append. This will result in adding an element to list.')
my_list.append(4)
print('my_list:', my_list)

print('\nWe may create our own objects after defining our class.')
print('Defining is done with a keyword class.')
print('The class name should start with a capital letter.')
print('A class called Car has been defined below.')


class Car:
    def use_horn(self):
        print("beep beep!")


print('\nAs you can see, the method (use_horn) is quite similar to functions that we get to know earlier.')
print('The only visible difference is that it has an argument called self.')
print('The function does not really uses it so PyCharm suggests to change it into a static method.')
print('This however will be left to for another lesson.')

print('\nAs it was mentioned before the object has its variables.')
print('If you want to reference the object that you are working on simply use self.')
print('You may access variables that belong to particular object with use of self.')
print('self is usually a first argument of all methods that are declared.')


print('\nWe may now instantiate an object of class Car by calling a method Car.')
fiat = Car()
print('Now check the class of the car')
print('type(fiat)): ', type(fiat))
print('We may call a method use_horn by fiat.use_horn()')
fiat.use_horn()




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



