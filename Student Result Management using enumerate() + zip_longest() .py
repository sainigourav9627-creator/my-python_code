from itertools import zip_longest

students = ["Aman", "Rahul", "Rohit", "Vikas"]
marks = [75, 35, 90]

result = enumerate(
    zip_longest(students, marks, fillvalue=0),
    start=1
)
for roll, (name, mark) in result:

    if mark >= 40:
        print(roll, name, "Pass")
    else:
        print(roll, name, "Fail")
