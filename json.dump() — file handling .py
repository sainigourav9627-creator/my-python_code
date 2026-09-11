import json

student = {
    "name": "Gourav",
    "age": 30,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("Data saved successfully")
