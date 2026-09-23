class Parent():
    def __init__(self):
        self.name = "Gourav"             # Parent Constructor

    def show(self):
        print("i like java")             # Parent Method


class child(Parent):
    def __init__(self):
        self.age = 25                    # Child Constructor

    def aman(self):
        print("this is python")          # Child Method


a = child()                              # Child Object

print(a.age)                             # Child Instance Variable
a.show()                                 # Parent Method
a.aman()                                 # Child Method
