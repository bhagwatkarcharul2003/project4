from abc import ABC
class Polygon(ABC):
    def sides(self):
        pass
class Triangle(Polygon):
    def sides(self):
        print("triangle have 3 sides")
class Square(Polygon):
    def sides(self):
        print("square have 4 sides")
class Rectangle(Polygon):
    def sides(self):
        print("rectangle have 4 sides")
t=Triangle()
s=Square()
r=Rectangle()
t.sides()
s.sides()
r.sides()                            