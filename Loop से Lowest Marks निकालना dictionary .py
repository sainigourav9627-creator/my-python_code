marks = {
    "Hindi": 70,
    "English": 80,
    "Python": 40
}

lowest = 100

for mark in marks.values():
    if mark < lowest:
        lowest = mark

print("Lowest Marks:", lowest)
