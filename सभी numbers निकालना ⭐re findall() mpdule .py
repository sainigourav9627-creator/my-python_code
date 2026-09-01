import re

text = "Math 85, English 90, Science 78"

result = re.findall(r"\d+", text)

print(result)
