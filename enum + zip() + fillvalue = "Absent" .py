from itertools import zip_longest

students = ["Aman", "Rahul", "Rohit", "Vikas"]
marks = [85, 90]

result = zip_longest(students, marks, fillvalue="Absent")


print(dict(result))
