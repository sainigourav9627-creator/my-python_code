import re

# 1. Pattern compile करना
pattern = re.compile(r"\d+")

text = "My marks are 85 and 90"

result = pattern.findall(text)
print("1.", result)


# 2. Compiled pattern + search()
text = "My age is 32"

match = pattern.search(text)
print("2.", match.group())


# 3. Compiled pattern + match()
text = "123abc"

match = pattern.match(text)
print("3.", match.group())


# 4. Compiled pattern + findall()
text = "10 20 30 40"

result = pattern.findall(text)
print("4.", result)


# 5. Compiled pattern + finditer()
text = "I have 10 apples and 20 bananas"

matches = pattern.finditer(text)

print("5.")
for match in matches:
    print(match.group(), match.span())


# 6. दूसरा pattern compile करना
word_pattern = re.compile(r"[A-Za-z]+")

text = "Python 2026"

result = word_pattern.findall(text)
print("6.", result)


# 7. Compiled pattern से numbers replace करना
number_pattern = re.compile(r"\d+")

text = "My marks are 85 and 90"

result = number_pattern.sub("XX", text)
print("7.", result)


# 8. Compiled pattern से split करना
space_pattern = re.compile(r"\s+")

text = "Python   Java   C++"

result = space_pattern.split(text)
print("8.", result)
