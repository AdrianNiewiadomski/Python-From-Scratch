# As you already know a function can be passed as an argument and returned by another function.
# Furthermore, an inner function has access to variables defined in enclosing function.
# These may result in the following construction.
def outer_function(func):
    def inner_function():
        func()
        print("But I got decorated.")

    return inner_function


# Now lets take an ordinary function.
def ordinary_function():
    print("I am an ordinary function.")


# And create decorated function.
decorated_function = outer_function(ordinary_function)

# Calling decorated function will result in printing:
# I am an ordinary function.
# But I got decorated.
decorated_function()

# Notice that nothing stops us from giving the decorated function the same name as the original function:
ordinary_function = outer_function(ordinary_function)
ordinary_function()


# The same thing maybe achieved with the following:
@outer_function
def another_ordinary_function():
    print("I am another ordinary function.")


# Now we may call decorated another_ordinary_function with:
another_ordinary_function()

# So as you can see the phrase:
# @outer_function
# before definition of the function replaces the following:
# another_ordinary_function = outer_function(another_ordinary_function)

# To sum up, the decorator takes an existing function, adds some functionalities to it, and returns it.
