
class Employee:
    def __init__(self):
        self.__salary=50000
    def show(self):
        print("salary is",self.__salary)
class Charul(Employee):
    pass
p=Charul()
p.show()
print(p._Employee__salary)

