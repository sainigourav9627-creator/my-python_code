class Parent():
    def show(self):
        print("i like java")


class child(Parent):
    def display(self):
        print("i am child")


c = child()

c.show()       # Parent method
c.display()    # Child method
