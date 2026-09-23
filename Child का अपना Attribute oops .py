class Parent():
    name = "Gourav"                    # Parent Attribute

    def show(self):
        print("i like java")           # Parent Method


class child(Parent):
    age = 25                           # Child ka Own Attribute

    def aman(self):
        print("this is python")        # Child Method


a = child()                            # Child Object

a.show()                               # Parent Method → Inherited
a.aman()                               # Child Method → Own
print(a.name)                          # Parent Attribute → Inherited
print(a.age)                           # Child Attribute → Own
