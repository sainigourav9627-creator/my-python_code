with open("student.txt", "r") as file:
    data = file.read()

count = data.count("Python")

print("Python appears:", count, "times")
