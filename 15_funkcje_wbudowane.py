print("---------------- funkcje wbudowane - max, min i sum ----------------")

print(max(2,3))
print(min([1,2,3,4,5,6,7]))
print(sum([1,2,3]))

print("---------------- moduł math ----------------")

import math
print("math.cos(math.pi) = ", math.cos(math.pi))
print("math.sqrt(2) = ", math.sqrt(2))

print("---------------- funkcje wbudowane - enumerate ----------------")

for letter in ['a', 'b', 'c']:
    print(letter)

mylist = ['a', 'b', 'c']
for letter in mylist:
    print(letter)

#jeśli chcemy indeks tych liter:
mylist = ['a', 'b', 'c']
i = 0
for letter in mylist:
    print("{} znajduje sie pod indeksem {}".format(letter,i))
    i = i+1

#wygodnie jest przy użyciu enumerate

mylist = ['a', 'b', 'c']

for item in enumerate(mylist):
    print(item)
    print("{} znajduje sie pod indeksem {}".format(item[1],item[0]))

for key,value in enumerate(mylist):
    print("{} znajduje sie pod indeksem {}".format(value,key))

print("---------------- funkcje wbudowane - join ----------------")

mylist = ['a', 'b', 'c']
print("".join(mylist))
print("--".join(mylist))

print("---------------- funkcje wbudowane - split ----------------")

string = "a,b,c,d"
print(string.split(","))
lista = string.split(",")
print(lista[0])

print("---------------- funkcje wbudowane - index ----------------")

indeks="szla dzieweczka do laseczka, szla i szla".index("szla")
print(indeks)

indeks="Szla dzieweczka do laseczka, szla i szla".index("szla")
print(indeks)

print('---------------- zip function ----------------')
my_list_1 = [1, 2, 3]
my_list_2 = ['a', 'b', 'c']
my_zip_object = zip(my_list_1, my_list_2)
print('A zip object is an iterator and may be converted into list.')
print(list(my_zip_object))
