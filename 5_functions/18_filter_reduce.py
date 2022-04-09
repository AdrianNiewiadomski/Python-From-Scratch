def main():
    lista = [1, 2, 3, 4]
    print("lista: ", lista)

    # Podobnie do funkcji map mozemy wykorzystywac funkcje filter
    przefiltrowana_lista = list(
        filter(lambda x: x > 2, lista)
    )
    print("przefiltrowana_lista: ", przefiltrowana_lista)

    # Zeby uzywac funkcji reduce trzeba ja zaimportowac
    from functools import reduce
    # ponizsze wypisze sume elementow listy
    print("reduce: ", reduce(lambda a, b: a + b, lista))


if __name__ == "__main__":
    main()
