def numbers():
    yield 10
    yield 20
    yield 30

def get_numbers():
    return numbers()

g = get_numbers()

print(next(g))
print(next(g))
print(next(g))
