import os
from zipfile import ZipFile


class FileHelper:
    @classmethod
    def utworz_katalog(cls, sciezka):
        try:
            os.mkdir(sciezka)
        except FileExistsError:
            print('\'{}\' juz istnieje!'.format(sciezka))
        except OSError:
            print('Utworzenie katalogu \'{}\' nie powiodlo sie!'.format(sciezka))
        else:
            print('Utworzono katalog \'{}\'.'.format(sciezka))

    @classmethod
    def utworz_plik(cls, sciezka, dane):
        with open(sciezka, 'w') as plik:
            plik.write(dane)

    @classmethod
    def kompresuj_pliki(cls, sciezka, pliki):
        zip_obj = ZipFile(sciezka, 'w')
        for plik in pliki:
            zip_obj.write(plik)
        zip_obj.close()


def main():
    path = os.getcwd()

    FileHelper.utworz_katalog(path+'/temp')
    FileHelper.utworz_plik(path+'/temp/moj_plik.txt', 'jakies_dane')
    FileHelper.utworz_plik(path + '/temp/moj_inny_plik.txt', 'inne_dane')
    FileHelper.kompresuj_pliki(
        path + '/temp/moje_pliki.zip',
        [path + '/temp/moj_plik.txt', path + '/temp/moj_inny_plik.txt']
    )


if __name__ == '__main__':
    main()
