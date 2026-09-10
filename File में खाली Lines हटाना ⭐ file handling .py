with open("student.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if line.strip():
        print(line.strip())
