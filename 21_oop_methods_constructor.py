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
print('The method Car is in fact a constructor. However this will be discussed later.')
fiat = Car()
print('Now check the class of the car')
print('type(fiat)): ', type(fiat))
print('We may call a method use_horn by fiat.use_horn()')
fiat.use_horn()


print('\nWe may create various classes in our programs. Let\'s create a class Rectangle.')
print('All rectangles have length and width. This will be our fields (variables of the object).')
print('This time we will define a constructor method (__init__).')
print('It is convenient because we want to establish length and width as we create object.')
print('All fields should be initiated in the constructor.')
print('\nNotice that constructor has two arguments (length and width).')
print('These are used to set values of fields (self.length and self.width).')
print('Let\'s define a method that calculate an area of our rectangle.')
print('Notice that we do not have to pass any arguments to the method.')
print('This is because an object itself will have an access to its fields.')


class Rectangle:
    def __init__(self, length, width):
        print('Creating an object of class Rectangle.')
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


print('\nWe create an object by calling constructor and passing required arguments')
my_rectangle = Rectangle(2, 3)
print('Notice we do not write __init__ when we create an object.')
print('We may access fields by <name_of_object>.<name_of_field>')
print('my_rectangle.length: ', my_rectangle.length)
print('Similarly we may call a method.')
print('area: ', my_rectangle.calculate_area())
