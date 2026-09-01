import re

text = "Python@123"

result = re.search(r"\W+", text)

print(result.group())
