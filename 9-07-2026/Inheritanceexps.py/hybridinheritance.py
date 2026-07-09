# Hybrid Inheritance

class GrandParent:
    def grand(self):
        print("Grand Parent")

class Father(GrandParent):
    def father(self):
        print("Father")

class Mother(GrandParent):
    def mother(self):
        print("Mother")

class Child(Father, Mother):
    def child(self):
        print("Child")

obj = Child()

obj.grand()
obj.father()
obj.mother()
obj.child()
