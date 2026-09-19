class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

    @classmethod
    def show_count(cls):
        print(cls.count)


s1 = Student("Gourav")
s2 = Student("Amit")
s3 = Student("Rahul")

Student.show_count()
