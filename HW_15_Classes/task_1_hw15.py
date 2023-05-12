
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = self.age_validator(age)

    def called_talk(self):
        print(f"Hello, my name is {self.name} {self.surname} and I'm {self.age} years old")
        
    def age_validator(self, age):
        if age < 0:
            raise ValueError("You are have not born yet!")

p_1 = Person("Alan", "Turing", -1)

p_1.called_talk()