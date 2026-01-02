class Library:
    def __init__(self,bookn,booka):
        self.bookn=bookn
        self.booka=booka
    def show(self):
        print(self.bookn,self.booka)
class school(Library):
    pass
s1=school("maths","charu")
s2=school("english","kunal")
s1.show()
s2.show()            