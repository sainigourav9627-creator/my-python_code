def mix():
    yield 10+20
    yield 10-2
    yield 10*2
g = mix()
print(next(g))
print(next(g))
print(next(g))
