class Parent():
    def show(self):
        print("This is Parent")          # Parent Method


class Child1(Parent):
    def show1(self):
        print("This is Child 1")         # Child1 Method


class Child2(Parent):
    def show2(self):
        print("This is Child 2")         # Child2 Method


c1 = Child1()
c2 = Child2()

c1.show()                                # Parent Method → Child1 gets it
c1.show1()                               # Child1 Method → Own

c2.show()                                # Parent Method → Child2 gets it
c2.show2()                               # Child2 Method → Own
