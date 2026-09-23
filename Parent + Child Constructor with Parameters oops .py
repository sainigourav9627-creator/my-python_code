class Parent():
    def __init__(self, name):
        self.name = name                         # Parent Constructor Parameter

    def show(self):
        print("i like java")


class child(Parent):
    def __init__(self, name, age):
        super().__init__(name)                   # Parent Constructor Call
        self.age = age                           # Child Constructor Parameter

    def aman(self):
        print("this is python")


a = child("Gourav", 25)                          # Object + Arguments

print(a.name)                                    # Parent Data
print(a.age)                                     # Child Data
a.show()                                         # Parent Method
a.aman()                                         # Child Method
