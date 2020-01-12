print("----------------------------------- String'i - metody -----------------------------------")
x = "Hello"
print(x)
print(len(x))
print(x[len(x)-1])

print('----------------------------')
x = "[a,b]"
print( x[ 1 : x.index(']') ] )

print('----------------------------')
x = "a,b,c"
x = x.split(',')
print(x)

print('----------------------------')
x = "15:30"
godz,min = x.split(':')
print(godz)
print(min)

print('----------------------------')
x = "Hello World"
print(x.split())

print('----------------------------')
wyraz = "123"
a,b,c = wyraz
print(a)
print(b)
print(c)

print('----------------------------')
wyraz = '[a,b][c,d]'
print( wyraz[ 1 : wyraz.find(']') ] )
print( wyraz[ wyraz.rfind('[') +1 : wyraz.rfind(']') ] )

print('----------------------------')
x = "Hello"
x = x.upper()
print(x)
x = x.lower()
print(x)

print("----------------------------------- String'i - format -----------------------------------")
user = "Danuta"
color = "green"
print("The {} fav color is {}".format(user,color))

print("----------------------------------- python 3.6 -----------------------------------")
print(f"The {user} chose {color}")