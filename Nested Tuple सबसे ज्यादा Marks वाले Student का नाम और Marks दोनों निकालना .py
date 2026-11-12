students = (
    ("Amit", 80),
    ("Ravi", 90),
    ("Gourav", 85)
)

topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

print("Name:", topper[0])
print("Marks:", topper[1])
