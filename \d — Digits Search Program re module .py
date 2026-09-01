import re

text = "My age is 32"

result = re.search(r"\d+", text)

print(result.group())
