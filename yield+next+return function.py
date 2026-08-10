def numbers():
    yield 10
    return
    yield 20

g = numbers()

print(next(g))
print(next(g))


10

Traceback (most recent call last):
  File "<main.py>", line 9, in <module>
StopIteration
