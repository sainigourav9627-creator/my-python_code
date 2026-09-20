class Student:

    @staticmethod
    def check_marks(marks):
        if marks >= 33:
            return "Pass"
        else:
            return "Fail"


print(Student.check_marks(75))
print(Student.check_marks(25))
