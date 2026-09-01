import re

text = "Python java ruby"

result = re.findall(r"[a-z]+", text)

print(result)
