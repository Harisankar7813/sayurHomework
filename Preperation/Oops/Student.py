class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def print_details(self):
        print("Student details")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grade:{self.grade}")
Student_details=Student("Hari",34,"A")
Student_details.print_details()aA