students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 55)
)

for name, marks in students:
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"

    print(name, grade)
