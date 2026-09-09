import re

# 1. Basic word replacement
text = "I like Java"
result = re.sub("Java", "Python", text)
print("1.", result)


# 2. Numbers replace करना
text = "My marks are 85 and 90"
result = re.sub(r"\d+", "XX", text)
print("2.", result)


# 3. count का use
text = "10 20 30 40"
result = re.sub(r"\d+", "X", text, count=2)
print("3.", result)


# 4. Word replace करना
text = "I like Tea. Tea is good."
result = re.sub(r"Tea", "Coffee", text)
print("4.", result)


# 5. सभी spaces replace करना
text = "Hello Python World"
result = re.sub(r"\s+", "-", text)
print("5.", result)


# 6. Special characters हटाना
text = "Hello@Python#2026!"
result = re.sub(r"[^A-Za-z0-9 ]", "", text)
print("6.", result)


# 7. Mobile number hide करना
text = "My mobile number is 9876543210"
result = re.sub(r"\d{10}", "XXXXXXXXXX", text)
print("7.", result)


# 8. Multiple numbers को replace करना
text = "I have 10 apples, 20 bananas and 30 oranges"
result = re.sub(r"\d+", "NUMBER", text)
print("8.", result)
