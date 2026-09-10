with open("student.txt", "r") as file:
    data = file.read()

print(data)

and


file = open("student.txt", "r")

data = file.read()

print(data)

file.close()
