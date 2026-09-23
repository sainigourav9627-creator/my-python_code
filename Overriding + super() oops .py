class Parent():
    def show(self):
        print("This is Parent")             # Parent Method


class Child(Parent):
    def show(self):
        super().show()                      # Parent ka overridden method call
        print("This is Child")              # Child ka own version


c = Child()

c.show()                                    # Child show() call
