from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def display(self):
        pass

class Result(Student):

    def display(self):
        print("Name: Ravi")
        print("Age: 20")
        print("Marks: 75")
        print("Result: Pass")

s1 = Result()
s1.display()