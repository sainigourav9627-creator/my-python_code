import json

student = {
    "name": "Gourav",
    "age": 30,
    "course": "Python"
}

# Save
with open("student.json", "w") as file:
    json.dump(student, file)

# Read
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
