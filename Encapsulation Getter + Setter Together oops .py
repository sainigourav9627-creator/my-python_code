class Student:
    def __init__(self):
        self.__marks = 80

    # Setter
    def set_marks(self, marks):
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks


s1 = Student()

print(s1.get_marks())

s1.set_marks(90)

print(s1.get_marks())
