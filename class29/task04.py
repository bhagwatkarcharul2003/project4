class Employee:
    def __init__(self,name,__salary,_branch):
        self.name=name
        self.__salary=__salary
        self._branch="hr"
    def show(self):
        print(self.name,self.__salary,self._branch)
emp=Employee("charul",40000,"hr")
emp.show()
print(emp.name)
print(emp._branch)
print(emp._Employee__salary)   





class Employee:
    def __init__(self,name,__salary,_branch):
        self.name=name
        self.__salary=__salary
        self._branch="hr"
emp=Employee("charul",40000,"hr")
print(emp.name)
print(emp._branch)
print(emp._Employee__salary)   



