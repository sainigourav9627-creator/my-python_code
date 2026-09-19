class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


s1 = Student()
s2 = Student()

s1.change_school("XYZ School")

print(s1.school)
print(s2.school)
print(Student.school)
