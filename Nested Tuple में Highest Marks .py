students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 85)
)

highest = 0

for name, marks in students:
    if marks > highest:
        highest = marks

print(highest)
