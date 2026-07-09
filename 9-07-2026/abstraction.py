from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod   #abstact method
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
car1=Car()
car1.start()