class Parent():
    def __init__(self):
        self.name = "Gourav"             # Parent Constructor

    def show(self):
        print("i like java")             # Parent Method


class child(Parent):
    def __init__(self):
        super().__init__()               # Parent Constructor Call
        self.age = 25                    # Child Constructor

    def aman(self):
        print("this is python")          # Child Method


a = child()                              # Child Object

print(a.name)                            # Parent Variable
print(a.age)                             # Child Variable
a.show()                                 # Parent Method
a.aman()                                 # Child Method
