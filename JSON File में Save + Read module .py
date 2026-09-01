import json

data = {
    "name": "Gourav",
    "age": 32,
    "course": "Python"
}

# Data save करना
with open("student.json", "w") as file:
    json.dump(data, file)

# Data read करना
with open("student.json", "r") as file:
    result = json.load(file)

print(result)
