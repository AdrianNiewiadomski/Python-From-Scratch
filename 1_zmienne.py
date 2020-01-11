print("Hello world!")

# This is comment

print(2+2)
print(8**2)
print(2+2*10)

print("----------------------------------- Zmienne + Dynamic typing -----------------------------------")

x = 2
print(x)
x = 2.5
print(x)
x = "Napis"
print(x)
x = ["Napis", 2, 2.5]
print(x)

print("----------------------------------- Typy zmiennych + funkcja type() -----------------------------------")
x = True
print(x)
print(type(x))
x = 2
print(x)
print(type(x))
x = 2.5
print(x)
print(type(x))
x = "Napis"
print(x)
print(type(x))
x = ["Napis", 2, 2.5]
print(x)
print(type(x))
x = {"Adrian":1,"Danuta":2}
print(x)
print(type(x))


print("----------------------------------- rzutowanie -----------------------------------")

#x="2.5"
#print(x+2)				#TypeError: can only concatenate str (not "int") to str

x="2.5"
print(x+str(2))

x="2.5"
print(float(x)+2)

x = 10/2
print(x)
print(type(x))

x=int(x)
print(type(x))

x=bool(x)
print(x)

print("----------------")
x=0
print(x)
x=bool(x)
print(type(x))
print(x)

print("----------------")
x=1
print(x)
x=bool(x)
print(type(x))
print(x)

print("----------------")
x="0"
print(x)
x=bool(x)
print(type(x))
print(x)

print("----------------")
x=""
print(x)
x=bool(x)
print(type(x))
print(x)

print("----------------------------------- input -----------------------------------")

print("podaj x")
x = input()
print(x)
print(type(x))