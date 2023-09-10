#  From YouTube chanel ArjanCodes
# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://www.youtube.com/watch?v=CvQ7e6yUtnw
# Let's say that we want to create, print, compare and sort objects of class Person
from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        self.sort_index = self.strength


if __name__ == "__main__":
    person1 = Person("Johny", "Soldier", 30, 120)
    print(person1)

    person2 = Person("Tom", "Plumber", 25)
    person3 = Person("Sam", "Plumber", 42, 95)

    print(person1 > person2)  # This works.

    mylist = [person2, person1, person3]
    mylist.sort()
    print(mylist)
