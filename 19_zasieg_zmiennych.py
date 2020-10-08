def funkcja():
    pi = 3.14
    print("Pi =", pi)


funkcja()
# print(pi)   #NameError: name 'pi' is not defined
# jest tak ponieważ zmienna utworzona w funkcji ma zasięg lokalny
# i nie jest widziana na zewnątrz jej funkcji.


x = 2


def funkcja2():
    print("x =", x)  # to jest ok w Pythonie.
    # Zmienna x jest widziana w funkcji. Ma ona zasięg globalny


funkcja2()

napis = "zewnatrz"


def funkcja3():
    napis = "wewnatrz"
    return napis


print(napis)
print(funkcja3())
print(napis)

# Dla Pythona mamy cztery zasięgi zmiennych. Stąd zasada LEGB
#
# 1. LOCAL (aktualna funkcja)
# 2. ENCLOSING (dla funkcji zagnieżdżonych. Zasięg poszerzony do wyrażeń zawierających funkcję)
# 3. GLOBAL (skrypt/moduł)
# 4. BUILT IN (zakres wbudowany - nazwy zmiennych z innych, zaimportowanych modułów itp)
#
# Interpreter Pythona szuka pasujących nazw zmiennych w tej kolejności



outer = 'global'
def func():
    enclosing = 'enclosing'
    def inner():
        inner = 'inner'
        print(inner)           #fetch from (L)ocal scope
        print(enclosing)       #fetch from (E)nclosing scope
        print(outer)           #fetch from (G)lobal scope
        print(any)             #fetch from (B)uilt-ins
    inner()
func()



zmienna = "global"
def funkcja_zewnetrzna():
    zmienna = "enclosing"

    def funkcja_wewnetrzna():
        print("zmienna =", zmienna)
        #   Ale uwaga! Jeśli zdefiniujemy tutaj zmienną o tej samej nazwie
        #   co zmienna funkcji zewnętrznej to powyższa linijka spowoduje błąd
        #zmienna = 2
    funkcja_wewnetrzna()
funkcja_zewnetrzna()



from moj_duzy_modul import *
print("zmienna_w_module =",zmienna_w_module)



napis = "zewnatrz"
def funkcja4():
    napis = "wewnatrz"
    return napis
napis = funkcja4()
print(napis)



napis = "zewnatrz"
def funkcja5():
    global napis
    napis = "wewnatrz"
funkcja5()
print(napis)