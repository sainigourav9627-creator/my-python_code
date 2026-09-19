class Student:

    school = "ABC School"

    def show(self):
        print(self.school)
        print(Student.school)


s1 = Student()

s1.show()
