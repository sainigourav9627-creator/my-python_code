with open("student.txt", "r") as file:
    lines = file.readlines()

count = 0

for line in lines:
    if "Python" in line:
        count += 1

print("Python found in", count, "line(s)")
