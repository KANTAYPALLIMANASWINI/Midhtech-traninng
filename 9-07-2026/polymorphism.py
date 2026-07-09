# # Define the Dog class
# class Dog:
#     def sound(self):
#         print("Dog barks")

# # Define the Cat class
# class Cat:
#     def sound(self):
#         print("Cat meows")

# # Create objects
# dog = Dog()
# cat = Cat()

# # Call the sound() method
# dog.sound()
# cat.sound()














class Animal:
    def sound(self):
        print("Animal makes a sound")  

class Dog(Animal):
    def sound(self):
        print("Dog barks")
    
class Cat(Animal):
    def sound(self):
        print("cat mewos")
animals=[Animal(),Dog(),Cat()]
for animal in animals:
    animal.sound()
def add(a,b=0,c=0):
    return a+b+c


print("add(s):",add(5))
print("add(5,10):",add(5,10))
print("add(5,10,15):",add(5,10,15))