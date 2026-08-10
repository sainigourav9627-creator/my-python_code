def test():
    yield 5
    return
    yield 10

for x in test():
    print(x)
