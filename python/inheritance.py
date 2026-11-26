class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("My course is", self.course)


student1 = Student("Kumaran", "AI and Data Science")

student1.introduce()
student1.show_course()
