class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls):
        cls.school = "XYZ School"


Student.change_school()

print(Student.school)
