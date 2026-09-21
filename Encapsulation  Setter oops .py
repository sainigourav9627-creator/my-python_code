class Student:
    def __init__(self):
        self.__marks = 80

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s1 = Student()

print(s1.get_marks())

s1.set_marks(90)

print(s1.get_marks())
