class Parent1:
    def show(self):
        print("Parent 1")

class Parent2:
    def show(self):
        print("Parent 2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.show()
