import json

with open("students.json", "r") as file:
    students = json.load(file)

print(students)
print(students[0])
