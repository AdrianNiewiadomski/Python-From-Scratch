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

print("----------------------------------------------")

def word_check(mystring):
    return 'alaaaaa' in mystring

string = "Szla dzieweczka do laseczka, szla i szla"
print(word_check(string))

print("----------------------------------------------")

def code_maker(mystring):
    lista = []
    lista1 = ['a','e','i','o','u']
    for letter in mystring:
        if letter.lower() in lista1:
            lista.append('x')
        else:
            lista.append(letter)
    print("".join(lista))


code_maker("Ala ma kota")

print("---------------- Zadanie ----------------")
#Zadanie. Napisz funkcję, która sprawdzi czy w zadanej liście znajduje się sekwencja [1,2,3].
#Zwróć True jeśli tak.

#Hint użyj cięcia listy i pętli for

def znajdz_123(lista):
    for i in range(len(lista)-2):
        if lista[i:i+3] == [1,2,3]:
            print(lista[i:i+3])
            return True
    return False

print(znajdz_123([1,2,3,4,5,6,22,-3]))
print(znajdz_123([2,2,3,4,1,1,2,-3]))
print(znajdz_123([2,1,3,4,5,6,22,-3,1,2,3]))