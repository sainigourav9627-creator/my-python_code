json.dump() ⭐

ध्यान से — dump() और dumps() अलग हैं।

dumps() → JSON string बनाता है
dump()  → JSON data को file में लिखता है

import json

data = {
    "name": "Gourav",
    "age": 32
}

with open("data.json", "w") as file:
    json.dump(data, file)
