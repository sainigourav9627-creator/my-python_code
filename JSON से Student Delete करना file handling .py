import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    if student["name"] == "Rahul":
        students.remove(student)

with open("students.json", "w") as file:
    json.dump(students, file)

print("Student deleted")
