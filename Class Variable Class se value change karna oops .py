class Student:

    school = "ABC School"


s1 = Student()
s2 = Student()

Student.school = "XYZ School"

print(s1.school)
print(s2.school)
