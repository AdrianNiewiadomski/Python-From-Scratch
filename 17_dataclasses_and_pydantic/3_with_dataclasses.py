#  From YouTube chanel ArjanCodes
# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://www.youtube.com/watch?v=CvQ7e6yUtnw
# Let's say that we want to create, print, compare and sort objects of class Person
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    job: str
    age: int


if __name__ == "__main__":
    person1 = Person("Johny", "Soldier", 30)
    print(person1)

    person2 = Person("Tom", "Plumber", 25)
    person3 = Person("Tom", "Plumber", 25)

    print(person2 == person3)  # This works.

    print(person1 > person2)  # But this does not.
