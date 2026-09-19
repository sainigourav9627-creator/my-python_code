class Student:

    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        print(Student.school)


s1 = Student("Gourav", 25)
s2 = Student("Amit", 21)

s1.show()
s2.show()
