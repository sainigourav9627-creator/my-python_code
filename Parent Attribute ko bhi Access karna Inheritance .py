class Parent:
    name = "Gourav"

class Child(Parent):
    name = "Amit"

c = Child()

print(c.name)       # Child ka name
print(Parent.name)  # Parent ka name
