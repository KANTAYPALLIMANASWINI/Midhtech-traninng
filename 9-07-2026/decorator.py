def message(func):
    def wrapper():
        print("Welcome")
        func()
        print("Thank You")
    return wrapper

@message
def display():
    print("Learning Python")

display()