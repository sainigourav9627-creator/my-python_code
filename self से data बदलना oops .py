class Student:
    def change_name(self):
        self.name = "Rahul"

s1 = Student()
s1.name = "Gourav"

s1.change_name()

print(s1.name)
