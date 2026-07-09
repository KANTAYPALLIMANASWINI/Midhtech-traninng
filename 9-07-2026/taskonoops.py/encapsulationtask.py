# Encapsulation example
class Student:
    def __init__(self, name, age, marks, result):
        self.name = name              # Public variable
        self.age = age                # Public variable
        self.__marks = marks          # Private variable
        self.__result = result        # Private variable

    def display(self):                # Public method
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.__marks)
        print("Result:", self.__result)

# Create object
s1 = Student("Ravi", 20, 75, "Pass")

# Call method
s1.display()