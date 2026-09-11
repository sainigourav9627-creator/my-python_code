import json

students = ["Gourav", "Rahul", "Amit", "Ravi"]

with open("students.json", "w") as file:
    json.dump(students, file)

print("List saved successfully")
