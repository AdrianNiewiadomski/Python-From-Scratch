def main():
    # Lambde czyli funkcje anonimowa mozemy definiowac tak
    my_lambda = lambda x: x + 200
    # my_lambda zawiera referencje do funkcji. Owa funkcje mozemy wywolac jak ponizej.
    print("my_lambda(2): ", my_lambda(2))
    # Jednak przechowywanie referencji do lambdy jest niezgodne z PEP 8

    # Wykorzystanie lambdy dobrze obrazuje przyklad uzycia funkcji map. Niech jest lista
    lista = [1, 2, 3, 4]
    print("lista: ", lista)

    # Teraz chcemy wykonac operacje na jej elementach. Moze to byc np. dodanie 100 do elementow.
    # W tym celu mozna wykorzystac funkcje
    def dodaj_100(zmienna):
        return zmienna + 100

    # Wowczas aby otrzymac zmodyfikowana mozemy napisac:
    nowa_lista_1 = list(map(dodaj_100, lista))

    # Mozna tez uzyc lambd
    nowa_lista_2 = list(map(my_lambda, lista))
    nowa_lista_3 = list(map(lambda x: x + 300, lista))
    print("nowa_lista_1: ", nowa_lista_1)
    print("nowa_lista_2: ", nowa_lista_2)
    print("nowa_lista_3: ", nowa_lista_3)

    multi_argument_lambda = lambda x, y, z: f"{x}x + {y}y + {z}z"
    print("multi_argument_lambda: ", multi_argument_lambda(1, 2, 3))


if __name__ == "__main__":
    main()
