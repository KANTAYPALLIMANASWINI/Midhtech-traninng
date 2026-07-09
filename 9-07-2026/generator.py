def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)