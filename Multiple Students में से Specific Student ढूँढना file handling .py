import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    if student["name"] == "Rahul":
        print(student)
