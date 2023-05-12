
class Person:

    def __init__(self, name: str, surname: str, age: int, country: str):
        
        self.name = name
        self.surname = surname
        self.age = self.age_validator(age)
        self.age = age
        self.country = country
        
    def age_validator(self, age):
        if age < 0:
            raise ValueError("Age can't be negative")
        
    def full_info(self):
        return f"{self.name} {self.surname} is {self.age} years old, he/she is from {self.country}"
    



class Student(Person):

    classes = 12

    def __init__(self, name: str, surname: str, age: int, country: str, grade: int):
        self.grade = grade
        super().__init__(name, surname, age, country)

    # Calculates how many years until the graduation
    def years_left_calc(self):
        years_left = Student.classes - self.grade
        return f"There are {years_left} years left till the graduation"
    
    # Returns avarage value of your marks
    def avarage_mark(self, *args):
        av_mark = sum(args) / len(args)
        return f"Your avarage mark is {av_mark}"

    # Checks whether you passed or failed exam
    def fail_pass(self, mark):
        if mark < 60:
            return "You've failed"
        else:
            return "You've passed"
    # Converts marks from (0-100) system to the (2F - 5A) system  
    def digit_to_letter_mark_converter(self, mark): #I tried to to this methof with match/case but didn't understand syntax
        if mark in range(0, 60):
            return "Your mark is 2F"
        elif mark in range(60, 75):
            return "Your mark is 3E"
        elif mark in range(75, 80):
            return "Your mark is 4C"
        elif mark in range(80, 90):
            return "Your mark is 4B"
        elif mark in range(90, 101):
            return "Your mark is 5A"
        else:
            return "Wrong mark format"


    
class Teacher(Person):

    salary_ratio = 1.0
    min_retirement_exp = 30

    def __init__(self, name: str, surname: str, age: int, country: str, subject: str, experience_years: int, init_salary: int):
        self.subject = subject
        self.init_salary = init_salary
        self.experience_years = experience_years
        super().__init__(name, surname, age, country)

    # Calculates salary 
    def salary_calc(self):
        self.salary_ratio += self.experience_years * 0.5
        return self.init_salary * self.salary_ratio
    
    # How many years until the retirement
    def retirement_calc(self):
        if self.experience_years < 30 and self.age < 60:
            exp_age = self.age + Teacher.min_retirement_exp - self.experience_years   
            if exp_age < 60:
                return f"{Teacher.min_retirement_exp - self.experience_years} years left"
            else:
                return f"{60 - self.age} years left"
        else:
            return "You should have been retired already"

    


