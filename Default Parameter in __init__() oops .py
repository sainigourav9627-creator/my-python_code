class Student:
    def __init__(self, name, course="Python"):
        self.name = name
        self.course = course

s1 = Student("Anil")
s2 = Student("Amit", "Java")

print(s1.name)
print(s1.course)

print(s2.name)
print(s2.course)
