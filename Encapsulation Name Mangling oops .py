class Student:
    def set_marks(self):
        self.__marks = 80


s1 = Student()

s1.set_marks()

print(s1._Student__marks)
