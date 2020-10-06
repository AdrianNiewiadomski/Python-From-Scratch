print('Sets are data types that store unordered and unindexed values.')
x = set()
print(x)
x.add('John')
x.add('Doe')

print(x)
# print(x[1]) #TypeError: 'set' object does not support indexing

x.add(2)
print(x)

print("--------------------")
lista = [1, 1, 2, 3, 4, 5, 2, 2, 3, 1, 1, 0]
print(set(lista))
