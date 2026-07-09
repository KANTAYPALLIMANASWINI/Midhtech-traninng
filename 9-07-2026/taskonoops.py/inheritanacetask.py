# Parent class
class Student:
    def __init__(self, name, age):
        self.name = name      # Store name
        self.age = age        # Store age

# Child class
class Result(Student):
    def __init__(self, name, age, marks, result):
        self.name = name          # Store name
        self.age = age            # Store age
        self.marks = marks        # Store marks
        self.result = result      # Store result

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Result:", self.result)

# Create object
s1 = Result("Ravi", 20, 75, "Pass")

# Call method
s1.display()