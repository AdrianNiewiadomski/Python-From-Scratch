# Let's say that we have a simple class
class MySimpleClass:
    def __init__(self):
        self.some_field = "a"
        self.some_other_field = "b"

# As presented below, an attempt to print the object of this class will not end up with satisfactory result.
# However, this situation may change if we add a __str__ method to our class.


class MyBetterClass:
    def __init__(self):
        self.some_field = "a"
        self.some_other_field = "b"

    def __str__(self):
        return str({"some_field": self.some_field, "some_other_field": self.some_other_field})


if __name__ == '__main__':
    my_simple_object = MySimpleClass()
    # This will print my_simple_object:  <__main__.MySimpleClass object at 0x7f1260072240>
    print("my_simple_object: ", my_simple_object)

    my_better_object = MyBetterClass()
    # The line below will result in the following output to console:
    # my_better_object: {'some_field': 'a', 'some_other_field': 'b'}
    print("my_better_object: ", my_better_object)

    # The __str__ method is called when you try to get a string representation of an object:
    my_string = str(my_better_object)
    print("my_string: ", my_string)

