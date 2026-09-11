import json

student = {
    "name": "Gourav",
    "marks": {
        "Python": 85,
        "Math": 78
    }
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["marks"]["Python"])
