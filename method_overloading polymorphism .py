class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


c = Calculator()

print(c.add(10, 20))
print(c.add(10, 20, 30))
