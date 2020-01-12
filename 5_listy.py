lista = []
print(lista)
print(type(lista))

print("-----------------------")
lista = ["ser", "mleko", "parowki"]
print(lista)
print(lista[0])
print(lista[0][0])

print(lista[:2])

print("-----------------------")
lista.append("Szynka")
print(lista)

print("-----------------------")
lista2 = lista
print(lista)
print(lista2)

lista.clear()
print(lista)
print(lista2)

print("-----------------------")
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

print("-----------------------")
lista.insert(1,3.14)
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