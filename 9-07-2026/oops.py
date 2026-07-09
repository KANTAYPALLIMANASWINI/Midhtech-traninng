# Define a class named Student
class Student:

    # Define a method named display
    # self refers to the current object
    # name is a parameter passed to the method
    def display(self, name):

        # Print the student's name
        print("Student name:", name)

# Create the first object of the Student class
s1 = Student()

# Create the second object of the Student class
s2 = Student()

# Call the display() method using the first object
# "Manaswini" is passed as the name argument
s1.display("Manaswini")

# Call the display() method using the second object
# "Tejaswini" is passed as the name argument
s2.display("Tejaswini")