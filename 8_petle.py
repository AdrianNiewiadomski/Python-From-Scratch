i=0
while i<10:
    print(i)
    #i++    #unresolved reference
    i = i + 1

print("---------------------------------")

i = 0;j=0
while i<5:
    while j<=i:
        print('*', end=' ')
        j = j+1
    print()
    i = i+1
    j = 0

print("---------------------------------")

char = 'z'; string = "asvfllnfgnnhnmh"
if char in string:
    print(f"{char} is in the {string} string.")
else:
    print(f"{char} is not in the {string} string.")

print("---------------------------------")

lista = [1,2,3,4]
for i in lista:
    print(i)

print("---------------------------------")

lista = list(range(5,10,1))
print(lista)

print("---------------------------------")

for i in range(5):
    print(f"i : {i}")

print("---------------------------------")

for i in range(5,10,2):
    print(f"i : {i}")

print("---------------------------------")

mystring = "hello"
for ch in mystring:
    print(ch)

print("---------------------------------")

salaries = {'John':10, 'Sally':20}
for key in salaries:
    print(key)

print("---------------------------------")

salaries = {'John':10, 'Sally':20}
for key in salaries:
    print(f"{key} : {salaries[key]}")

print("--------------------------------- odpakowywanie tupli")

lista_tupli = [("a",1),("b",2),("c",3)]
for (item1,item2) in lista_tupli:   #nawiasy sa opcjonalne
    print(f"{item1} : {item2}")