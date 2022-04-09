def main():
    # Niech jest lista
    lista = [i for i in range(4)]
    print("lista: ", lista)

    # teraz chcemy wykonac operacje na jej elementach.
    # Moze to byc np. dodanie 100 do elementow.
    # W tym celu mozna wykorzystac funkcje
    def dodaj_100(zmienna):
        return zmienna + 100

    # Wowczas aby otrzymac zmodyfikowana liste wystarczy napisac
    nowa_lista = list(map(dodaj_100, lista))
    print("nowa_lista: ", nowa_lista)

    # Po obiekcie mapy mozna iterowac
    my_map = map(dodaj_100, lista)
    for i, item in enumerate(my_map):
        print(f"item {i}: {item}")


if __name__ == "__main__":
    main()
