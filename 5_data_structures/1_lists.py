# Data structures like list allow to store multiple items.
my_list = []
print("my_list: ", my_list)

print("-----------------------")
my_list = ["item 1", "item 2", "item 3"]
print(my_list)
print(my_list[0])
print(my_list[0][0])

print(lista[:2])

print("We can add items to list with append method")
lista.append("item 4")
print(lista)

print("-----------------------")
lista2 = lista
print(lista)
print(lista2)

lista.clear()
print(lista)
print(lista2)

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

print("-----------------------")
lista = [1, 2.5, "parowki"]
print(lista)

print("lista.insert(index, object) -----------------------")
lista.insert(2, 3.14)
print(lista)

print("-----------------------")
print(lista.pop(2))
print(lista)

print("-----------------------")
li1 = [0,1,2]
li2 = [3,4,5]
li3 = [6,7,8]

li = [li1, li2, li3]
print(li)
print(len(li))

print("-----------------------")
lista = [1, 1, 1]
print(lista)
