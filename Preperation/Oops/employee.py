class Employee:
    def __init__(self,name,age,emp_id,department):
        self.name=name
        self.age=age
        self.emp_id=emp_id
        self.department=department
    def print_details(self):
        print("Employee details")
        print(f"Name {self.name}")
        print(f"Age{self.age}")
        print(f"Employee id {self.emp_id}")
        print(f"Department {self.department}")
Employee_detail1=Employee("Hari",23,982398,"Software") 
Employee_detail2=Employee("sankar",18,983428,"engineer") 
Employee_detail1.print_details()
Employee_detail2.print_details()