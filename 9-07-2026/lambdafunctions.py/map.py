numbers = [1, 2, 3, 4]   #using lambda

result = list(map(lambda x: x * x, numbers))

print(result)



#normal map function
def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)