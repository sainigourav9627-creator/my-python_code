class Student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show():
        print("Static Method")


s1 = Student("Gourav")
s1.show()
