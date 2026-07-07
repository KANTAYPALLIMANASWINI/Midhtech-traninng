import math

print("Scientific Calculator")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("sqrt  Square Root")
print("square  Square")
print("power  Power")
print("sin  Sine")
print("cos  Cosine")
print("tan  Tangent")
print("fact  Factorial")

operation = input("Enter operation: ")

if operation == "+":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a + b)

elif operation == "-":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a - b)

elif operation == "*":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a * b)

elif operation == "/":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a / b)

elif operation == "sqrt":
    a = float(input("Enter a number: "))
    print("Answer =", math.sqrt(a))

elif operation == "square":
    a = float(input("Enter a number: "))
    print("Answer =", a * a)

elif operation == "power":
    a = float(input("Enter base: "))
    b = float(input("Enter power: "))
    print("Answer =", math.pow(a, b))

elif operation == "sin":
    a = float(input("Enter angle in degrees: "))
    print("Answer =", math.sin(math.radians(a)))

elif operation == "cos":
    a = float(input("Enter angle in degrees: "))
    print("Answer =", math.cos(math.radians(a)))

elif operation == "tan":
    a = float(input("Enter angle in degrees: "))
    print("Answer =", math.tan(math.radians(a)))

elif operation == "fact":
    a = int(input("Enter a number: "))
    print("Answer =", math.factorial(a))

else:
    print("Invalid Operation")