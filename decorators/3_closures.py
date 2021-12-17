# As you already know we may define functions inside, of the other functions.
# These functions have access to variables defined in the body of outer function.
def outer_function():
    print("The outer_function has been called")
    x = 2

    def inner_function():
        print(f"The inner_function has access to x = {x}")

    return inner_function()


outer_function()  # The inner_function has access to x = 2


# Instead of calling inner_function, the outer_function may return the reference to inner_function.
def outer_function(some_variable):
    def inner_function(other_variable):
        print(f"The inner_function called with some_variable={some_variable} and other_variable={other_variable}")

    return inner_function


# As a result, we may call the outer function and pass its argument once. This will give us a new function with
# a different argument. The argument of the outer function is remembered by the new_function.
new_function = outer_function("constant")
new_function("variable value 1")
new_function("variable value 2")

# The mechanism where the inner function has access to a variable of the outer function and the inner function is
# returned by the outer function is called a closure. Sometimes using a closure may be a better solution instead of
# creating a global variable and more convenient instead of the implementation of a class.

# The value that are enclosed in the new_function may be accessed with:
print(new_function.__closure__[0].cell_contents)
