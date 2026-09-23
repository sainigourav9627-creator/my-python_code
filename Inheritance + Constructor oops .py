class Parent():
    def __init__(self):
        self.name = "Gourav"             # Parent Instance Variable

    def show(self):
        print("i like java")             # Parent Method


class child(Parent):
    def aman(self):
        print("this is python")          # Child Method


a = child()                              # Child Object

print(a.name)                            # Parent ka Instance Variable
a.show()                                 # Parent Method → Inherited
a.aman()                                 # Child Method → Own
