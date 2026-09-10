with open("student.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

for line in sorted(lines):
    print(line)
