import re

text = "My marks are 85, 90 and 76"

matches = re.finditer(r"\d+", text)

for match in matches:
    print("Number:", match.group())
