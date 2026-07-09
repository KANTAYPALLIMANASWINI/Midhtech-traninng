# Protected Variable Example

class Parent:

    def __init__(self):
        self._name = "Manaswini"   # Protected variable

class Child(Parent):

    def display(self):
        print("Name:", self._name)

obj = Child()

obj.display()