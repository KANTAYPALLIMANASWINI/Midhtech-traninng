#Write to a File ("w" mode)
file = open("student.txt", "w")

file.write("Hello Manaswini")

file.close()

#Read from a File ("r" mode)
file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


#Append to a File ("a" mode)
file = open("student.txt", "a")

file.write("\nWelcome to Python")

file.close()



