with open("student.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    if "Python" in line:
        print("Python found in line:", i)
