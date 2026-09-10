with open("student.txt", "r") as file:
    data = file.read()

words = data.split()
lines = data.splitlines()

word_count = len(words)
line_count = len(lines)
char_count = len(data)
alphabet_count = 0
digit_count = 0
special_count = 0

for char in data:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isspace():
        special_count += 1

print("Total lines:", line_count)
print("Total words:", word_count)
print("Total characters:", char_count)
print("Alphabets:", alphabet_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
