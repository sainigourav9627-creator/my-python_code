def numbers():
    yield 10
    yield 20
    return
    yield 30

g = numbers()

print(next(g))
print(next(g))
