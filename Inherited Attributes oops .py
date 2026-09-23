class Parent():
    name = "Gourav"                  # Parent Attribute

    def show(self):
        print("i like java")


class child(Parent):
    def aman(self):
        print("this is python")


a = child()

print(a.name)       # Parent ka attribute
a.show()            # Parent ka method
a.aman()            # Child ka own method
