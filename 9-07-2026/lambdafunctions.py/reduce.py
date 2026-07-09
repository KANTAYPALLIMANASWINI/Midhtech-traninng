from functools import reduce  #using normal function

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]

result = reduce(add, numbers)

print(result)


#using lambda functions
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]

result = reduce(add, numbers)

print(result)