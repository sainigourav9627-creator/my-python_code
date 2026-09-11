import json

with open("student.json", "r") as file:
    data = json.load(file)

data["marks"]["Python"] = 95

with open("student.json", "w") as file:
    json.dump(data, file)

print("Marks updated")
