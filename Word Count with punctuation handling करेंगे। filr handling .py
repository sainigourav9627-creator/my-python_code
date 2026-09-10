with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

count = 0

for word in words:
    word = word.strip(".,!?")

    if word == "Python":
        count += 1

print("Python count:", count)
