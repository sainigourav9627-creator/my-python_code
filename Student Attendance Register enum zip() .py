students = ["Gourav", "Aman", "Rahul", "Amit"]
attendance = ["Present", "Absent", "Present", "Present"]

result = enumerate(zip(students, attendance),start = 101)

print(dict(result))
