with open("student.txt", "r") as file:
    data = file.read()

data = data.replace("Python", "Programming")

with open("student.txt", "w") as file:
    file.write(data)
