class Parent:
    pass

class Child(Parent):
    pass

c = Child()

print(isinstance(c, Child))
print(isinstance(c, Parent))

print(issubclass(Child, Parent))
print(issubclass(Child, Child))
