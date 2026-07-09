# Private Variable Example

class Student:

    def __init__(self):
        self.__marks = 95

    def display(self):
        print(self.__marks)   #__marks → Private variable.

obj = Student()

obj.display()