#Pamietamy użycie import math, import time i import datetime.
#Importowaliśmy wtedy moduły by móc wykorzystać napisane przez kogoś funkcje.
#Możemy też pisać własne moduły


#Importujemy moduł
import moj_modul
#używamy funkcji za pomocą składni nazwa_modulu.nazwa_funkcji()
print("2+2 =", moj_modul.dodaj(2,2))


#Jeśli z dużego modułu potrzebuję tylko kilku funkcji
from moj_duzy_modul import iloczyn,iloraz
#Tutaj nie trzeba pisać nazwy modułu!
print("2*3 =", iloczyn(2,3))


#Można ustalać swoje nazwy funkcji jeśli oryginalne są kłopotliwe
from datetime import datetime as data
print(data.now())
#wcześniej datetime.datetime.now()