from abc import ABC
class Animal(ABC):
    def activity(self):
        pass
    def sound(self):
        pass   
class Snake(Animal):
    def activity(self):
        print("they are carnivorous")  
    def sound(self):
        print("hissing")
class Dog(Animal):
    def activity(self):
        pass
        super()
    print("dogs love to playing")
    def sound(self):
        pass
        super()
    print("bark")
class Cat(Animal):
    def activity(self):
        print("cat can jump up to 6 times their height")    
    def sound(self):
        pass
s=Snake()
d=Dog()
c=Cat()
for n in (s,d,c):
    n.activity()
    n.sound() 

   

                     