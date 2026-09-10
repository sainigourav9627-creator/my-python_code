with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

count = {}

for word in words:
    word = word.strip(".,!?")

    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
