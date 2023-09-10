#  From YouTube chanel ArjanCodes
# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://www.youtube.com/watch?v=CvQ7e6yUtnw
# Let's say that we want to create, print, compare and sort objects of class Person
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.strength)

    def __str__(self):
        return f"{self.name}, {self.job} ({self.strength})"


if __name__ == "__main__":
    person1 = Person("Johny", "Soldier", 30, 120)
    print(person1)

    person2 = Person("Tom", "Plumber", 25)
    person3 = Person("Tom", "Plumber", 25)
    print(person2)

    print(person2 == person3)  # This works.

    print(person1 > person2)  # This works.
