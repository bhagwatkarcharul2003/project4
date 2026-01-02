#encapsultions
#public
class Employee:
    def __init__(self,name,designations,salary):
        self.name=name
        self.designation=designations
        self.salary=salary
    def show(self):
        print(self.name,self.designation,self.salary)
emp=Employee("rajat","HR",40000)
emp.show()
print(emp.name)
print(emp.designation)
print(emp.salary)        