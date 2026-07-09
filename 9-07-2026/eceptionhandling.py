# Exception Handling Example

try:
    # Initialize variables
    a = 10
    b = 0                    # Change to 0 to raise ZeroDivisionError

    # Create a list
    list1 = [10, 20, 30]

    # Perform division
    print("Division:", a / b)

    # Access list element
    print("List Value:", list1[5])     #  IndexError

    # Convert string to integer
    num = int("abc")                    # raise ValueError
    print("Number:", num)

    # Open and read a file
    file = open("student.txt", "r")    # Change to "abc.txt" to raise FileNotFoundError
    print(file.read())
    file.close()

    # Add two numbers
    result = 10 + "20"                  # Change to 10 + "20" to raise TypeError
    print("Addition:", result)

# Handles divide by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handles invalid list index
except IndexError:
    print("Error: List index out of range.")

# Handles invalid value conversion
except ValueError:
    print("Error: Invalid value.")

# Handles file not found
except FileNotFoundError:
    print("Error: File not found.")

# Handles invalid data type operation
except TypeError:
    print("Error: Invalid data type.")

# Executes whether an exception occurs or not
finally:
    print("Program completed.")