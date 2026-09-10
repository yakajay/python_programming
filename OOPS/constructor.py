

class Employee: # A class in Python is a blueprint or template for creating oobjects.
    department = "Accounts"

# A class can have set attributes (variables) and methods(functions).

#Constructor
#1. non-parameterized constructor

    def __init__(self): # this is the way to declare the constructor
        self.emp_name = "Ajay"
        self.phone = "123456"

    def emp_detail(self):
        return f"Employee Name is {self.emp_name}, phone number is {self.phone}"

new_emp = Employee()

print(new_emp.emp_detail())

#2. parameterized construcotr

class Student:

    def __init__(self, name, age): # construcot method is names as "__init__"
        self.name = name
        self.age = age

    def stuednt_det(self):
        return f"Student name is {self.name}, age is {self.age}"

student_one = Student("Ajay", 32) # we can create a n number of objects based on any number of instances using a class objects
print(student_one.stuednt_det())

student_two = Student("Sravani", 30)
print(student_two.stuednt_det())

student_three = Student("Kanth", 40)
print(student_three.stuednt_det())

student_four = Student("Lekshu", 8)
print(student_four.stuednt_det())

