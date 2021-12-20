# To create an iterator object we have to implement __iter__ and __next__ methods. The example is shown below:

class MyIterator:
    def __init__(self, limit):
        # The limit has been introduced to finish iterations.
        self.limit = limit

    def __iter__(self):
        # The iter method sets the initial conditions.
        self.current_iteration = 0
        return self

    def __next__(self):
        if self.current_iteration < self.limit:
            # If the limit is not exceeded, you may define what should be returned by the next method.
            self.current_iteration += 1
            return self.current_iteration
        else:
            # Otherwise, raise StopIteration to stop iterations.
            raise StopIteration


# Now create all necessary objects and iterate by using the method __next__.
my_iterable = MyIterator(3)
my_iterator = iter(my_iterable)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
# print(next(my_iterator))  # StopIteration

# Or simply use a loop:
for i in MyIterator(4):
    print("*" * i)
