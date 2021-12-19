# We call an iterable object any object that implements an iterable interface. That is that it implements an __iter__
# and __next__ methods. The __iter__ method should return an iterator object. While a __next__ method returns the next
# element of an iterator. An iterator is an object that can be iterated over. A list is an iterable object. Let's say we
# have the following list.

my_iterable = [1, 2, 3]
print(type(my_iterable))  # <class 'list'>

# We may call its __iter__ method and get an iterator object.
my_iterator = iter(my_iterable)
print(type(my_iterator))  # <class 'list_iterator'>

# Now we may call the __next__ on the iterator object to get its next element.
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# Because our iterator has only three elements, the next attempt to call its __next__ method would raise a StopIteration
# print(next(my_iterator))  # StopIteration Exception

# Therefore, all attempts to use this method should be in try except block.
try:
    print(next(my_iterator))
except StopIteration:
    print("StopIteration Exception has been raised!")

# As you can probably guess, this is implemented in a for loop. For more information, look at
# https://www.programiz.com/python-programming/iterator
