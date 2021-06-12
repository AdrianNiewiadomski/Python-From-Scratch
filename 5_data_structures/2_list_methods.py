# Let's create a list:
my_list = ["item 1", "item 2", "item 3"]

# When you check the type of my_list, you will see that it belongs to a class called list.
print("type(my_list): ", type(my_list))

# This class contains a number of functions that can be can be performed on a list.

# We already know a function called len, that returns a length of a list.
print("The length of my_list is: ", len(my_list))

# We can add an item to the list with the append method.
print("my_list: ", my_list)
my_list.append("item 4")
print("my_list after appending item 4: ", my_list)

# To append more items to the list you may use a method extend:
my_list.extend(["item 5", "item 6"])
print("my_list after extending with ['item 5', 'item 6']: ", my_list)

# To insert item before given index use a method insert.
# 3 examples are presented below.
my_list = ["item 1", "item 2", "item 3"]
print("\nmy_list: ", my_list)
my_list.insert(0, "A")
print("my_list after inserting A:", my_list)
my_list.insert(2, "X")
print("my_list after inserting X:", my_list)
my_list.insert(len(my_list), "Z")
print("my_list after inserting Z:", my_list)

# We may remove the first occurrence of an item of given value with method remove:
my_list.remove("X")
print("\nmy_list after removing X: ", my_list)
# If there are no given item, then a ValueError exception will be raised.

# To remove an item from a given index use a method pop.
removed_item = my_list.pop(0)
print("my_list after removing the first item: ", my_list)
# The method also returns an item it removed from the list.
print("removed_item:", removed_item)
# The default index for method pop is the last index of the list:
my_list.pop()
print("my_list after removing the default item: ", my_list)

# To remove all the items from the list use method clear
my_list.clear()
print("my_list after calling the method clear: ", my_list)

# To find the first occurrence of a given item use a method index
my_list = ["item 1", "item 2", "item 3", "item 2"]
print("\nmy_list: ", my_list)
print("my_list.index('item 2'): ", my_list.index("item 2"))
# If there is no searched item a ValueError is raised.

# Method count returns a number of occurrences of a given value in a list.
print("my_list.count('item 2'): ", my_list.count("item 2"))

# Let us assume that we have the following list:
my_list = ["A", "C", "B"]
print("\nmy_list: ", my_list)
# We may sort the list with method sort.
my_list.sort()
print("my_list after sort: ", my_list)
my_list.sort(reverse=True)
print("my_list after sort (reverse): ", my_list)

# The method sort works for integers and floats (even mixed):
my_list = [1, 3, 2]
print("\nmy_list: ", my_list)
my_list.sort()
print("my_list after sort: ", my_list)

# as well as for strings:
my_list = ["item 1", "item 3", "item 2"]
print("\nmy_list: ", my_list)
my_list.sort()
print("my_list after sort: ", my_list)
# However, an exception shown below will be raised if the list contains numbers and strings
# TypeError: '<' not supported between instances of 'float' and 'str'

# The list may be reversed with method reverse:
my_list.reverse()
print("my_list after reverse: ", my_list)

# As you may recall, the variable my_list stores reference to list.
my_list = ["A", "B", "C"]
print("\nmy_list: ", my_list)
my_list_2 = my_list
print("my_list_2: ", my_list_2)

# Therefore if we change one list the other will also change.
my_list[0] = "D"
print("my_list after change:", my_list)
print("my_list_2 after change in my_list:", my_list_2)

# To get a copy of values in another list you may use a method copy:
my_list = ["A", "B", "C"]
print("\nmy_list: ", my_list)
my_list_2 = my_list.copy()
print("my_list_2 (my_list.copy()): ", my_list_2)

# There will be no changes to the list.
my_list[0] = "D"
print("my_list after change:", my_list)
print("my_list_2 after change in my_list:", my_list_2)

# A list may also be copied with a copy method from module copy.
import copy
my_list = ["A", "B", "C"]
print("\nmy_list: ", my_list)
my_list_2 = copy.copy(my_list)
print("my_list_2 (copy.copy(my_list)): ", my_list_2)

# There will be no changes to the list.
my_list[0] = "D"
print("my_list after change:", my_list)
print("my_list_2 after change in my_list:", my_list_2)

# This works for primitive types however does not if stored values are objects like list:
my_list = ["A", "B", ["C", "D"]]
print("\nmy_list: ", my_list)
my_list_2 = copy.copy(my_list)
# my_list_2 = my_list.copy()
print("my_list_2 (copy.copy(my_list)): ", my_list_2)

my_list[2][0] = "E"
print("my_list after change:", my_list)
print("my_list_2 after change in my_list:", my_list_2)
# The same will hapen for my_list_2 = my_list.copy()

# To avoid this inconvenience use copy.deepcopy instead of copy.copy:
my_list = ["A", "B", ["C", "D"]]
print("\nmy_list: ", my_list)
my_list_2 = copy.deepcopy(my_list)
print("my_list_2 (copy.deepcopy(my_list)): ", my_list_2)

my_list[2][0] = "E"
print("my_list after change:", my_list)
print("my_list_2 after change in my_list:", my_list_2)
