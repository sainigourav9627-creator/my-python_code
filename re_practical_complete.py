import re

print("===== 1. MOBILE NUMBER =====")

mobile = "9876543210"

if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


print("\n===== 2. EMAIL =====")

email = "gourav@gmail.com"

if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")


print("\n===== 3. USERNAME =====")

username = "Gourav123"

if re.fullmatch(r"[A-Za-z0-9_]{3,15}", username):
    print("Valid Username")
else:
    print("Invalid Username")


print("\n===== 4. PASSWORD =====")

password = "Gourav@123"

if re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%]).{8,}", password):
    print("Strong Password")
else:
    print("Weak Password")


print("\n===== 5. PIN =====")

pin = "2445"

if re.fullmatch(r"\d{4}", pin):
    print("Valid PIN")
else:
    print("Invalid PIN")


print("\n===== 6. DATE =====")

date = "09-09-2026"

if re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")


print("\n===== 7. FIND NUMBERS =====")

text = "I have 10 apples and 20 bananas."

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)


print("\n===== 8. FIND EMAIL =====")

text = "My email is gourav@gmail.com"

result = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)

if result:
    print("Email Found:", result.group())
else:
    print("Email Not Found")
