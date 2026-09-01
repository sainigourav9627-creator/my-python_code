import json

student = {
    "name": "Gourav",
    "age": 32,
    "course": "Python",
    "marks": 85
}

# JSON file में save
with open("student.json", "w") as file:
    json.dump(student, file)

# JSON file से read
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
