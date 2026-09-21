class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


s1 = Student(80)

print(s1.marks)

s1.marks = 90
print(s1.marks)

s1.marks = 150
print(s1.marks)
