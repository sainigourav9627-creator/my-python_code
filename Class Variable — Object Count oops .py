class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


s1 = Student("Gourav")
s2 = Student("Amit")
s3 = Student("Rahul")

print(Student.count)
