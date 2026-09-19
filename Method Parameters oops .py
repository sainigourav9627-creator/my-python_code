class Student:

    def set_data(self, name, age, course):
        self.name = "Gourav"
        self.age = 20

    def show(self):
        print(self.name)
        print(self.age)

s1 = Student()

s1.set_data("Gourav", 20, "BCA")
s1.show()
