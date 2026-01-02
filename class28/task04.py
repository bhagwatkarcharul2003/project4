#hybrid
class Parent1:
    def abc(self,fname,age):
        print(fname,age)
class Parent2:
    def xyz(self,mname):
        print(mname)
class Child1(Parent1,Parent2):
    def mno(self,fname,age,mname,lname,BOD):
        print(fname,age,mname,lname,BOD)  
class Child2(Parent1,Parent2):
    def uvw(self,fname,age,mname,lname,BOD,brithofplace):
        print(fname,age,mname,lname,BOD,brithofplace)
class Child3(Child1,Child2):
    def gfh(self,fname,age,mname,lname,BOD,brithofplace,gender):
        print(fname,age,mname,lname,BOD,brithofplace,gender)
class Child4(Child3):
    pass
c1=Child4()
c1.gfh("charul","19","pandurang","bhagwatkar","11 jan 2003","nagpur","female")
#second object
c2=Child1
c2.abc(20,"charul",19)
c3=Child2
c3.xyz("yyy","pandurang")
c4=Child3
c4.mno("charul","19","pandurang","bhagwatkar","11 jan 2003","nagpur")
c4.uvw("charul","19","pandurang","bhagwatkar","11 jan 2003","nagpur","female")