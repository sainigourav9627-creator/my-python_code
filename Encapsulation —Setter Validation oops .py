class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks


s1 = Student()

s1.set_marks(80)
print(s1.get_marks())

s1.set_marks(150)
print(s1.get_marks())
