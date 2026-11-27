from abc import ABC, abstractmethod


# Abstraction
class Person(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_details(self):
        pass


# Inheritance and Encapsulation
class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks")

    def show_details(self):
        print("Student Name:", self.name)
        print("Marks:", self.__marks)

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"


# Create student objects
student1 = Student("Kumaran", 85)
student2 = Student("Arun", 92)

# Polymorphism
students = [student1, student2]

for student in students:
    student.show_details()
    print("Grade:", student.calculate_grade())
    print()
