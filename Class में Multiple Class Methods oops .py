class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.show_school()

Student.change_school("XYZ School")

Student.show_school()
