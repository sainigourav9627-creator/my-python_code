class Student:
    def set_marks(self):
        self.__marks = 80

    def get_marks(self):
        return self.__marks


s1 = Student()

s1.set_marks()

print(s1.get_marks())
