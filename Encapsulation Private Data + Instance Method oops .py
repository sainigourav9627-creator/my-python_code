class Student:
    def __init__(self, marks):
        self.__marks = marks

    def show_result(self):
        if self.__marks >= 33:
            print("Pass")
        else:
            print("Fail")


s1 = Student(80)

s1.show_result()
