print("----------------------------------- String'i, konkatenacja, indeksy -----------------------------------")

print("String'i")
print(type("String'i"))
print('String\'i')
print('String"i')

x='Hello world!'
print(x)
print(x*2)
#print(x+2)              #TypeError: must be str, not int
print(x+str(2))

x="Hello"
x+=' '
print(x+'world')

x=2
print(x)
x="Hello"
print(x)

x = "Hello world!"
print(x[0])
print(type(x[0]))
print(x[1])
print(x[-1])

print("----------------------------------- String'i - cięcie -----------------------------------")
x = "Ala ma kota"
print(x)
#ciecie x[start:stop:krok]]
print(x[0:-1])
print(x[0:3])
print(x[0:-1:2])
print(x[:])
print(x[4:])
print(x[-5:])
print(x[:5])
print(x[::2])
print(x[::-1])

#x[0] = '!'    #TypeError: 'str' object does not support item assignment