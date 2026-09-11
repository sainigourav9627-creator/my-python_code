import json

with open("student.json", "r") as file:
    data = json.load(file)

data["city"] = "Meerut"

with open("student.json", "w") as file:
    json.dump(data, file)

print(data)
