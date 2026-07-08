 # basic function
# def  welcome_message():
#     print("Welcome to the python class")
#     print("Today we are learning functions")
# welcome_message()


# #prime number function
# def is_prime(num):
#     if num <= 1:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True


# num = int(input("Enter a number: "))

# if is_prime(num):
#     print(num, "is a Prime Number")
# else:
#     print(num, "is Not a Prime Number")

# is_prime(num)




# ## simple function using  arguments
# def student_details(name, course_name):
#     return "Student Name: " + name + "\nCourse Name: " + course_name

# name = "Manaswini"
# course_name = "Telugu"

# print(student_details(name, course_name))


# # Addition using function

# def add(a, b):
#     return a + b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = add(num1, num2)

# print("Sum =", result)

# # subtraction using function

# def sub(a, b):
#     return a - b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = sub(num1, num2)

# print("Subraction =", result)


# # multiplication using function

# def MUL(a, b):
#     return a * b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = MUL(num1, num2)

# print("Multiplication=", result)


# # Division using function

# def DIV(a, b):
#     return a / b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = Division(num1, num2)

# print("DIV =", result)  


#normal functions to  print prime without using parameters and arguments
# Prime number without parameters and arguments

def prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a Prime Number")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            return

    print("Prime Number")


prime()

