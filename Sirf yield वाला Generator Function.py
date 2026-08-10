def numbers():
    yield 10
    yield 20
    yield 30

for x in numbers():
    print(x)
