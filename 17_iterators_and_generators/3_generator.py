# An easier way to create an iterator is by creating a function containing a keyword yield.

def create_generator(limit):
    for j in range(limit):
        yield j + 1


# This looks like an ordinary function, but it turns out that by calling the function we get a generator object.
print(type(create_generator))  # <class 'function'>
my_generator = create_generator(3)
print(type(my_generator))  # <class 'generator'>

# Now, we can proceed with it as before with the iterator object.
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator))  # StopIteration

# This also works for loops.
for i in create_generator(4):
    print(i)


# One should notice that keyword yield differs significantly from the return keyword. The return keyword terminates the
# function and all its variables are lost. On the other hand, the yield keyword saves the state of function and gives
# back control outside the function. When the method next is called, the function continues from the state where the
# yield was called.
# A function can have multiple yield and return keywords. However, at least one yield keyword is needed to create a
# generator.

# A generator may also be created with generator expression:
generator = (-x for x in range(4))
for k in generator:
    print(k)
