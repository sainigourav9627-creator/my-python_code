import re

text = "I LOVE PYTHON"

result = re.findall(r"[A-Z]+", text)

print(result)
