import json

with open("students.json", "r") as file:
    students = json.load(file)

new_student = {
    "name": "Suresh",
    "age": 27,
    "marks": 88
}

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file)

print("New student added")
