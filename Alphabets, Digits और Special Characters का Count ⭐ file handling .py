with open("student.txt", "r") as file:
    data = file.read()

alphabets = 0
digits = 0
special = 0

for char in data:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special)
