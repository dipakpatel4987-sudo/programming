
class Employee:
    
   
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


emp1 = Employee("Dipak", 22, 25000)


print("Employee Name:", emp1.name)
print("Employee Age:", emp1.age)
print("Employee Salary:", emp1.salary)