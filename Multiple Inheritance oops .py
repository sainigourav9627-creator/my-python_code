class Parent1():
    def show1(self):
        print("This is Parent 1")       # Parent 1 Method


class Parent2():
    def show2(self):
        print("This is Parent 2")       # Parent 2 Method


class Child(Parent1, Parent2):
    pass


c = Child()

c.show1()                               # Parent 1 → Inherited
c.show2()                               # Parent 2 → Inherited
