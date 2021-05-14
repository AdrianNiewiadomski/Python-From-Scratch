# Lets say we have a class circle.

class Circle:
    def __init__(self):
        print('Creating an object of class Rectangle.')
        self.radius = 0

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


# This way the user may abuse this class and may not even realize it.
my_circle = Circle()
my_circle.radius = -3
print('The area of circle is: ', my_circle.calculate_area())


class BetterCircle:
    def __init__(self):
        print('Creating an object of class Rectangle.')
        # Below we created a radius field with value None. Notice the _ sign.
        # This means that field radius is a protected field of the class.
        # Therefore it should only be accessed by the methods of the class.
        self._radius = None

    # Because radius is now protected field of the class, the user (i.e. another developer)
    # will expect that creator of this class created a method to access this field to set its value.
    def set_radius(self, radius):
        # This allows the new value of field to be validated before any action.
        if radius >= 0:
            self._radius = radius
        else:
            # If the value does not conform some requirements, the field is not set.
            print(f'an invalid radius value ({radius}) was specified!')
            # The author of the script may event raise an exception to stop the script from further execution.
            # raise ValueError(f'an invalid radius value ({radius}) was specified!')

    def calculate_area(self):
        return 3.14 * self._radius * self._radius


my_circle = BetterCircle()
# Other developer will try to access the value of protected field.
# my_circle._radius = -3

# Instead he/she will try to access it using a method
my_circle.set_radius(-3)
# The line above will print a warning and will not set the value of the field.
# The lines below will set the value and perform calculation.
my_circle.set_radius(1)
print(my_circle.calculate_area())

# Similar strategy may be used for getting the values of the fields.
# The mechanism of restricting direct access to the data and allowing the access through the methods
# is called encapsulation.
# Methods that allow to get and set value of the fields are getters and setters.
