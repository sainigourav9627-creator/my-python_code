import re

text = "Hello123"

result = re.search(r"\D+", text)

print(result.group())
