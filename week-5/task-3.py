# Task 3: OOP Principles

class Person:
    def __init__(self, name):
        self.name = name  # encapsulation

    def get_info(self):
        return f"Person name: {self.name}"


class Student(Person):  # inheritance
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def get_info(self):  # polymorphism
        return f"Student name: {self.name}, ID: {self.student_id}"


# Test
person = Person("Madina")
student = Student("Zarina", 241925 )

print(person.get_info())
print(student.get_info())
