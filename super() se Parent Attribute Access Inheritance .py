class Parent:
    name = "Gourav"

class Child(Parent):
    name = "Amit"

    def show(self):
        print(self.name)
        print(super().name)

c = Child()
c.show()
