students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 85)
)

search = "Gourav"

for name, marks in students:
    if name == search:
        print("Marks:", marks)
        break
else:
    print("Student Not Found")
