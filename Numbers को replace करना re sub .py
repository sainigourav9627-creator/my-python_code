import re

text = "My mobile number is 9876543210"

result = re.sub(r"\d+", "XXXXXXXXXX", text)

print(result)
