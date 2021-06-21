print("If you define a function, it turns out that it is an object of a class function.")


def print_hello():
    print("Hello World!")


print("type(print_hello): ", type(print_hello))
print("\nThe name of the function is in fact a variable storing a reference to the function.")
print("Therefore, like any other variable, the reference to function may be passed to another function as an argument:")


def my_function(func):
    print("******************************************")
    func()
    print("******************************************")


print("\nAnd the function may be called with my_function(print_hello):")
my_function(print_hello)
