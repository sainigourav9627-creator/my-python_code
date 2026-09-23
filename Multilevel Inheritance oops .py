class Grandparent():
    def grand_show(self):
        print("This is Grandparent")          # Grandparent Method


class Parent(Grandparent):
    def parent_show(self):
        print("This is Parent")                # Parent Method


class Child(Parent):
    def child_show(self):
        print("This is Child")                 # Child Method


c = Child()

c.grand_show()                                # Grandparent Method → Inherited
c.parent_show()                               # Parent Method → Inherited
c.child_show()                                # Child Method → Own
