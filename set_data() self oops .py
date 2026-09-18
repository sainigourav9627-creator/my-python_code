class Student:

    def set_data(self):
        self.name = "Gourav"

    def show(self):
        print(self.name)


s1 = Student()
s2 = Student()

s1.set_data()
s2.name = "Amit"

s1.show()
s2.show()
