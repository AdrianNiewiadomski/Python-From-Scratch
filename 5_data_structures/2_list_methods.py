my_list = ["item 1", "item 2", "item 3"]

print("type(my_list): ", type(my_list))

print("We can add items to list with append method")
my_list.append("item 4")
print(my_list)

# ---------------------------------------

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