class Student:

    def set_data(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show(self):
        print(self.name)
        print(self.age)
        print(self.course)


s1 = Student()
s2 = Student()

s1.set_data("Gourav", 20, "BCA")
s2.set_data("Amit", 22, "MCA")

s1.show()
s2.show()
