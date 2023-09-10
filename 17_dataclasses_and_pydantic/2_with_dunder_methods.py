#  From YouTube chanel ArjanCodes
# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://www.youtube.com/watch?v=CvQ7e6yUtnw
# Let's say that we want to create, print, compare and sort objects of class Person

class Person:

    # To create objects you have to implement init method
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

    # To compare objects you have to implement eq method
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name \
                and self.job == other.job \
                and self.age == other.age
        else:
            return False

    # To be able to sort the objects we have to implement gt, ge, lt, le methods.
    def __gt__(self, other):
        if isinstance(self, other.__class__):
            return self.age > other.age
        else:
            raise TypeError("Compared objects must be of the same type!")

    # To print objects you have to implement either str or repr method.
    def __str__(self):
        return str({"name": self.name, "job": self.job, "age": self.age})


if __name__ == "__main__":
    person1 = Person("Johny", "Soldier", 30)
    print(person1)

    person2 = Person("Tom", "Plumber", 25)
    person3 = Person("Tom", "Plumber", 25)
    print(id(person2))
    print(id(person3))  # The address in the memory of person2 and person3 is different.
    # Therefore they are different objects.

    print(person2 == person3)  # But because we implemented __eq__ they are now equal.
    print(person1 != person2)  # This works.

    print(person1 > person2)  # Because we implemented __gt__ method, the '>' operator is now supported.
    print(person1 < person2)  # This also seem to work.
    # print(person1 >= person2)  # This raises exception. So we now have to implement le and ge methods.

    # But there is another problem. Everytime anything changes,
    # like a new field has to be added, we have to add it everywhere (to every method).

    mylist = [person2, person1, person3]
    mylist.sort()
    for el in mylist:
        print(el)
