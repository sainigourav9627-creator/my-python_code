import os

file_name = "student.txt"

# 1. Check File
print("File Exists:", os.path.exists(file_name))

# 2. Read File
with open(file_name, "r") as file:
    data = file.read()

print("\n--- Original Data ---")
print(data)

# 3. Total Characters
print("\nTotal Characters:", len(data))

# 4. Total Lines
lines = data.splitlines()
print("Total Lines:", len(lines))

# 5. Total Words
words = data.split()
print("Total Words:", len(words))

# 6. Count Python
print("Python Count:", data.count("Python"))

# 7. Uppercase / Lowercase
upper = 0
lower = 0
digits = 0
spaces = 0

for char in data:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Spaces:", spaces)

# 8. Vowels
vowels = 0

for char in data.lower():
    if char in "aeiou":
        vowels += 1

print("Vowels:", vowels)

# 9. Consonants
consonants = 0

for char in data.lower():
    if char.isalpha() and char not in "aeiou":
        consonants += 1

print("Consonants:", consonants)

# 10. Print Lines with Line Number
print("\n--- Lines ---")

for number, line in enumerate(lines, start=1):
    print(number, line)

# 11. Find Python Line
for number, line in enumerate(lines, start=1):
    if "Python" in line:
        print("Python found in line:", number)

# 12. Copy File
with open(file_name, "r") as source:
    data = source.read()

with open("student_copy.txt", "w") as destination:
    destination.write(data)

print("\nFile copied successfully.")

# 13. Save Uppercase File
with open("uppercase.txt", "w") as file:
    file.write(data.upper())

print("Uppercase file created.")

# 14. File Size
print("File Size:", os.path.getsize(file_name), "bytes")

# 15. Absolute Path
print("File Path:", os.path.abspath(file_name))
