with open("student.txt", "r") as file:
    lines = file.readlines()

count = 0

for line in lines:
    words = line.split()

    for word in words:
        word = word.strip(".,!?")

        if word == "Python":
            count += 1

print("Total Python:", count)
