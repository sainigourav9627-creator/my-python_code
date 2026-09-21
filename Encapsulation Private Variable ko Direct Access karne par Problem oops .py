class Student:
    def set_marks(self):
        self.__marks = 80

    def show_marks(self):
        print(self.__marks)


s1 = Student()

s1.set_marks()
s1.show_marks()
