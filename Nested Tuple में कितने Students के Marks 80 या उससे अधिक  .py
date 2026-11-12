students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 55),
    ("Anil", 70)
)

count = 0

for name, marks in students:
    if marks >= 80:
        count += 1

print(count)
