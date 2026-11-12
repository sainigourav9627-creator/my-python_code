students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 85)
)

for name, marks in students:
    percentage = marks / 100 * 100
    print(name, percentage)
