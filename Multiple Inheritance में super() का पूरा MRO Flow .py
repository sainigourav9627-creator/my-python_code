class Parent1:
    def show(self):
        print("Parent 1")
        super().show()

class Parent2:
    def show(self):
        print("Parent 2")

class Child(Parent1, Parent2):
    def show(self):
        print("Child")
        super().show()

c = Child()
c.show()
