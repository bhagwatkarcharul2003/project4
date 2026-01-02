class Parent1:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
    def show(self):    
        print(self.fname,self.age)
class Parent2:
    def __init__(self,mname):
        self.mname=mname
    def show1(self):    
        print(self.mname)
class Child1(Parent1,Parent2):
    def __init__(self,fname,age,mname,lname,BOD):
        self.lname=lname
        self.BOD=BOD
        Parent1().__init__(fname,age)
        Parent2().__init__(mname)
    def new(self):
        print(self.fname,self.age,self.mname,self.lname,self.BOD)
class Child2(Parent1,Parent2):
    def __init__(self,fname,age,mname,birthofplace):
        self.birthofplace=birthofplace
        Parent1().__init__(fname,age)
        Parent2().__init__(mname)
    def new1(self):
            print(self.fname,self.age,self.mname,self.birthofplace)
class Child3(Child1,Child2):
    def __init__(self,lname,BOD,birthofplace,gender):
        self.gender=gender
        Child1().__init__(lname,BOD)
        Child2().__init__(birthofplace)
    def new2(self):
            print(self.lname,self.BOD,self.birthofplace,self.gender)
class Child4(Child3):
    def __init__(self, gender,id):
        self.id=id
        Child3().__init__(gender)
    def new3(self):
        print(self.gender,self.id)    
c1=Parent1("charul",19)
c2=Parent2("pandurang")
c3=Child1("bhagwatkar","11 jan 2003")
c4=Child2("nagpur")
c5=Child3("female")
c6=Child4(2204)
c1.show()
c2.show1()
c3.new()
c4.new1()
c5.new2()
c6.new3()