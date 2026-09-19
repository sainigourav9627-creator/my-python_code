class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls):
        cls.school = "XYZ School"


s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

Student.change_school()

print(s1.school)
print(s2.school)
