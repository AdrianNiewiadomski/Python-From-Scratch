# In Python, a function is an object. Therefore, it may be returned by another function
# Let us define two functions.
def some_function():
    print("some_function has been called.")
    # Do something


def other_function():
    print("other_function has been called.")
    # Do something else
    return some_function


# As you can see the second function is returning a reference to the first function.
# We may call the first function.
some_function()  # some_function has been called.
# As well as the second function.
other_function()  # other_function has been called.
# However, in the second case, the first function has not been called.
# To call the first function you may use the following.
reference_to_some_function = other_function()
reference_to_some_function()


# The returned function may be defined either outside or inside, of the returning function.
def outer_function():
    print("The outer_function has been called")

    def inner_function():
        print("The inner_function has been called")

    return inner_function


# The function defined inside another function is sometimes called a nested function.
# An external function is also called an enclosing function.
# To call inner function we must do the following:
reference_to_inner_function = outer_function()
reference_to_inner_function()
