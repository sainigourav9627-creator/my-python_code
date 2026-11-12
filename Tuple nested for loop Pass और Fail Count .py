students = (
    ("Amit", 80),
    ("Ravi", 35),
    ("Gourav", 85),
    ("Anil", 30)
)

passed = 0
failed = 0

for name, marks in students:
    if marks >= 40:
        passed += 1
    else:
        failed += 1

print(passed)
print(failed)
