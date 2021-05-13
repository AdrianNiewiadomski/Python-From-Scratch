# Lets say we have a class circle.

class Circle:
    def __init__(self):
        print('Creating an object of class Rectangle.')
        self.radius = 0

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


# This way the user may abuse this class and may not realize.
my_circle = Circle()
my_circle.radius = -3
print('The area of circle is: ', my_circle.calculate_area())


class BetterCircle:
    def __init__(self):
        print('Creating an object of class Rectangle.')
        self._radius = 0

    def set_radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise E

    def calculate_area(self):
        return 3.14 * self.radius * self.radius