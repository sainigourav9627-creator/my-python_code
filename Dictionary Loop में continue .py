marks = {
    "Gourav": 85,
    "Amit": 0,
    "Rahul": 90
}

for name, mark in marks.items():
    if mark == 0:
        continue
    print(name, mark)
