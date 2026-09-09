import re

text = "I have 10 apples and 20 bananas"

matches = re.finditer(r"\d+", text)

for match in matches:
    print("Value:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
    print()
