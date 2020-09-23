# niech jest lista
lista = [i for i in range(10)]


# teraz chcemy wykonac operacje na jej elementach.
# Moze to byc np. dodanie 100 do elementow.
# W tym celu mozna wykorzystac funkcje
def dodaj_100(zmienna):
    return zmienna + 100


# Wowczas aby otrzymac zmodyfikowana liste wystarczy napisac
nowa_lista = list(map(dodaj_100, lista))
print(nowa_lista)

# Jezeli funkcja dodaj_100 byla napisana tylko w celu wykonania przeksztalcenia listy.
# Dlatego nie bedzie ona juz nigdy potrzebna. W takim wypadku stosuje sie lambdy.
nowa_lista = list(
    map(lambda zmienna: zmienna + 100, lista)
)
print(nowa_lista)

# Podobnie sprawa ma sie z funkcja filter
przefiltrowana_lista = list(
    filter(lambda x: x > 5, lista)
)
print(przefiltrowana_lista)