import re

text = "   Python"

result = re.search(r"\S+", text)

print(result.group())
