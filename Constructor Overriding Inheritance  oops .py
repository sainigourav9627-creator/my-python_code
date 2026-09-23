class Parent():
    def __init__(self):
        self.name = "Gourav"                 # Parent Constructor

    def show(self):
        print(self.name)


class Child(Parent):
    def __init__(self):
        self.age = 25                        # Child Constructor


c = Child()

print(c.age)                                 # Child Data
