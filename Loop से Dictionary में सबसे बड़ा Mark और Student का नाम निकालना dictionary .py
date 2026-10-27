marks = {
    "Gourav": 85,
    "Amit": 95,
    "Rahul": 75
}

highest = 0
topper = ""

for name, mark in marks.items():
    if mark > highest:
        highest = mark
        topper = name

print("Topper:", topper)
print("Highest Marks:", highest)
