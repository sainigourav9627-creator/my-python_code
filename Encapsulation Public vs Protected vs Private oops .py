class Student:
    def __init__(self):
        self.name = "Gourav"        # Public
        self._age = 25              # Protected
        self.__marks = 80           # Private

    def show_private(self):
        print(self.__marks)


s1 = Student()

print(s1.name)          # Public
print(s1._age)          # Protected
s1.show_private()       # Private - class ke method se
