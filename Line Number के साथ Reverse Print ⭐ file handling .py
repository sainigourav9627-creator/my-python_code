with open("student.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(reversed(lines), start=1):
    print(i, "→", line, end="")
