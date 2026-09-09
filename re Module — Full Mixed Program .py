import re

text = """
Name: Gourav Kumar
Age: 32
Mobile: 9876543210
Email: gourav@gmail.com
Skills: Python, Java, SQL
"""

# 1. search() → Email ढूँढना
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)

if email:
    print("Email:", email.group())


# 2. match() → शुरुआत में Name check करना
name_check = re.match(r"\s*Name:\s*(.+)", text)

if name_check:
    print("Name:", name_check.group(1))


# 3. findall() → सभी numbers निकालना
numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)


# 4. finditer() → Numbers की position
print("\nNumber Positions:")

for match in re.finditer(r"\d+", text):
    print(match.group(), match.span())


# 5. sub() → Mobile number hide करना
hidden_text = re.sub(r"\d{10}", "XXXXXXXXXX", text)

print("\nAfter Hiding Mobile:")
print(hidden_text)


# 6. split() → Skills अलग करना
skills = "Python,Java,SQL"

skill_list = re.split(r",\s*", skills)

print("Skills:", skill_list)


# 7. compile() → Mobile pattern तैयार करना
mobile_pattern = re.compile(r"[6-9]\d{9}")

mobile = "9876543210"

if mobile_pattern.fullmatch(mobile):
    print("Mobile: Valid")
else:
    print("Mobile: Invalid")


# 8. Character Class + Quantifier
# सिर्फ Name में letters निकालना
name = "Gourav123"

letters = re.findall(r"[A-Za-z]+", name)

print("Name Letters:", letters)


# 9. Whitespace pattern
clean_text = re.sub(r"\s+", " ", text).strip()

print("\nClean Text:")
print(clean_text)
