class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return f"{__class__.__name__} says woof, woof"


class Cat(Animal):
    def talk(self):
        return f"{__class__.__name__} says meow"


def talking_func(animal):
    return animal.talk()


print(talking_func(Cat()))
print(talking_func(Dog()))