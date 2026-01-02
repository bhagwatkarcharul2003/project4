#
class Employee:
    def show(self,name,__salary,_branch):
        print(name,__salary,_branch)
emp=Employee()
emp.show("charul",40000,"HR")

class Employee:
    def __init__(self,__salary,_branch):
        self.__salary=__salary
        self._branch="hr"
    def show(self):
        print(self.__salary,self._branch)
emp=Employee(40000,"HR")
emp.show()
print(emp._branch)
print(emp._Employee__salary)

class Employee:
    def __init__(self,name,_branch):
        self.name=name
        self._branch="hr"
    def show(self):
        print(self.name,self._branch)
emp=Employee("charul","hr")
emp.show()
print(emp.name)
print(emp._branch)


class Employee:
    def __init__(self,name,__salary):
        self.name=name
        self.__salary=__salary
    def show(self):
        print(self.name,self.__salary)
emp=Employee("charul",40000)
emp.show()
print(emp.name)
print(emp._Employee__salary)