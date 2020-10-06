# tworzenie listy w 'tradycyjny' sposob
moja_lista = [1, 2, 3]
print('moja_lista: ', moja_lista)

# lub
moja_inna_lista = []
for i in range(10):
    moja_inna_lista.append(i)
print('moja_inna_lista: ', moja_inna_lista)

# list comprehension pozwala uproscic powyzsze
moja_nowa_lista = [i for i in range(10)]
print('moja_nowa_lista: ', moja_nowa_lista)

# wyrazenie moze tez zawierac instrukcje warunkowe
moja_inna_nowa_lista = [i for i in range(10) if i % 2 == 0]
print('moja_inna_nowa_lista: ', moja_inna_nowa_lista)

# mozna tez podobnie tworzyc slowniki
