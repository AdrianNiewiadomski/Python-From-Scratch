def my_function():
    '''
    to jest dokumentacja funkcji
    :return:void
    '''
    print("Hello world")

my_function()
#my_function("Adrian")          #blad

print("----------------------------------------------")

def my_function(name):
    '''
    to jest dokumentacja funkcji
    :return:void
    '''
    print(f"Hello {name}")

#my_function()  #TypeError: my_function() missing 1 required positional argument: 'name'
my_function("Adrian")

print("----------------------------------------------")

def dodaj(a,b):
    return a+b

print(dodaj(2,3))

print("----------------------------------------------")

def odejmij(a,b=1):
    return a-b

print(odejmij(2,2))
print(odejmij(2,b=3))
print(odejmij(2))