class Student:
    def __init__(self, marks):
        self.marks = marks

    def __sub__(self, other):
        return self.marks - other.marks


s1 = Student(80)
s2 = Student(30)

print(s1 - s2)
