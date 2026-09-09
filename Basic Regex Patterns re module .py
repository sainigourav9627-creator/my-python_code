import re

text = "Python 123 is easy. My age is 32."


# 1. Literal character
print("1.", re.findall(r"Python", text))


# 2. . (dot) — कोई भी एक character
print("2.", re.findall(r"P.thon", text))


# 3. ^ — text की शुरुआत
print("3.", re.findall(r"^Python", text))


# 4. $ — text का अंत
text2 = "I love Python"
print("4.", re.findall(r"Python$", text2))


# 5. \d — digit
print("5.", re.findall(r"\d", text))


# 6. \D — non-digit
print("6.", re.findall(r"\D", "ABC123"))


# 7. \w — word character
print("7.", re.findall(r"\w", "Python_123"))


# 8. \W — non-word character
print("8.", re.findall(r"\W", "Hello @ Python!"))


# 9. \s — whitespace
print("9.", re.findall(r"\s", "Hello Python World"))


# 10. \S — non-whitespace
print("10.", re.findall(r"\S+", "Hello Python World"))
