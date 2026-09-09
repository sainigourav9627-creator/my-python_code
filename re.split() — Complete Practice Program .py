import re

# 1. Basic split
text = "Python Java C++"
result = re.split(r"\s+", text)
print("1.", result)


# 2. Comma से split
text = "Apple,Banana,Mango"
result = re.split(",", text)
print("2.", result)


# 3. Multiple spaces से split
text = "Python    Java     C++"
result = re.split(r"\s+", text)
print("3.", result)


# 4. Multiple separators से split
text = "Apple,Banana;Mango|Orange"
result = re.split(r"[,;|]", text)
print("4.", result)


# 5. maxsplit का use
text = "10 20 30 40"
result = re.split(r"\s+", text, maxsplit=2)
print("5.", result)


# 6. Hyphen से split
text = "10-20-30-40"
result = re.split("-", text)
print("6.", result)


# 7. Numbers के आधार पर split
text = "Python123Java456C++"
result = re.split(r"\d+", text)
print("7.", result)


# 8. Comma + spaces से split
text = "Apple, Banana, Mango, Orange"
result = re.split(r",\s*", text)
print("8.", result)


# 9. Date को split करना
date = "09-09-2026"
result = re.split(r"-", date)
print("9.", result)


# 10. सभी common separators से split
text = "Python,Java;C++|JavaScript"
result = re.split(r"[,;|]", text)
print("10.", result)
