with open("student.txt", "r") as file:
    lines = file.readlines()

with open("clean_student.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)

print("Clean file created successfully")
