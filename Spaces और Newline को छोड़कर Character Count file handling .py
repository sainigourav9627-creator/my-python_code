with open("student.txt", "r") as file:
    data = file.read()

count = 0

for char in data:
    if not char.isspace():
        count += 1

print("Characters without spaces/newlines:", count)
