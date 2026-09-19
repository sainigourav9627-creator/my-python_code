class Student:

    school = "ABC School"          # Class Variable

    def __init__(self, name, age):
        self.name = name           # Instance Variable
        self.age = age             # Instance Variable


s1 = Student("Gourav", 25)
s2 = Student("Amit", 21)

print(s1.name)
print(s1.age)
print(s1.school)

print(s2.name)
print(s2.age)
print(s2.school)
