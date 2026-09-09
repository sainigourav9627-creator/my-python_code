import re

text = "I like tea. Tea is good."

result = re.sub(r"Tea", "Coffee", text)

print(result)
