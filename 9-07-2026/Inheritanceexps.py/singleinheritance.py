# Single Inheritance

class Parent:
    def display(self):
        print("I am Parent")

class Child(Parent):
    def show(self):
        print("I am Child")

obj = Child()

obj.display()
obj.show()
