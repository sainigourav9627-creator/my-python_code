import json

with open("student.json", "r") as file:
    data = json.load(file)

del data["city"]

with open("student.json", "w") as file:
    json.dump(data, file)

print("City deleted")
