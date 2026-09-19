class Student:

    school = "ABC School"

    def show_student(self):
        print("Instance Method")
        print(self)

    @classmethod
    def show_class(cls):
        print("Class Method")
        print(cls)


s1 = Student()

s1.show_student()
Student.show_class()
