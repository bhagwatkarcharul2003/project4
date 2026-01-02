#single
class Library:
    def __init__(self,bookn,booka):
        self.bookn=bookn
        self.booka=booka
    def show(self):
        print(self.bookn,self.booka)
class school(Library):
    def __init__(self,bookn,booka,books):
        self.books=books
        super().__init__(bookn,booka)
    def new(self):
        print(self.booka, self.bookn, self.books)
s1=school("maths","charu","pelne")
s2=school("english","kunal","bhagwatkar")
s3=school("science","harshda","kakde")
s1.show()
s2.show()            
s3.show()
s1.new()
s2.new()
s3.new()