with open("student.txt", "r") as file:
    data = file.read()

count = {}

for char in data:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
