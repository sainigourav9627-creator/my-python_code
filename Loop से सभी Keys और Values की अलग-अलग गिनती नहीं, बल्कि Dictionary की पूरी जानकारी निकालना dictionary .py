marks = {
    "Gourav": 85,
    "Amit": 70,
    "Rahul": 90
}

total = 0

for name, mark in marks.items():
    print("Name:", name, "| Marks:", mark)
    total = total + mark

print("Total Marks:", total)
