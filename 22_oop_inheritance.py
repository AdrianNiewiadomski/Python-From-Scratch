class Tool:
    def start_engine(self):
        print('Engine start!')


class AngleGrinder(Tool):
    def cut(self):
        print('I\'m cutting!')


class Driller(Tool):
    def drill(self):
        print('I\'m drilling')


def main():
    my_driller = Driller()
    my_driller.start_engine()
    my_driller.drill()

    my_grinder = AngleGrinder()
    my_grinder.start_engine()
    my_grinder.cut()


if __name__ == '__main__':
    main()