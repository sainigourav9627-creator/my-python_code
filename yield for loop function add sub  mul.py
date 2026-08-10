def mix():
    yield 10+20
    yield 10-2
    yield 10*2
for x in mix():
    print(x)
