class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Anil", 25, "Python")
s2 = Student("Amit", 30, "Java")

print(s1.name)
print(s2.name)
print(s1.age)
print(s2.age)
print(s1.course)
print(s2.course)
