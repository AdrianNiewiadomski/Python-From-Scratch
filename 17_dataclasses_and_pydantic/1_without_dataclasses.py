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


if __name__ == "__main__":
    person1 = Person("Johny", "Soldier", 30)
    print(person1)  # This will print only an address of the object.

    person2 = Person("Tom", "Plumber", 25)
    person3 = Person("Tom", "Plumber", 25)
    print(id(person2))
    print(id(person3))  # The address in the memory of person2 and person3 is different.
    # Therefore they are different objects.

    print(person2 == person3)  # As a result they are not equal.

    print(person1 > person2)  # TypeError: '>' not supported between instances of 'Person' and 'Person'
