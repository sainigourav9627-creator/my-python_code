class Student:

    school = "ABC School"

    def change_school(self):
        Student.school = "XYZ School"

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

s1.change_school()

print(s1.school)
print(s2.school)
