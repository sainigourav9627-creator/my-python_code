import re

text = "My age is 32"

match = re.search(r"\d+", text)

print(match)
print(match.group())
