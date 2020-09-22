class Dom:
    def __init__(self, adres, liczba_pieter, kolor):
        self.adres = adres
        self.liczba_pieter = liczba_pieter
        self.kolor = kolor

    def opisz_dom(self):
        print("Twoj dom znajduje sie przy ul. {}, ma {} pietra i jest {}."
              .format(self.adres, self.liczba_pieter, self.kolor))

    def metoda1(self):
        pass

    def metoda2(self):
        pass

    class Builder:
        def __init__(self):
            self.adres = ""
            self.liczba_pieter = 0
            self.kolor = ""

        def ustaw_adres(self, adres):
            self.adres = adres
            return self

        def ustaw_liczba_pieter(self, liczba_pieter):
            self.liczba_pieter = liczba_pieter
            return self

        def ustaw_kolor(self, kolor):
            self.kolor = kolor
            return self

        def build(self):
            return Dom(self.adres, self.liczba_pieter, self.kolor)


def main():
    moj_dom = Dom.Builder()\
        .ustaw_adres('Jakis_adres')\
        .ustaw_liczba_pieter(2)\
        .ustaw_kolor('szary')\
        .build()
    moj_dom.opisz_dom()


if __name__ == "__main__":
    main()
