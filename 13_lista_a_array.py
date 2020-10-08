import datetime
import sys

n = 100000

start = datetime.datetime.now()
lista = []

for i in range(n):
    lista.append(i)

for i in range(n):
    lista[i] = lista[i] + 1

print('czas dla listy: ', datetime.datetime.now() - start)
print('wielkosc zwyklej listy: ', sys.getsizeof(lista))


time_before_import_of_array = datetime.datetime.now()
import array
arr = array.array('i', [])

for i in range(n):
    arr.append(i)

for i in range(n):
    arr[i] = arr[i] + 1

print('czas dla array\'a: ', datetime.datetime.now() - time_before_import_of_array)
print('wielkosc array\'a: ', sys.getsizeof(arr))
