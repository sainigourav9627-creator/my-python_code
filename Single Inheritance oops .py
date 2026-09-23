class Parent():
    def show(self):
        print("This is Parent")


class Child(Parent):
    def display(self):
        print("This is Child")


c = Child()

c.show()             # Parent Method → Inherited
c.display()          # Child Method → Own
