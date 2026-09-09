import re

text = "Python 123 Java ABC xyz"


# 1. [abc] — दिए गए characters में से कोई एक
print("1.", re.findall(r"[abc]", "apple"))


# 2. [a-z] — lowercase letters
print("2.", re.findall(r"[a-z]", text))


# 3. [A-Z] — uppercase letters
print("3.", re.findall(r"[A-Z]", text))


# 4. [0-9] — digits
print("4.", re.findall(r"[0-9]", text))


# 5. [a-zA-Z] — lowercase + uppercase
print("5.", re.findall(r"[a-zA-Z]", text))


# 6. [^...] — दिए गए characters को छोड़कर
print("6.", re.findall(r"[^0-9]", "ABC123"))


# 7. Character combination
print("7.", re.findall(r"[A-Z][a-z]+", "Hello Python Java"))


# 8. सिर्फ vowels
print("8.", re.findall(r"[aeiou]", "Hello Python"))


# 9. सिर्फ consonants
print("9.", re.findall(r"[^aeiou\s]", "Hello Python"))
