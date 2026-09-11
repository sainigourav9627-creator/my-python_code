import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    if student["name"] == "Rahul":
        student["marks"] = 95

with open("students.json", "w") as file:
    json.dump(students, file)

print("Record updated")
