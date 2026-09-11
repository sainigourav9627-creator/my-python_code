import json

students = [
    {"name": "Gourav", "age": 30, "marks": 85},
    {"name": "Rahul", "age": 25, "marks": 90}
]

# 1. Save JSON
with open("students.json", "w") as file:
    json.dump(students, file)

# 2. Load JSON
with open("students.json", "r") as file:
    students = json.load(file)

# 3. Search + Update
for student in students:
    if student["name"] == "Rahul":
        print("Found:", student)
        student["marks"] = 95

# 4. Add new student
new_student = {
    "name": "Amit",
    "age": 28,
    "marks": 80
}

students.append(new_student)

# 5. Delete student
for student in students:
    if student["name"] == "Amit":
        students.remove(student)
        break

# 6. Save updated data
with open("students.json", "w") as file:
    json.dump(students, file)

print("Final data:", students)
