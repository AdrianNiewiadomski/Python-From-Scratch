# Let's create a list:
my_list = ["item 1", "item 2", "item 3"]

# When you check the type of my_list, you will see that it belongs to a class called list.
print("type(my_list): ", type(my_list))

# This class contains a number of functions that can be can be performed on a list.

# We already know a function called len, that returns a length of a list.
print("The length of my_list is: ", len(my_list))

# We can add an item to the list with the append method.
my_list.append("item 4")
print("my_list after appending item 4: ", my_list)

# To append more items to the list you may use a method extend:
my_list.extend(["item 5", "item 6"])
print("my_list after extending: ", my_list)

# To insert item before given index use a method insert.
# 3 examples are presented below.
my_list = ["item 1", "item 2", "item 3"]
my_list.insert(0, "A")
print("\nmy_list after inserting A:", my_list)
my_list.insert(2, "X")
print("my_list after inserting X:", my_list)
my_list.insert(len(my_list), "Z")
print("my_list after inserting Z:", my_list)

# We may remove an item of given value with method remove:
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

# As
my_list2 = my_list
print(my_list2)
print(my_list2)

my_list2.clear()
print(my_list2)
print(my_list2)

print("copy.copy(lista) -----------------------")
import copy
lista = ["ser", "mleko", "parowki"]
lista2 = copy.copy(lista)
print(lista)
print(lista2)

lista.clear()
print(lista)
print(lista2)

print("-----------------------")
lista = ["ser", "mleko", "parowki"]
lista2 = lista.copy()
print(lista)
print(lista2)

lista.clear()
print(lista)
print(lista2)

print("lista.insert(index, object) -----------------------")
lista.insert(2, 3.14)
print(lista)

print("-----------------------")
print(lista.pop(2))
print(lista)