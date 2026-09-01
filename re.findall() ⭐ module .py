import re

text = "I have 10 apples and 20 bananas"

result = re.findall(r"\d+", text)

print(result)
