# Pamietamy użycie import math, import time i import datetime.
# Importowaliśmy wtedy moduły by móc wykorzystać napisane przez kogoś funkcje.
# Możemy też pisać własne moduły


# Importujemy moduł
import my_module
# używamy funkcji za pomocą składni nazwa_modulu.nazwa_funkcji()
print("2+2 =", my_module.add(2, 2))


# Jeśli z dużego modułu potrzebuję tylko kilku funkcji
from my_big_module import calculate_product

# Tutaj nie trzeba pisać nazwy modułu!
print("2*3 =", calculate_product(2, 3))


import datetime
print(datetime.datetime.now())

# Można ustalać swoje nazwy funkcji jeśli oryginalne są kłopotliwe
from datetime import datetime as data
print(data.now())
# Jest to ekwiwalent wcześniejszego datetime.datetime.now()

# Dobra praktyka jest umieszczac importy modulow na poczatku pliku
