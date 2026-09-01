import re

text = "Hello World"

result = re.search(r"\s+", text)

print(result.group())
