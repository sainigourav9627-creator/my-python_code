import re

text = "Python_123"

result = re.search(r"\w+", text)

print(result.group())
