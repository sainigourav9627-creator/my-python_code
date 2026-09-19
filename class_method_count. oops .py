class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

    @classmethod
    def reset_count(cls):
        cls.count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)


s1 = Student("Gourav")
s2 = Student("Amit")

Student.show_count()

Student.reset_count()

Student.show_count()
