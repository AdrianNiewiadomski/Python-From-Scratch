# Data structures like lists allow storing multiple items.
# A list may be created like this:
my_list = []
print("my_list: ", my_list)

# Or, you can create it with stored values:
my_list = ["item 1", "item 2", "item 3"]
print("my_list: ", my_list)

# You may access an element of list with the following line:
print("my_list[0]: ", my_list[0])

# Since all items stored in our list are strings, you can access letters with:
print("my_list[0][0]: ", my_list[0][0])

# A list can be sliced
print("my_list[:2]: ", my_list[:2])

# Lists are mutable, this means that once created a list may be changed.
my_list[0] = "item 4"
print("\nmy_list with changed item: ", my_list)

# However an attempt to add an item to list:
# my_list[3] = "item 4"
# will result in an IndexError with the message: list assignment index out of range
# To add an additional item to list you have to use a method append

# The variable my_list stores a reference to an object
my_list2 = my_list
print("\nmy_list: ", my_list)
print("my_list2: ", my_list2)

my_list[0] = "A new item"
print("my_list after changing first item: ", my_list)
print("my_list2: ", my_list2)
# To copy values instead of reference to a new variable you may use a method copy.

# Unlike in C++ or in Java a list may store data of different types
my_list = [1, 2.5, "item"]
print("\nmy_list: ", my_list)

# A list may contain other data structures like lists, dictionaries etc.
li1 = [0, 1, 2]
li2 = [3, 4, 5]
li3 = [6, 7, 8]
li = [li1, li2, li3]
print("li: ", li)
print("A length of this list is: ", len(li))

# List may hold non-unique values:
my_list = [1, 1, 1]
print("\nMy non-unique list: ", my_list)
