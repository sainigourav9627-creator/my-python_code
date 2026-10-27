marks = {
    "Hindi": 70,
    "English": 80,
    "Python": 90
}

highest = 0

for mark in marks.values():
    if mark > highest:
        highest = mark

print("Highest Marks:", highest)
