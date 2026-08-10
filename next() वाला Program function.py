def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))
print(next(g))
print(next(g))
