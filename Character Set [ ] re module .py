import re

text = "apple banana cat"

result = re.findall(r"[ab]", text)

print(result)
