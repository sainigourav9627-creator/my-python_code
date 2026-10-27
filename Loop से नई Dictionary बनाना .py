marks = {
    "Gourav": 85,
    "Amit": 55,
    "Rahul": 90,
    "Sumit": 40
}

passed = {}

for name, mark in marks.items():
    if mark >= 70:
        passed[name] = mark

print(passed)
