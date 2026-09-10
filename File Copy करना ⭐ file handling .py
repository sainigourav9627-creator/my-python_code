with open("student.txt", "r") as source:
    data = source.read()

with open("student_copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully")
