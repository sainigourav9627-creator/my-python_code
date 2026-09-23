class Parent():
    def __init__(self):
        self.name = "Gourav"

    def show(self):
        print("i like java")                 # Parent Method


class child(Parent):
    def __init__(self):
        super().__init__()                   # Parent Constructor Call
        self.age = 25

    def show(self):
        super().show()                       # Parent Method Call
        print("this is child show")          # Child Method


    def aman(self):
        print("this is python")              # Child Method


a = child()

print(a.name)
print(a.age)

a.show()                                     # Child show → Parent show भी call
a.aman()
