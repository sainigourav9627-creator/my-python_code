with open("student.txt", "r") as file:
    data = file.read()

count = 0

for char in data:
    if char.isdigit():
        count += 1

print("Total digits:", count)
