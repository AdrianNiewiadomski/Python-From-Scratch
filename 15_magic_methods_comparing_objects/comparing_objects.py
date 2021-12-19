# Let's say that you want to compare cars (or any other objects).
class Car:
    def __init__(self, car_brand: str, engine_capacity: float, color: str):
        self.car_brand = car_brand
        self.engine_capacity = engine_capacity
        self.color = color

    # To do that, you have to tell the Python how to compare objects.
    # You do that, by defining a method called eq.
    def __eq__(self, other):

        # If both instances belong to the same class, then you may compare their fields.
        if isinstance(self, other.__class__):
            # Let's say that you care about a brand and capacity but do not care about the color.
            # Therefore, write the following:
            return self.car_brand == other.car_brand and self.engine_capacity == other.engine_capacity

        else:
            # If the instances are not of the same class the objects are not equal.
            return False


# Now, let's add another simple class.
class Bicycle:
    def __init__(self, color):
        self.color = color


if __name__ == "__main__":
    # Now let assume that you have a 2 bikes and 3 cars.
    bike = Bicycle("blue")
    bike2 = Bicycle("blue")
    toyota = Car("Toyota", 1.8, "grey")
    mc1 = Car("Mercedes", 1.8, "grey")
    mc2 = Car("Mercedes", 1.8, "red")

    # Everyone knows that a bicycle is not a car ;)
    print("Q: Is a bike a car? A:", bike == toyota)
    # And of course, a car is not a number.
    print("Q: Is car a number? A:", toyota == 1)

    # Let us compare cars!
    print("Q: Does Toyota have the same brand as Mercedes? A:", toyota == mc1)
    print("Q: Do you remember that we don't care about color? A:", mc1 == mc2)

    # Since an eq method has not been defined for class Bicycle, the Python cannot compare bikes!
    print("Q: Can I compare bikes? A:", bike == bike2)
