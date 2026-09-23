class Parent():
    def show_parent(self):
        print("This is Parent")


class Child1(Parent):
    def show_child1(self):
        print("This is Child 1")


class Child2(Parent):
    def show_child2(self):
        print("This is Child 2")


class Child3(Child1, Child2):
    def show_child3(self):
        print("This is Child 3")


c = Child3()

c.show_parent()                         # Parent → inherited
c.show_child1()                         # Child1 → inherited
c.show_child2()                         # Child2 → inherited
c.show_child3()                         # Child3 → own
