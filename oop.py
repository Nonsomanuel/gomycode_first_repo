#Object Oriented Programming (OOP) in Python
# class Student:
#     def __init__(self, name, age, department):
#         self.name = name
#         self.age = age
#         self.department = department
#
#     def display_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Department: {self.department}"
#
# student1 = Student("Victor", 20, "Data Science")
# student2 = Student("Lekan", 22, "Computer Science")
# print(student1.display_info())
# print(student2.display_info())
# print(student2.department)
#
# #Introducing Methods in Python
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def introduce(self):
#         return f"This is a {self.year} {self.make} {self.model} car."
#
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("Honda", "Civic", 2019)
# print(car1.introduce())
# print(car2.introduce())

#Encapsulation in Python
# class Cat:
#     def __init__(self):
#         self.__sound = "Meow"  # Private attribute
#     def speak(self):
#         print(self.__sound)  # Accessing private attribute through a public method
# speaking_cat = Cat()
# speaking_cat.speak()

#Inheritance in python
# class Animal:
#     def speak(self):
#         print("Animals makes sounds")
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# cat = Cat()
# cat.speak()
# dog = Dog()
# dog.speak()
#
# #Using Inheritance to calculate student average
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def average(self):
#         return sum(self.score)/len(self.score)
#
# class ScienceStudent(Student):
#     pass
#
# class ArtStudent(Student):
#     pass
# class CommercialStudent(Student):
#     pass
#
# sciencestudent1 = ScienceStudent("Stanley", [80, 90, 85])
# artstudent1 = ArtStudent("Waris", [75, 85, 90])
# commercialstudent1 = CommercialStudent("Elizabeth", [70, 80, 75])
#
#
# print(f"{sciencestudent1.name}'s average score is: {sciencestudent1.average()}")
# print(f"{artstudent1.name}'s average score is: {artstudent1.average()}")
# print(f"{commercialstudent1.name}'s average score is: {commercialstudent1.average()}")
#
#
# #Polymorphism in Python
# class Fruits:
#     def fruit_type(self):
#         print("Mango, Banana, Orange")
#
# class Vegetables:
#     def fruit_type(self):
#         print("Carrot, Cabbage, Spinach")
#
# for item in (Fruits(), Vegetables()):
#     item.fruit_type()

#Building Student Management System using OOP
class Student:
    def __init__(self, name, age, score, grade=None):
        self.name = name
        self.age = age
        self.score = score
        self.grade = grade

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and my score is {self.score}, which corresponds to grade {self.get_grade()}."

    def get_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        else:
            return "F"
john = Student("John", 20, 80)
mary = Student("Mary", 19, 75)
david = Student("David", 21, 90)

studentname = input("Enter your name: ")
if studentname.lower() == "john":
    print(john.introduce())
elif studentname.lower() == "mary":
    print(mary.introduce)
elif studentname.lower() == "david":
    print(david.introduce)
else:
    print("Student not found.")

# print(mary.introduce())