#Zbiory modułów będziemy umieszczać w pakietach.
#Pakietem może być dowolny (zwykły) katalog zawirający plik __init__.py
#Można też użyć edytora jak na przykład PyCharm, który automatycznie doda __init__.py

#Dodano pakiet myPackage oraz jego podpakiet mySubPackage.
#Pliki __init__.py zostały dodane automatycznie. Są one puste (i mogą takie być).

import myPackage.some_main_script

napis = myPackage.some_main_script.konkat("Ala ", "ma kota")
print(napis)

from myPackage.mySubPackage.some_sub_script import fun as fun
fun()
#fun2()  #NameError: name 'fun2' is not defined

#from myPackage.mySubPackage.some_sub_script import *
fun()
#Można wywołać fun2 (L20) bo wszystko jest zaimportowane. Nawet bez linii 17
myPackage.mySubPackage.some_sub_script.fun2()