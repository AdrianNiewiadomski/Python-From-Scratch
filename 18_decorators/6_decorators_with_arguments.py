def decorate(func):
    def inner_function(msg):
        print("*******************")
        func(msg)
    return inner_function


@decorate
def print_message(msg):
    print(msg)


print_message("Resource not found!")


print("\n")
# del print_message
# del decorate
# Now let's say we want to change from stars to strings like INFO, WARNING, or
# ERROR: before our message. To do this we have to pass an argument to the
# decorator. We can do this in two ways.
# 1. Either change the number of arguments of the inner function:


def decorate(func):
    def inner_function(msg, prefix):
        print(prefix, end="")
        func(msg)
    return inner_function


@decorate
def print_message(msg):
    print(msg)


# But then you have to pass an additional argument to the decorated function.
print_message("Resource not found!", "ERROR: ")


# or 2. Create the following decorator.


def add_prefix(prefix):
    def new_decorate(func):
        def inner_function(msg):
            print(prefix, end="")
            func(msg)
        return inner_function
    return new_decorate


@add_prefix("ERROR: ")
def print_message(msg):
    print(msg)


print_message("Resource not found!")
