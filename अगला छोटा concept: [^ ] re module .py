import re

text = "abc123"

result = re.findall(r"[^0-9]+", text)

print(result)
