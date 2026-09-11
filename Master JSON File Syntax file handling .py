import json

# File से data पढ़ना
with open("students.json", "r") as file:
    data = json.load(file)

# यहाँ Logic
# search / update / add / delete

# वापस file में save करना
with open("students.json", "w") as file:
    json.dump(data, file)
