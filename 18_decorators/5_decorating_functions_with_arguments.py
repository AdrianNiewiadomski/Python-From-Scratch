# Let's say we want a method to add costs in our company. Therefore, we write a simple function that adds two costs.
# And we add the functionality of validation of costs to it with a decorator.
def validate_costs(func):
    def inner_function(cost1, cost2):
        if cost1 < 0 or cost2 < 0:
            print("Costs cannot be negative!")
            return
        else:
            return func(cost1, cost2)

    return inner_function


@validate_costs
def add_costs(cost1, cost2):
    print(cost1 + cost2)


# We can check that this works with the following:
add_costs(2, 3)  # 5
add_costs(2, -1)  # Costs cannot be negative!


# However, this is inconvenient since the number of arguments of the decorated function must match the number of
# arguments of the inner function. This may be solved with args:


def validate_costs(func):
    def inner_function(*args):
        if any(arg < 0 for arg in args):
            print("Costs cannot be negative!")
            return
        else:
            return func(args)

    return inner_function


@validate_costs
def add_costs(args):
    print(sum(args))


add_costs(1, 2)
add_costs(1, 2, 3)
add_costs(2, -3)
