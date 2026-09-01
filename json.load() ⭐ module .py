json.load() ⭐

json.load() का काम है:

JSON file से data पढ़कर Python object में बदलना।

पहले हमने dump() से file में data लिखा था:


import json

data = {
    "name": "Gourav",
    "age": 32
}

with open("data.json", "w") as file:
    json.dump(data, file)
