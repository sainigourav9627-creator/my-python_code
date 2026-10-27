student = {
    "Gourav": 85,
    "Amit": 90,
    "Rahul": 75
}

for name, marks in student.items():
    if marks == 90:
        print(name, marks)
        break
