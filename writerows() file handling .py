import csv

students = [
    ["Gourav", 30, 85],
    ["Rahul", 25, 90],
    ["Amit", 28, 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Data saved")
