#multiple
class Parent1:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname 
    def show(self):
        print(self.fname,self.lname)      
class Parent2:
    def __init__(self,middlename,age):
        self.middlename=middlename
        self.age=age
    def sell(self):
        print(self.middlename,self.age)     
class Child(Parent1,Parent2):
    pass
c1=Parent1("charu","bhagwatkar")
c2=Parent2("harshda",20)    
c1.show()
c2.sell()
c2.sell()


