#data abstraction
#abc-abstract base class
from abc import ABC
class Car(ABC):
    def mileage(self):
        pass
class Truck(ABC):
    def mileage(self):
        print("25 kmph")
class Bike(ABC):
    def mileage(self):
        print("30 kmph")
class Cycle(ABC):
    def mileage(self):
        print("10 kmph")      
t=Truck()
b=Bike()
c=Cycle()                  
t.mileage()
b.mileage()
c.mileage()


