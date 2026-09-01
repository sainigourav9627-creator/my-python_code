json.loads() ⭐

loads() का काम:

JSON string → Python object


import json

data = '{"name": "Gourav", "age": 32}'

result = json.loads(data)

print(result)
print(type(result))
