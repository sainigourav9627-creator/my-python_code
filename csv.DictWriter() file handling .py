import csv

students = [
    {"name": "Gourav", "age": 30, "marks": 85},
    {"name": "Rahul", "age": 25, "marks": 90}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Data saved")
