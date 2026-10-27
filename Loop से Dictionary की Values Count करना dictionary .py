marks = {
    "Hindi": 60,
    "English": 80,
    "Python": 90,
    "Maths": 50
}

count = 0

for mark in marks.values():
    if mark >= 70:
        count = count + 1

print("Count:", count)
