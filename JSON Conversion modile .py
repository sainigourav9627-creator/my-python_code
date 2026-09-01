Python ↔ JSON Conversion

जब हम json.dumps() करते हैं, Python की values JSON values में convert होती हैं।

| Python  | JSON    |
| ------- | ------- |
| `dict`  | object  |
| `list`  | array   |
| `tuple` | array   |
| `str`   | string  |
| `int`   | number  |
| `float` | number  |
| `True`  | `true`  |
| `False` | `false` |
| `None`  | `null`  |

  import json

data = {
    "name": "Gourav",
    "age": 32,
    "active": True,
    "skills": ["Python", "SQL"],
    "value": None
}


    JSON के 4 functions — Final Chart

    
dumps() → Python → JSON String
loads() → JSON String → Python

dump()  → Python → JSON File
load()  → JSON File → Python


