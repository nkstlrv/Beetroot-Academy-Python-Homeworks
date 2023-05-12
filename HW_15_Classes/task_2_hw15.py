
class Dog:
    
    age_factor = 7

    def __init__(self, name, dog_age):
        self.name = name
        self.dog_age = self.age_validator(dog_age)
        self.dog_age = dog_age

    def age_validator(self, dog_age):
        if dog_age < 0:
            raise ValueError("Bro, age can not be negative! :)")
        
    def human_age(self):
        human_age = self.dog_age * self.age_factor
        print(f"{self.name}'s age, converted to human's equals {human_age}")



dog = Dog("Sharik", 3)

dog.human_age()



