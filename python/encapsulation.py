class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks")

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.__marks)


student1 = Student("Kumaran", 85)

student1.show_details()

student1.update_marks(95)

student1.show_details()
