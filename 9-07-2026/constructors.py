class Student:                      # Create a class named Student

    def __init__(self, name, age):  # Constructor called automatically when an object is created
        self.name = name            # Store name in the object
        self.age = age              # Store age in the object

    def display(self):              # Define a method to display object data
        print("Name", self.name)    # Print the object's name
        print("Age", self.age)      # Print the object's age

s1 = Student("Ravi", 20)            # Create an object and pass name & age

s1.display()                        # Call the display() method


# Employee class
class Employee:                          # Create a class named Employee

    def __init__(self, emp_id, name):    # Constructor
        self.emp_id = emp_id             # Store employee ID
        self.name = name                 # Store employee name

    def display(self):                   # Method to display details
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)

# Create an object
e1 = Employee(101, "Manaswini")          # Pass ID and name

# Call the method
e1.display()                             # Display employee details